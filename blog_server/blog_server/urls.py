"""blog_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.login),
    path('logout',views.logout),
    path('register', views.register),
    path('getUserInfo',views.getUserInfo),
    path('uploadAvatar', views.uploadAvatar),
    path('uploadCover',views.uploadCover),
    path('uploadImage',views.uploadImage),
    path('uploadCommentImage',views.uploadCommentImage),
    path('writeArticle',views.writeArticle),
    path('addCategory',views.addCategory),
    path('addLabel',views.addLabel),
    path('getCategoryList',views.getCategoryList),
    path('getCategoryCount',views.getCategoryCount),
    path('getLabelList',views.getLabelList),
    path('getLabelCount',views.getLabelCount),
    path('getArticleList',views.getArticleList),
    path('submitComment',views.submitComment),
    path('getCommentList',views.getCommentList),
]
