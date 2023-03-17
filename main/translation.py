from modeltranslation.translator import translator, TranslationOptions
from main.models import (Article, ArticleImage, GalleryCategory, 
                         GalleryImage, SliderImage, Employee, 
                         Subject, AttachmentCategory, Attachment )

class ArticleTranslation(TranslationOptions):
    fields = ('title', 'content', )

class ArticleImageTranslation(TranslationOptions):
    fields = ('title', )

class GalleryCategoryTranslation(TranslationOptions):
    fields = ('name', )

class GalleryImageTranslation(TranslationOptions):
    fields = ('title', )

class SliderImageTranslation(TranslationOptions):
    fields = ('title', )

class EmployeeTranslation(TranslationOptions):
    fields = ('full_name', 'title', )

class SubjectTranslation(TranslationOptions):
    fields = ('name', )

class AttachmentCategoryTranslation(TranslationOptions):
    fields = ('name', )

class AttachmentTranslation(TranslationOptions):
    fields = ('name', )

translator.register(Article, ArticleTranslation)
translator.register(ArticleImage, GalleryImageTranslation)
translator.register(GalleryCategory, GalleryCategoryTranslation)
translator.register(GalleryImage, GalleryImageTranslation)
translator.register(SliderImage, SliderImageTranslation)
translator.register(Employee, EmployeeTranslation)
translator.register(Subject, SubjectTranslation)
translator.register(AttachmentCategory, AttachmentCategoryTranslation)
translator.register(Attachment, AttachmentTranslation)