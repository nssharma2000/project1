from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone                         
   

# Create your models here.
class Blog_Category(models.Model):
    blog_cat = models.CharField(max_length=60,unique=True)
    blogcat_img = models.ImageField(upload_to='media/images')
    blogcat_description = models.CharField(max_length=200)
    def __str__(self):
        return self.blog_cat
    
class contact_info(models.Model):
    u_email = models.EmailField()
    u_message = models.CharField(max_length=200)
    def _str_(self):
        return self.u_email
    


    
class blog_post(models.Model):
    blog_name = models.CharField(max_length=100)
    cover_img = models.ImageField(upload_to='media/images')
    like_count=models.IntegerField(default=0, null=True)
    views_count=models.IntegerField(default=0, null=True)
    blog_description = RichTextField()
    blog_cat = models.ForeignKey(Blog_Category, on_delete = models.CASCADE, null=True)
    def _str_(self):
        return self.blog_name
    
class Comment(models.Model):
    post = models.ForeignKey(blog_post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def str(self):
        return self.text
    


    

    


    

    



