from .form import Blog_Form, BlogPost_Form, CommentForm
from django.shortcuts import redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog_Category, contact_info, blog_post, Comment
from django.utils.html import strip_tags
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    # return HttpResponse('<h1>this is the home page</h1>')
    #fetch the data from db
    x=Blog_Category.objects.all()
    # print (x)
    return render(request, 'myblog/home.html',{"category":x})
def contact(request):
    # return HttpResponse('<h1>this is the contact page</h1>')
    if request.method == 'GET':
        return render(request, 'myblog/contact.html')
    elif request.method == 'POST':
        email = request.POST.get('user_email')
        message = request.POST.get('message')
        x = contact_info(u_email=email, u_message=message)
        x.save()
        print(email)
        print(message)
        return render(request,'myblog/contact.html',{'feedback':'Your message has been recorded'})


def blog(request):
    category_name = request.GET.get('category')
    if category_name:
        blogs = blog_post.objects.filter(blog_cat__blog_cat=category_name)
    else:
        blogs = blog_post.objects.all()
    print(blogs)
    return render(request, 'myblog/blog.html', {"blogs": blogs, "category": category_name})
    


            
        
def ck(request):
    x = BlogPost_Form()
    return render(request,'myblog/ck.html',{"x":x})

def sub(request):
    if request.method == 'GET':
        return render(request, 'myblog/sub.html')
    elif request.method == 'POST':
        email = request.POST.get('use_email')
        if SubscribedUser.objects.filter(u_email=email).exists():
            return render(request, 'myblog/sub.html', {'feedback': 'Already Subscribed'})
        else:
            x = SubscribedUser(u_email=email)
            x.save()
            return render(request, 'myblog/sub.html', {'feedback': 'Thank You for subscribing to our page'})

def allblogs(request):
    y=blog_post.objects.all()
    return render(request,'myblog/allblogs.html',{"y":y})

def blog_details(request, blog_id):
    obj = get_object_or_404(blog_post, pk=blog_id)
    strip_tags(blog_post.blog_description)
    z=obj.views_count
    z=z+1
    obj.views_count=z
    obj.save()
    return render(request,'myblog/blog_details.html', {"obj":obj})
    

def login_u(request):
    if request.method == "GET":
        return render(request, 'myblog/login_u.html', {'form' : AuthenticationForm()})
    else:
        a = request.POST.get('username')
        b = request.POST.get('password')
        user = authenticate(request, username = a, password = b)
        if user is None:
            return render(request, 'myblog/login_u.html', {'form': AuthenticationForm(), 'error' : 'Invalid credentials'})
        else:
            login(request, user)
            return redirect('home')
    
def signup(request):
    if request.method == 'GET':
        return render(request, 'myblog/signup.html', {'form' : UserCreationForm()})
    else:
        a = request.POST.get('username')
        b = request.POST.get('password1')
        c = request.POST.get('password2')
        if b == c:
            if(User.objects.filter(username = a)):
                return render(request, 'myblog/signup.html', {'form' : UserCreationForm(), 'error' : 'Username already exists. Try again with a different username.'})
            else:
                user = User.objects.create_user(username = a, password = b)
                user.save()
                login(request, user)
                return redirect('home')

        else:
            return render(request, 'myblog/signup.html', {'form' : UserCreationForm(), 'error' : 'Password mismatch. Try again.'})

    
def logout_u(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home')

def addLikes(request, blog_id):
    obj = get_object_or_404(blog_post, pk=blog_id)
    print(obj.like_count)
    y=obj.like_count
    y=y+1
    obj.like_count=y
    obj.save()
    return redirect('blog_details', obj.id)

def add_comment(request, blog_id):
    post = get_object_or_404(blog_post, pk=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.created_at = timezone.now()  # Add this line to save the current timestamp
            comment.save()
            return redirect('blog_details', blog_id=post.id)

def delete_comment(request, blog_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect( 'blog_details', blog_id=blog_id)

def edit_comment(request, blog_id, comment_id):
    # Retrieve the comment object
    comment = Comment.objects.get(id=comment_id)
    
    if request.method == 'POST':
        # Process the form submission
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog_details', blog_id=blog_id)
    else:
        # Populate the form with existing comment data
        form = CommentForm(instance=comment)
    
    return render(request, 'myblog/edit_comment.html', {'form': form})






    


    
    
    






    


    



    