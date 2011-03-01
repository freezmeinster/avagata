from django.conf.urls.defaults import *
from django.contrib import admin
import os.path

admin.autodiscover()
asset = os.path.join(os.path.dirname(__file__),'asset')

urlpatterns = patterns('',
    # Example:
    # (r'^avagata/', include('avagata.foo.urls')),
	(r'^admin/', include(admin.site.urls)),
	(r'^asset/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': asset}),

)
