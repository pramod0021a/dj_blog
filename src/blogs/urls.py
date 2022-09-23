from django.urls import path
from . import views

app_name = 'blogs' 

urlpatterns = [
path('', views.IndexView.as_view(), name='home'), 
path('post_detail/<int:pk>/', views.DetailPostView.as_view(), name='post_detail'),
path('post_add/', views.AddPostView.as_view(), name='post_add'),
path('category_add/', views.AddCategoryView.as_view(), name='category_add'),
path('post_detail/edit/<str:pk>/', views.UpdatePostView.as_view(), name='post_update'),
path('post_detail/<int:pk>/remove/', views.DeletePostView.as_view(), name='post_delete'),
path('post_detail/<int:pk>/comment', views.AddCommentView.as_view(), name='add_comment'),

path('category_list/', views.CategoryListView, name='category_list'),
path('category/<str:cats>/', views.CategoryView, name='category'),
path('like/<int:pk>/', views.LikeView, name='post_like'),
]