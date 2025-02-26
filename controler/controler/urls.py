"""
URL configuration for controler project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', views.forum, name='forum'),
    path('', views.forum, name='forum'),
    path('api/comments/', views.get_comments, name='get_comments'),
    path('api/comments/add/', views.add_comment, name='add_comment'),
    path('api/comments/<int:comment_id>/reply/', views.add_reply, name='add_reply'),
    path('api/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]
