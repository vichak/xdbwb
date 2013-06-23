from django.conf.urls import patterns, include, url
from django.conf import settings # import the settings file

#static fileserver for development
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.shortcuts import redirect
admin.autodiscover()

urlpatterns = patterns('',
    # Examples
    url(r'^$', 'lib.views.index', name='index'),
    url(r'^movies/', include('lib.movie.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
)
