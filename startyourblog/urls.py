"""startyourblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from blogging.views import login
# from blogging.views import data
from blogging.views import Home
from blogging.views import ( Data_to_get_post, Show_all_blogs, Show_details, Delete_Blog)
from blogging.views import Login_page
from blogging.views import Details_page
from django.views.generic import TemplateView, CreateView, DeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',Login_page.as_view(),name="login_page"),
    path('data/',Data_to_get_post.as_view(),name="data"),
    path('details/',Details_page.as_view(),name="details_page"),
    path('home/', Show_all_blogs.as_view(),name="home"),
    path('home/<pk>/',Show_details.as_view(),name="detail"),
    path('delete/<pk>/',Delete_Blog.as_view(),name="delete")
]
