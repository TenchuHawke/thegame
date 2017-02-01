from django.conf.urls import url
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^add_monster$', views.add_monster, name='add_monster'),
	url(r'^add_item$', views.add_item, name='add_item'),
	url(r'^add_room$', views.add_room, name='add_room'),
	url(r'^add_trap$', views.add_trap, name='add_trap'),
	url(r'^add_treasure$', views.add_treasure, name='add_treasure'),
	url(r'^$', views.index, name='megalist'),
	
	
]
