import os, sys

sys.path.append('/var/www/xdbwb')

os.environ['DJANGO_SETTINGS_MODULE'] = 'xdbwb.settings'

import django.core.handlers.wsgi

_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    #environ['SCRIPT_NAME'] = '/'
    environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
    return _application(environ, start_response)

