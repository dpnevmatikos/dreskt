from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from students.api import *

admin.autodiscover()

v1_api = Api(api_name='dreskt')
v1_api.register(NotificationResource())
v1_api.register(DocumentResource())
v1_api.register(DocumentEnquiryResource())
v1_api.register(StudentResource())
v1_api.register(CourseResource())

notification_resource = NotificationResource()
document_enquiries_resource = DocumentEnquiryResource()
documents_resource = DocumentResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dreskt.views.home', name='home'),
    # url(r'^dreskt/', include('dreskt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^api/', include(notification_resource.urls)),
    #url(r'^api/', include(document_enquiries_resource.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^students/(?P<student_id>\d+)/$', 'students.views.detail'),

)
