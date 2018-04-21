from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^s',views.simple,name='simple'),
    url(r'^login',views.login,name='login'),
    url(r'^DefenseTimes',views.readAllDefenseTimes,name='All Defense Times'),
    url(r'^logout$',views.doLogout,name='logout')
]