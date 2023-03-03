from django.db import models

class Article:
    title = models.CharField(max_length=150, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at', )

class ArticleImages:
    article = models.ForeignKey(Article, blank=False, null=False, on_delete=models.CASCADE)
    image = models.ImageField(blank=False, null=False)
 
class Slider:
    position = models.SlugField(max_length=50, blank=False, null=False)
    
class SliderImage:
    slider = models.ForeignKey(Slider, blank=False, null=False, on_delete=models.CASCADE)
    order = models.IntegerField(blank=False, null=False, default=1)
    image = models.ImageField(blank=False, null=False)
    
# class GalleryImage:
    # 

# class Employee
# 
# class ContactFormMessage
