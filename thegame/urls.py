from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^game/', include('apps.game.urls', namespace='Game')),
    url(r'^mainmenu/', include('apps.mainmenu.urls', namespace='Mainmenu')),
    url(r'^login/', include('apps.login.urls', namespace='Login')),
    url(r'^admin/', include('apps.gameadmin.urls', namespace='Admin')),
    url(r'^', include('apps.login.urls', namespace='Login')),
]
