"""
WSGI config for thatforum project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys, site
if 'DJANGO_SETTINGS_MODULE' not in os.environ:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "commwar.settings")

import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    os.environ['THATFORUM_DB_PASS'] = environ['THATFORUM_DB_PASS']
    os.environ['DJANGO_SETTINGS_MODULE'] = environ['DJANGO_SETTINGS_MODULE']
    os.environ['THATFORUM_SECRET_KEY'] = environ['THATFORUM_SECRET_KEY']
    # if 'DJANGO_CONFIGURATION' in environ:
    #     import newrelic.agent
    #     newrelic.agent.initialize('%s/newrelic/newrelic.ini' % Path(__file__).ancestor(2), environ['DJANGO_CONFIGURATION'])

    try:
        return _application(environ, start_response)
    except ImportError:
        # Remember the original sys.path
        prev_sys_path = sys.path
        # Add the project folder to path
        mp = Path(__file__).ancestor(2)
        site.addsitedir(mp)
        # Reorder sys.path so new directory is at front
        new_sys_path = []
        for item in list(sys.path):
            if item not in prev_sys_path:
                new_sys_path.append(item)
                sys.path.remove(item)
        sys.path[:0] = new_sys_path
        return _application(environ, start_response)
