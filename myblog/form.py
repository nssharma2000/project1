from django import forms
from .models import Blog_Category, blog_post, Comment
from django.forms import ModelForm
 


class Blog_Form(ModelForm):
    class Meta:
         model = Blog_Category
         fields = '__all__'

class BlogPost_Form(ModelForm):
    class Meta:
         model = blog_post
         fields = "__all__"

class CommentForm(ModelForm):
     class Meta:
          model=Comment
          fields=('post', 'author', 'text', 'created_date')
          exclude = ['post', 'created_date', 'author']
          widgets = {'text': forms.Textarea(attrs={'placeholder': 'Add Comments', 'rows': 3})}
