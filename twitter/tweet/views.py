from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm


def index(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'tweets': tweets})
