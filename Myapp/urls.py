from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views



from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^register/$', views.register_request, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^ulogin/$', views.ulogin, name='ulogin'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^ulogout/$', views.ulogout, name='ulogout'),
    url(r'^home/$', views.home, name='home'),
    url(r'^uhome/$', views.uhome, name='uhome'),
    url(r'^form/$', views.my_form, name='form'),
    url(r'^uform/$', views.umy_form, name='uform'),
    url(r'^about/$', views.about, name='about'),
    url(r'^thankyou/$', views.thankyou, name='thankyou'),
    url(r'^update_delete/$', views.update_delete, name='update_delete'),
    url(r'^delete_view/$', views.delete_view, name='delete_view'),
    url(r'^update_view/$', views.update_view, name='update_view'),
]