from django.shortcuts import render
from django.http import HttpRequest

from main.models import Slider, Article

# Create your views here.
def index(request: HttpRequest):
    slider = Slider.objects.get(position_slug='index-slider')
    newest_articles = Article.objects.order_by('-created_at')[:3]

    return render(request, 'index.html', {
        'slider': slider,
        'articles': newest_articles
    })