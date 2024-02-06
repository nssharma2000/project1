from .form import Blog_Form, BlogPost_Form
from django.shortcuts import redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog_Category, contact_info, blog_post
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
    
def search1(request):
    if request.method == 'POST':
        x = request.POST.get('search_s')
        print(x)
        return redirect('home')


def blog(request):
    x = Blog_Form()  
    if request.method == "GET":
        return render(request,'myblog/blog.html',{"x":x})
    else:
        print("hi")
        form = Blog_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("hi")
            return redirect('')
        else:
            return render(request,'myblog/blog.html',{"x":x})

            
        
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
    print(obj)
    print(blog_id)
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


