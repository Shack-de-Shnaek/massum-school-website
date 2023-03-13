from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest

from main.models import Slider, Article

def index(request: HttpRequest):
    slider = Slider.objects.get(position_slug='index-slider')
    newest_articles = Article.objects.order_by('-created_at')[:3]

    return render(request, 'index.html', {
        'slider': slider,
        'articles': newest_articles
    })

def article_list(request: HttpRequest):
    year = None
    month = None
    
    try:
        if 'year' in request.GET: year = int(request.GET.get('year'))
        if 'month' in request.GET: month = int(request.GET.get('month'))
    except:
        return HttpResponseBadRequest()

    articles = Article.objects.all()

    return render(request, 'article_list.html', {
        'articles': articles
    })

def article(request: HttpRequest, article_id):
    article = get_object_or_404(Article, id=int(article_id))
    return render(request, 'article.html', {
        'article': article
    })