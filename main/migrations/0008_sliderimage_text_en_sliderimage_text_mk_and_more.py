# Generated by Django 4.1.7 on 2023-03-11 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_sliderimage_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimage',
            name='text_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='text_mk',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='text_sq',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Текст'),
        ),
    ]
