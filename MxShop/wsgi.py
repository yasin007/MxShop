# 作为你的项目的运行在 WSGI 兼容的Web服务器上的入口

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

application = get_wsgi_application()
