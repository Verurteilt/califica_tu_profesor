from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'califica_tu_profesor.views.home', name='home'),
    url(r'^clase/', include('clase.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
