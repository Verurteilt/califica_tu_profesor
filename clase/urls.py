from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from clase import views

urlpatterns = [
    url(r'^clasealumno/(?P<id_clase>[0-9]+)/(?P<matricula>\w+)/$', views.ClaseCalificar.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
