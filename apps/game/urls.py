from django.conf.urls import url
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^add_monster$', views.add_monster, name='add_monster'),
	url(r'^delete_monster$', views.delete_monster, name='delete_monster'),
	url(r'^add_item$', views.add_item, name='add_item'),
	url(r'^delete_item$', views.delete_item, name='delete_item'),
	url(r'^add_room$', views.add_room, name='add_room'),
	url(r'^delete_room$', views.delete_room, name='delete_room'),
	url(r'^add_trap$', views.add_trap, name='add_trap'),
	url(r'^delete_trap$', views.delete_trap, name='delete_trap'),
	url(r'^add_treasure$', views.add_treasure, name='add_treasure'),
	url(r'^delete_treasure$', views.delete_treasure, name='delete_treasure'),
	url(r'^assign_monster$', views.assign_monster, name='assign_monster'),
	url(r'^assign_trap$', views.assign_trap, name='assign_trap'),
	url(r'^assign_treasure$', views.assign_treasure, name='assign_treasure'),
	url(r'^assign_visitor$', views.assign_visitor, name='assign_visitor'),
	url(r'^assign_explorer$', views.assign_explorer, name='assign_explorer'),
	url(r'^room_monster$', views.room_monster, name='room_monster'),
	url(r'^room_visitor$', views.room_visitor, name='room_visitor'),
	url(r'^room_explorer$', views.room_explorer, name='room_explorer'),
	url(r'^room_trap$', views.room_trap, name='room_trap'),
	url(r'^room_treasure$', views.room_treasure, name='room_treasure'),
	url(r'^$', views.index, name='megalist'),
	
	
]
