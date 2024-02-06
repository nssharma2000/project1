# Generated by Django 5.0.1 on 2024-02-02 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_blog_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='like_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='blog_post',
            name='view_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.DeleteModel(
            name='Blog_likes',
        ),
    ]