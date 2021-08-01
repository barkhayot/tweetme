from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(User, related_name='followers', symmetrical=False, blank=True)
    bio = models.TextField(default='No Bio..')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def profiles_tweets(self):
        return self.tweet_set.all()

    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        ordering  = ('-created_at',) 
