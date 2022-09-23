from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse



class Profile(models.Model):
   user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
   bio = models.TextField()
   profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
   website_url = models.CharField(max_length=200,  blank=True, null=True) 
   facebook_url = models.CharField(max_length=200,  blank=True, null=True)
   youtube_url = models.CharField(max_length=200,  blank=True, null=True)
   instagram_url = models.CharField(max_length=200,  blank=True, null=True)
   twitter_url = models.CharField(max_length=200,  blank=True, null=True)

   def __str__(self):      
      return str(self.user)
   
   def get_absolute_url(self):      
      return reverse('blogs:home')


class Category(models.Model):
   name = models.CharField(max_length=200)

   def __str__(self):      
      return self.name
   
   # needed for CreateView
   def get_absolute_url(self):      
      return reverse('blogs:home')

class Post(models.Model):    
   category = models.CharField(max_length=200,  blank=True)        
   title = models.CharField(max_length=200)
   title_tag = models.CharField(max_length=200, default='MyBlog:')
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   body = models.TextField()
   header_image = models.ImageField(null=True, blank=True, upload_to='images/', default='')
   snippet = models.CharField(max_length=255, default='Click Link above to Read Blog Post... ')
   post_date = models.DateField(auto_now_add=True)
   likes = models.ManyToManyField(User, related_name='blog_posts')

   def __str__(self):
      return self.title + '| ' +  str(self.author)
   
   def total_likes(self):
      return self.likes.count()
   
   # needed for CreateView
   def get_absolute_url(self):      
      return reverse('blogs:home')
      # return reverse('blogs:post_detail', args=(str(self.id)))
   
class Comment(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
   name = models.CharField(max_length=200)
   body = models.TextField(null=True, blank=True)
   date_added = models.DateTimeField(auto_now_add=True)   

   def __str__(self):      
      return '%s - %s' % (self.post.title, self.name)