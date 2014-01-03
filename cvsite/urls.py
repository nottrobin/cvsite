from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
import cvsite.views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='vote'),
    url(r'^profiles.json$', cvsite.views.profiles, name='profiles'),
    url(r'^admin/', include(admin.site.urls)),
)
