from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:'
    # (r'^ozet/', include('ozet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^video', 'ozet.performances.views.video'),
    (r'^photos', 'ozet.performances.views.photos'),
    (r'^events/', include('ozet.performances.urls')),
    (r'^music/', include('ozet.music.urls')),
    (r'^log/', include('ozet.log.urls')),
    (r'^chv20/', include('ozet.chv20.urls')),
    # (r'^video/', include('ozet.videos.urls')),
    (r'^', include('ozet.home.urls')),
)
                  