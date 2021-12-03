import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()

application = WhiteNoise(application, root='/web/sac_fashion')
application.add_files('/web/sac_fashion/static/', prefix='')
application.add_files('/web/sac_fashion/images/', prefix='')
application.add_files('/web/sac_fashion/videos/', prefix='')