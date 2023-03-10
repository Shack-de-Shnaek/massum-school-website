# Generated by Django 4.1.7 on 2023-03-04 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('title_mk', models.CharField(max_length=150, null=True)),
                ('title_en', models.CharField(max_length=150, null=True)),
                ('title_sq', models.CharField(max_length=150, null=True)),
                ('content', models.TextField()),
                ('content_mk', models.TextField(null=True)),
                ('content_en', models.TextField(null=True)),
                ('content_sq', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ContactFormMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('full_name_mk', models.CharField(max_length=50, null=True)),
                ('full_name_en', models.CharField(max_length=50, null=True)),
                ('full_name_sq', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=20)),
                ('title_mk', models.CharField(max_length=20, null=True)),
                ('title_en', models.CharField(max_length=20, null=True)),
                ('title_sq', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('name_mk', models.CharField(max_length=50, null=True)),
                ('name_en', models.CharField(max_length=50, null=True)),
                ('name_sq', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('name_mk', models.CharField(max_length=20, null=True)),
                ('name_en', models.CharField(max_length=20, null=True)),
                ('name_sq', models.CharField(max_length=20, null=True)),
                ('employees', models.ManyToManyField(related_name='subjects', to='main.employee')),
            ],
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to='')),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.slider')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('name_mk', models.CharField(max_length=50, null=True)),
                ('name_en', models.CharField(max_length=50, null=True)),
                ('name_sq', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='images', to='main.gallerycategory')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.article')),
            ],
        ),
    ]
