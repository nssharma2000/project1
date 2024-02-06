# Generated by Django 5.0.1 on 2024-01-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_cat', models.CharField(max_length=60, unique=True)),
                ('blogcat_img', models.ImageField(upload_to='media/images/')),
                ('blogcat_description', models.CharField(max_length=200)),
            ],
        ),
    ]