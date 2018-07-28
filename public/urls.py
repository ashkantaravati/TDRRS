from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.get_home,name='home'),
   url(r'^defense-schedule', views.get_schedule,name='defense_schedule')

]