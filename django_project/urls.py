"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import include
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static

#we will have to specify what path to include
urlpatterns = [
    path('register/', users_views.register, name='register'),
    path('profile/', users_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'), name = 'blog-home'), #opening blog, we will go to the home of blog coz we specified in blog/urls
    #path('about/', include('blog.urls')) this is unnecessary
    #also if we do not write blog/ inside '' our blog will become the home page of our website
    #also if we want to test we can simply change the path, change blog to blog_dev and in web address too, write blog_dev so that you can run it when no one else can
    
]
#Refer Serving files uploaded by a user during development¶, this helper function works only in debug mode
if settings.DEBUG:  #we did not add it in the original list so that other programmers don't get confused
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)