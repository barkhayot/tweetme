from django.urls import path
from . import views

urlpatterns = [
    path('tweets/', views.tweets, name='tweets'),
    path('tweet/<int:pk>/', views.tweetDetail, name='tweetDetail'),
    path('tweetLike/<int:pk>', views.tweetLike, name="tweetLike"),
    path('comment_test/<int:pk>/', views.test_comment, name="comment_test"),

    path('tweetCreate/', views.tweetCreate, name="tweetCreate"),
]