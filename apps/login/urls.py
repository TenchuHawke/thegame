from django.conf.urls import url
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login$', views.loginreg, name='login'),
	url(r'^/checklogin$', views.login),
	url(r'^/register$', views.register),
	url(r'^logout$', views.logout, name='logout'),

]