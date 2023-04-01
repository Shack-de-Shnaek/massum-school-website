# Generated by Django 4.1.7 on 2023-04-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_adding_more_attachment_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='employees',
        ),
        migrations.AddField(
            model_name='employee',
            name='subjects',
            field=models.ManyToManyField(related_name='subjects', to='main.subject', verbose_name='Предмети'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Име'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Име'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name_mk',
            field=models.CharField(max_length=50, null=True, verbose_name='Име'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name_sq',
            field=models.CharField(max_length=50, null=True, verbose_name='Име'),
        ),
    ]
