from django.contrib import admin
from django.urls import path
from myblog import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('ck', views.ck, name='ck'),
    path('allblogs', views.allblogs, name='allblogs'),
    path('blog_details/<str:blog_id>/',views.blog_details,name ='blog_details'),
    path('login_u', views.login_u, name='login_u'),
    path('signup', views.signup, name='signup'),
    path('logout_u', views.logout_u, name='logout_u'),
    path('addLikes/<str:blog_id>', views.addLikes, name='addLikes'),
    path('add_comment/<str:blog_id>/',views.add_comment, name='add_comment'),
    path('delete_comment/<int:blog_id>/<int:comment_id>/',views.delete_comment, name='delete_comment'),
    path('edit_comment/<int:blog_id>/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    
    


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)