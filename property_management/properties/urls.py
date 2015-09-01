from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^$', 'index', name='index'),
    url(r'^properties/$', views.properties, name='properties'),
#    url(r'^(?P<property>[0-9]+)/$', views.property, name='property'),
]