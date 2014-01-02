from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from cv import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.homepage, name='vote'),
    url(r'^admin/', include(admin.site.urls)),
)
