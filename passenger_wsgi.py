#!/usr/bin/env python
import os
import sys

BASE_APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(os.path.join(BASE_APP_DIR, 'src/'))
sys.path.append(os.path.join(BASE_APP_DIR, 'venv/lib/python3.4/site-packages'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()