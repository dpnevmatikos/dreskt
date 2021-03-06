from django.contrib import admin
from students.models import *


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('subject','text','date_created','expiration_date')
    list_filter = ['date_created','expiration_date']
    search_fields = ['text','subject']


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','address','city','zipcode','email')
    list_filter = ['name','city','ethnicity']
    search_fields = ['name','email']


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('code','description')
    list_filter = ['code']
    search_fields = ['code','description']


class DocumentEnquiryAdmin(admin.ModelAdmin):
    list_display = ('document','student','status')
    list_filter = ['status']
    search_fields = ['student']


admin.site.register(Notification,NotificationAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Course)
admin.site.register(Ethnicity)
#admin.site.register(Notification)
admin.site.register(Grade)
admin.site.register(Document,DocumentAdmin)
admin.site.register(DocumentEnquiry,DocumentEnquiryAdmin)

