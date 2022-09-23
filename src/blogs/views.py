from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# ListView
class IndexView(ListView):   
   model = Post
   template_name = 'blogs/index.html'
   ordering = ['-post_date']
   
   def get_context_data(self, *args, **kwargs):
      cat_menu = Category.objects.all()
      context = super(IndexView, self).get_context_data(*args, **kwargs)
      context["cat_menu"] = cat_menu 
      return context
   
   
# DetailView
class DetailPostView(DetailView):     
   model = Post
   template_name = 'blogs/post_detail.html'
   
   def get_context_data(self, *args, **kwargs):
      cat_menu = Category.objects.all()
      context = super(DetailPostView, self).get_context_data(*args, **kwargs)
      
      stuff = get_object_or_404(Post, id=self.kwargs['pk'])
      total_likes = stuff.total_likes()
      
      liked = False
      if stuff.likes.filter(id=self.request.user.id).exists():
         liked = True
      
      context["cat_menu"] = cat_menu 
      context["total_likes"] = total_likes
      context["liked"] = liked
      return context

# CreateView for add post
class AddPostView(CreateView):   
   model = Post
   template_name = 'blogs/post_add.html'
   # form_class = PostForm
   # fields = '__all__'
   fields = ('category','title', 'body', 'header_image')
   
# CreateView for add category
class AddCategoryView(CreateView):   
   model = Category
   template_name = 'blogs/category_add.html'
   # form_class = EditForm
   fields = '__all__'
   
# CreateView for add comments
class AddCommentView(CreateView):   
   model = Comment
   template_name = 'blogs/add_comment.html'
   form_class = CommentForm
   success_url = reverse_lazy('blogs:home')
   
   def form_valid(self, form):
      form.instance.post_id = self.kwargs['pk']
      return super().form_valid(form)
   
   
# UpdateView
class UpdatePostView(UpdateView):  
   model = Post
   template_name = 'blogs/post_update.html'
   form_class = EditForm   
   # fields = ['title', 'title_tag', 'body']

# DeleteView
class DeletePostView(DeleteView):   
   model = Post
   template_name = 'blogs/post_delete.html'
   success_url = reverse_lazy('blogs:home')
   
#  Function view for Category list 
def CategoryListView(request):
   qs = Category.objects.all()
   context = {
      'cat_menu_list':qs,
   }
   return render (request, 'blogs/category_list.html', context ) 

# Function view for adding category pages
def CategoryView(request, cats):
   qs = Post.objects.filter(category=cats.replace('-', ' '))
   context = {
      'category_posts':qs,
      'cats':cats.title().replace('-', ' '),
   }
   return render (request, 'blogs/category.html', context )

# Add like button
def LikeView(request, pk):
   post = get_object_or_404(Post, id=request.POST.get('post_id'))
   liked = False
   if post.likes.filter(id=request.user.id).exists():
      post.likes.remove(request.user)
      liked = False
   else:
      post.likes.add(request.user)
      liked = True
   return HttpResponseRedirect(reverse('blogs:post_detail', args=[str(pk)]))