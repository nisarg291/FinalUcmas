"""ucmas URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
# from users import views as user_views
from . import views
urlpatterns = [
    path("listening",views.listening,name="listening"),
    path("",views.login,name="login"),
    path("index",views.index,name="index"),
    path("home",views.home,name="home"),
    path("generate_add",views.generate_add,name="generate_add"),
    path("generate_multi",views.generate_multi,name="generate_multi"),
    path("addition",views.addition,name="addition"),
    path("division",views.division,name="division"),
    path("multiplication",views.multiplication,name="multiplication"),
    path("flash_addition",views.flash_addition,name="flash_addition"),
    path("flash_division",views.flash_division,name="flash_division"),
    path("flash_multiplication",views.flash_multiplication,name="flash_multiplication"),
    path("generate_flash_addition",views.generate_flash_addition,name="generate_flash_addition"),
    path("generate_flash_multi",views.generate_flash_multi,name="generate_flash_multi"),
    path("generate_flash_div",views.generate_flash_div,name="generate_flash_div"),
    path("logout",views.logout,name="logout"),
    path("flash",views.flash,name="flash"),
    path("validate",views.validate,name="validate"),
]
