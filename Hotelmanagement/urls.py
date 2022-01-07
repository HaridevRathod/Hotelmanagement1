"""Hotelmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from Myapp import views
from django.conf.urls.static import static
from django.conf import settings
#from contact import views



urlpatterns = [
    path('Myapp/', include('Myapp.urls')),
    path('login/', views.login),
    path('register/', views.register_request),
    path('ulogin/', views.ulogin),
    path('home/', views.home),
    path('uhome/', views.uhome),
    path('index/', views.index),
    path('logout/', views.logout),
    path('ulogout/', views.ulogout),
    path('form/', views.my_form),
    path('about/', views.about),
    path('thankyou/', views.thankyou),
    path('uform/', views.umy_form),
    path('uCustomerForm/', views.umy_form),
    path('update_delete/', views.update_delete),
    path('delete/<int:id>',views.delete_view),
    path('update/<int:id>',views.update_view),
    path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    

