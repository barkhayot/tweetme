from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet_text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='tweet_like', blank=True)

    def __str__(self):
        return self.tweet_text

    def num_of_likes(self):
        return self.likes.count()
        
    @property
    def num_of_comments(self):
        return TweetComment.objects.filter(tweet=self).count()

class TweetComment(models.Model):
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='comments')
    content = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ', ' + self.tweet.tweet_text[:40]
