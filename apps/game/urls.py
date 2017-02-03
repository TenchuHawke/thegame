from django.conf.urls import url
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^main', views.main, name='game_main'),
    url(r'^start_combat', views.start_combat, name='game_combat'),
    url(r'^$', views.index, name='game_index'),

]
