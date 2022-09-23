from django.urls import path
from . import views

app_name = 'members' 

urlpatterns = [
path('', views.UserRegistrationView.as_view(), name='register'),
path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
path('password/', views.PasswordsChangeView.as_view()),
path('password_success/', views.password_success, name='password_success'),
path('<int:pk>/profile/', views.ShowProfilePageView.as_view(), name='show_profile_page'),
path('<int:pk>/edit_profile_page/', views.EditProfilePageView.as_view(), name='edit_profile_page'),
path('create_profile_page/', views.CreateProfilePageView.as_view(), name='create_profile_page'),

]