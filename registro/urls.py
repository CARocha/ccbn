from django.conf.urls.defaults import *
from models import *

urlpatterns = patterns('registro.views',
	url(r'^consultar/$', 'consultar', name='consultar'),
    url(r'^chatel/$', 'filtrado_chatel', name='filtrado-chatel'),
 
)