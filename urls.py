from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^avagata/', include('avagata.foo.urls')),
	(r'^admin/', include(admin.site.urls)),
)
