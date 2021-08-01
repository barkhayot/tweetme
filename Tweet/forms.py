from django import forms
from django.forms import ModelForm
from .models import TweetComment, Tweet


class TweetCreateForm(ModelForm):

    class Meta:
        model = Tweet
        fields = ['tweet_text']

    tweet_text = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Share your thoughts...',
        'class': 'form-control',
        'rows': '5'
        
    }))

class NewCommentForm(ModelForm):


    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Leave Your comments.',
        'class': 'form-control',
        'rows': '5'
        
    }))

    class Meta:
        model = TweetComment
        fields = ['content']

