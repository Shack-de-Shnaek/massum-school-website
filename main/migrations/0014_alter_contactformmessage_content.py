# Generated by Django 4.1.7 on 2023-03-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_attachment_name_en_attachment_name_mk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmessage',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Содржина'),
        ),
    ]