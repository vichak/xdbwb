from django.conf.urls import patterns, include, url

urlpatterns = patterns('lib.views',
                       url(r'^$',
                           'index', 
                           name='index')
                       )
