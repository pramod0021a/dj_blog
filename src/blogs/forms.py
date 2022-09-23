from random import choices
from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
   choice_list.append(item)

class PostForm(forms.ModelForm):
   class Meta:
      model = Post
      fields = ('category','title', 'title_tag', 'author', 'body', 'header_image')
      

      widgets = {
         'category':forms.Select( choices=choices, attrs={'class':'form-control'}),
         'title':forms.TextInput(attrs={'class':'form-control'}),
         'title_tag':forms.TextInput(attrs={'class':'form-control'}),
         'author':forms.Select(attrs={'class':'form-control'}),
         'body':forms.Textarea(attrs={'class':'form-control'}),
      }

class EditForm(forms.ModelForm):
   class Meta:
      model = Post
      fields = ('category', 'title', 'title_tag', 'body', 'header_image')
     
      widgets = {
         'category':forms.Select(choices=choices, attrs={'class':'form-control'}),         
         'title':forms.TextInput(attrs={'class':'form-control'}),
         'title_tag':forms.TextInput(attrs={'class':'form-control'}),         
         'body':forms.Textarea(attrs={'class':'form-control'}),
      }
      
class CommentForm(forms.ModelForm):
   class Meta:
      model = Comment
      fields = ('name', 'body')
     
      widgets = {                 
         'name':forms.TextInput(attrs={'class':'form-control'}),                  
         'body':forms.Textarea(attrs={'class':'form-control'}),
      }