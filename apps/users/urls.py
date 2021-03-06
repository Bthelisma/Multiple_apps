from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^users/new$', views.register),
    url(r'^users/(?P<user_id>\d+)$', views.show),
    url(r'^users/(?P<user_id>\d+)/edit$', views.edit),
    url(r'^users/(?P<user_id>\d+)/delete$', views.delete)

  ]
