from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.get_dashboard, name='Dashboard'),
    #url(r'^app/dashboard',views.get_dashboard,name='Dashboard'),
   url(r'^$', views.get_home,name='home')

]