# Generated by Django 4.1.7 on 2023-04-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_employee_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='subjects', to='main.subject', verbose_name='Предмети'),
        ),
    ]