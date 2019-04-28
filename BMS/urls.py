"""BMS URL Configuration

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
from index import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('add_publisher/', views.add_publisher),
    path('delete_publisher/', views.delete_publisher),
    path('update_publisher/', views.update_publisher),
    path('add_book/', views.add_book),
    path('add_author/', views.add_author),
    path('update_book/', views.update_book),
    path('update_author/', views.update_author),
    path('delete_author/', views.delete_author),
    path('delete_book/', views.delete_book),
]
