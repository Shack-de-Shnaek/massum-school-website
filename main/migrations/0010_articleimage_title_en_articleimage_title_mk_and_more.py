# Generated by Django 4.1.7 on 2023-03-13 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_text_sliderimage_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleimage',
            name='title_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='articleimage',
            name='title_mk',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='articleimage',
            name='title_sq',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Текст'),
        ),
    ]
