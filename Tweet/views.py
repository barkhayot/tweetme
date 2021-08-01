from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Tweet, TweetComment
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from . forms import NewCommentForm, TweetCreateForm
from django.utils import timezone
from Profiles.models import Profile


# Create your views here.

@login_required(login_url='loginpage')
def tweets(request):
    tweet = Tweet.objects.filter().order_by('-created_at')

    #data = super().get_context_data(**kwargs)
    

    context = {
        'tweets': tweet
    }
    return render(request, 'tweet/tweets.html', context)



def tweetLike(request, pk):
    tweet = get_object_or_404(Tweet, id=request.POST.get('tweet_id'))
    if tweet.likes.filter(id=request.user.id).exists():
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)

    return HttpResponseRedirect(reverse('tweetDetail', args=[int(pk)]))

def tweetDetail(request, pk):
    tweetObj = get_object_or_404(Tweet, pk=pk)
    likes_connected = get_object_or_404(Tweet, pk=pk)
    liked = False
    
    
    # Tweet Like Counting 
    if likes_connected.likes.filter(id=request.user.id).exists():
        liked = True
    num_of_likes = likes_connected.num_of_likes()
    tweet_is_liked = liked

    # Tweet Comment Section
    comment_form = NewCommentForm
    comment = TweetComment.objects.filter(tweet=tweetObj).order_by('-date_posted')
    if request.user.is_authenticated:
        comment_form = NewCommentForm
        if request.method == 'POST':
            comment_form = NewCommentForm(request.POST)
            comment = comment_form.save(commit=False)
            comment.tweet = tweetObj
            comment.user = request.user
            comment.save()
            return redirect('tweetDetail', pk=tweetObj.pk)
            

    context ={
        'tweetObj': tweetObj,
        'num_of_likes': num_of_likes,
        'tweet_is_liked': tweet_is_liked,
        'comments': comment,
        'comment_form': comment_form,
    }
    return render(request, 'tweet/tweetDetail.html', context)


def tweetCreate(request):
    new_tweet = TweetCreateForm()
    if request.method == 'POST':
        new_tweet = TweetCreateForm(request.POST)
        if new_tweet.is_valid():
            tweet = new_tweet.save(commit=False)
            tweet.user = request.user
            tweet.created_at = timezone.localtime(timezone.now())
            tweet.save()
            return redirect('tweetDetail', pk=tweet.pk)

    context = {
        'new_tweet': new_tweet 
    }
    return render(request, 'tweet/tweetCreate.html', context)



def test_comment(request, pk):
    user = get_object_or_404(Profile, pk=pk)
    tweet = Tweet.objects.filter(user=request.Profile)
    

    #comment = TweetComment.objects.filter(tweet=tweet)

    context = {
        'user': user,
        'tweets': tweet
        
    }
    return render(request, 'tweet/comment_test.html', context) 