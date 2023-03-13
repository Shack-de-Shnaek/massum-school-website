from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline, StackedInline

from main.models import Article, ArticleImage, Slider, SliderImage, GalleryCategory, GalleryImage, Employee, Subject, ContactFormMessage

class ArticleImageInline(TabularInline):
    model = ArticleImage
    fields = ('image', 'title_mk', 'title_en', 'title_sq', )

@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    inlines = (ArticleImageInline, )

class SliderImageInline(TabularInline):
    model = SliderImage
    fields = ('order', 'image', 'title_mk', 'title_en', 'title_sq', )

@admin.register(Slider)
class SliderAdmin(ModelAdmin):
    inlines = (SliderImageInline, )

class GalleryImageInline(TabularInline):
    model = GalleryImage

@admin.register(GalleryCategory)
class GalleryCategoryAdmin(ModelAdmin):
    inlines = (GalleryImageInline, )

@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    pass

class SubjectInline(TabularInline):
    model = Subject

@admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    # inlines = (SubjectInline, )
    pass

@admin.register(ContactFormMessage)
class ContactFormMessageAdmin(ModelAdmin):
    pass