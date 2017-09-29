import os
import sys

path ='/home/jingcui/efsblog'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTING_MODULE'] = 'efsblog.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
