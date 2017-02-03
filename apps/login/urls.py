from django.conf.urls import url
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^main$', views.main, name='login_main'),
    url(r'^log_in$', views.login, name='log-in'),
    url(r'^checklogin$', views.login),
    url(r'^register$', views.register),
    url(r'logout$', views.logout, name='logout'),
    url(r'^$', views.index, name='index'),
]
