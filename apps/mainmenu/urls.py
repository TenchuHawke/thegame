from django.conf.urls import url
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^create$', views.create, name='create'),
	url(r'^delete$', views.delete, name='delete'),
	url(r'^hall$', views.hall, name='hall'),
	url(r'^updatechar$', views.update),
	url(r'^roll$', views.roll, name='roll'),
	url(r'^show$', views.showcreate, name='show'),
	url(r'^create$', views.create),

]