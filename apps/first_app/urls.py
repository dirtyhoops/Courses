from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^(?P<id>\d+)/delete$', views.delete),
    url(r'^(?P<id>\d+)/confirm$', views.confirm)

]
