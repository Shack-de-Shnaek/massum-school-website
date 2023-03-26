# Generated by Django 4.1.7 on 2023-03-26 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_adding_attachment_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='main.attachmentcategory'),
        ),
    ]
