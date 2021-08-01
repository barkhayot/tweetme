from django.urls import path
from . import views

urlpatterns = [
    #path('profiles/', views.profiles, name='profiles'),
    #path('follow/<int:pk>', views.follow, name='follow'),
    #path('profile_detail/<int:pk>', views.profile_detail, name='profile_detail'),
    #path('following/', views.following, name='following'),

    path('register/', views.register, name='register'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('logoutpage/', views.logoutpage, name='logoutpage'),
    path('', views.loginpage, name='loginpage'),

]
