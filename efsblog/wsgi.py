import os
import sys

path ='home/pythonanywhereluoshuitaotao/efsblog.settings'
if path not in sys.path:
    sys.path.append(path)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "efsblog.settings")

application = get_wsgi_application()
