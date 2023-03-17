from datetime import datetime

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.db.models import Q
from django.utils.translation import get_language

from main.models import Slider, Article, GalleryCategory, GalleryImage

def index(request: HttpRequest):
    slider = Slider.objects.get(position_slug='index-slider')
    newest_articles = Article.objects.order_by('-created_at')[:3]

    return render(request, 'index.html', {
        'slider': slider,
        'articles': newest_articles
    })

def article_list(request: HttpRequest):
    article_filter = {}
    text_filter = ''
    try:
        if request.GET.get('time', None):
            split_time = request.GET.get('time').split('-')
            article_filter['created_at__month'] = int(split_time[1])
            article_filter['created_at__year'] = int(split_time[0])

    except (ValueError, TypeError, IndexError):
        return HttpResponseBadRequest()
    
    if request.GET.get('search', None): 
        text_filter = request.GET.get('search')

    articles = Article.objects.filter(Q(content__icontains=text_filter) | Q(title__icontains=text_filter), **article_filter)

    return render(request, 'article_list.html', {
        'articles': articles
    })

def article(request: HttpRequest, article_id):
    article = get_object_or_404(Article, id=int(article_id))
    return render(request, 'article.html', {
        'article': article
    })

def about_us(request: HttpRequest):
    return render(request, 'about_us.html')

def curriculum(request: HttpRequest):
    return render(request, 'curriculum.html')

def gallery(request: HttpRequest):
    categories = GalleryCategory.objects.prefetch_related('images')
    
    selected_category = request.GET.get('category', None)

    if selected_category:
        images = categories.get(name_slug=selected_category).images
    else:
        images = GalleryImage.objects
    
    return render(request, 'gallery.html', {
        'categories': categories,
        'selected_category': selected_category,
        'images': images,
    })