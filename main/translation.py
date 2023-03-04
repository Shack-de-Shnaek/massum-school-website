from modeltranslation.translator import translator, TranslationOptions
from main.models import Article, GalleryCategory, GalleryImage, Employee, Subject 

class ArticleTranslation(TranslationOptions):
    fields = ('title', 'content', )

class GalleryCategoryTranslation(TranslationOptions):
    fields = ('name', )

class GalleryImageTranslation(TranslationOptions):
    fields = ('title', )

class EmployeeTranslation(TranslationOptions):
    fields = ('full_name', 'title', )

class SubjectTranslation(TranslationOptions):
    fields = ('name', )

translator.register(Article, ArticleTranslation)
translator.register(GalleryCategory, GalleryCategoryTranslation)
translator.register(GalleryImage, GalleryImageTranslation)
translator.register(Employee, EmployeeTranslation)
translator.register(Subject, SubjectTranslation)
