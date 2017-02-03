from django.conf.urls import url
from django.conf.urls import url
from . import views
urlpatterns = [

    # Delete URLS
    url(r'^delete_monster$', views.delete_monster, name='delete_monster'),
    url(r'^delete_item$', views.delete_item, name='delete_item'),
    url(r'^delete_room$', views.delete_room, name='delete_room'),
    url(r'^delete_trap$', views.delete_trap, name='delete_trap'),
    url(r'^delete_treasure$', views.delete_treasure, name='delete_treasure'),
    url(r'^delete_user$', views.delete_user, name='delete_user'),
    url(r'^delete_character$', views.delete_character, name='delete_character'),
    #Assign URLS
    url(r'^assign_monster$', views.assign_monster, name='assign_monster'),
    url(r'^assign_trap$', views.assign_trap, name='assign_trap'),
    url(r'^assign_treasure$', views.assign_treasure, name='assign_treasure'),
    url(r'^assign_visitor$', views.assign_visitor, name='assign_visitor'),
    url(r'^assign_explorer$', views.assign_explorer, name='assign_explorer'),
    url(r'^assign_killer$', views.assign_killer, name='assign_killer'),
    url(r'^assign_item$', views.assign_item, name='assign_item'),
    #Select links URLS
    url(r'^room_monster$', views.room_monster, name='room_monster'),
    url(r'^room_visitor$', views.room_visitor, name='room_visitor'),
    url(r'^room_explorer$', views.room_explorer, name='room_explorer'),
    url(r'^room_trap$', views.room_trap, name='room_trap'),
    url(r'^room_treasure$', views.room_treasure, name='room_treasure'),
    url(r'^room_killer$', views.room_killer, name='room_killer'),
    url(r'^room_exit$', views.room_exit, name='room_exit'),
    url(r'^character_item', views.character_item, name='character_item'),
    #Add URLS
    url(r'^add_monster$', views.add_monster, name='add_monster'),
    url(r'^add_item$', views.add_item, name='add_item'),
    url(r'^add_room$', views.add_room, name='add_room'),
    url(r'^add_trap$', views.add_trap, name='add_trap'),
    url(r'^add_treasure$', views.add_treasure, name='add_treasure'),
    url(r'^add_exit$', views.add_exit, name='add_exit'),
    #Remove URLS
    url(r'^remove_killer$', views.remove_killer, name='remove_killer'),
    url(r'^remove_treasure$', views.remove_treasure, name='remove_treasure'),
    url(r'^remove_monster$', views.remove_monster, name='remove_monster'),
    url(r'^remove_visitor$', views.remove_visitor, name='remove_visitor'),
    url(r'^remove_explorer$', views.remove_explorer, name='remove_explorer'),
    url(r'^remove_trap$', views.remove_trap, name='remove_trap'),
    url(r'^remove_character$', views.remove_character, name='remove_character'),
    #Admin URLS
    url(r'^admin_characters$', views.admin_characters, name='admin_characters'),
    url(r'^admin_items$', views.admin_items, name='admin_items'),
    url(r'^admin_monsters$', views.admin_monsters, name='admin_monsters'),
    url(r'^admin_rooms$', views.admin_rooms, name='admin_rooms'),
    url(r'^admin_traps$', views.admin_traps, name='admin_traps'),
    url(r'^admin_treasure$', views.admin_treasure, name='admin_treasure'),
    url(r'^admin_users$', views.admin_users, name='admin_users'),
    #Edit URLS
    url(r'^edit_user/(?P<id>\d+)$', views.edit_user, name='edit_user'),
    url(r'^edit_character/(?P<id>\d+)$', views.edit_character, name='edit_character'),
    url(r'^edit_monster/(?P<id>\d+)$', views.edit_monster, name='edit_monster'),
    url(r'^edit_item/(?P<id>\d+)$', views.edit_item, name='edit_item'),
    url(r'^edit_treasure/(?P<id>\d+)$', views.edit_treasure, name='edit_treasure'),
    url(r'^edit_trap/(?P<id>\d+)$', views.edit_trap, name='edit_trap'),
    url(r'^edit_room/(?P<id>\d+)$', views.edit_room, name='edit_room'),
    #Update URLS
    url(r'^update_user$', views.update_user, name='update_user'),
    url(r'^update_character$', views.update_character, name='update_character'),
    url(r'^update_monster$', views.update_monster, name='update_monster'),
    url(r'^update_item$', views.update_item, name='update_item'),
    url(r'^update_treasure$', views.update_treasure, name='update_treasure'),
    url(r'^update_trap$', views.update_trap, name='update_trap'),
    url(r'^update_room$', views.update_room, name='update_room'),
    #Catch All (DONT MOVE)
    url(r'^$', views.index,  name='index'),
]
