# Generated by Django 5.0.1 on 2024-02-02 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_blog_post_like_count_blog_post_view_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='blog_comments',
            field=models.CharField(default='', max_length=300),
        ),
    ]