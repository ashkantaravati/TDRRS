from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='Dashboard'),
    url(r'^Dashboard',views.index,name='Dashboard'),
    url(r'^login$',views.doLogin,name='login'),
    url(r'^DefenseTimes',views.readAllDefenseTimes,name='DefenseTimes'),
    url(r'^myRequests',views.myRequests,name='MyRequests'),    
    url(r'^logout$',views.doLogout,name='logout'),
    url(r'^changePassword',views.changePassword,name='changePassword'),        
]