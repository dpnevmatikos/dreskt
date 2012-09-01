from django.conf.urls import patterns, include, url
from django.contrib import admin
from students.api import NotificationResource

admin.autodiscover()

notification_resource = NotificationResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dreskt.views.home', name='home'),
    # url(r'^dreskt/', include('dreskt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^api/', include(notification_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
