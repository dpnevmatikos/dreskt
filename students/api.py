from tastypie.resources import ModelResource,ALL,ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from students.models import *
from datetime import datetime
from django.db.models import Q
from django.contrib import auth

class CustomAuthentication(Authentication):
    
    def is_authenticated(self, request, **kwargs):
        user_pass_header = request.META.get("HTTP_X_AUTH_TOKEN", None)
        if not user_pass_header:
            return None

        user, passwd = user_pass_header.split("|")
        user = auth.authenticate(username=user, password=passwd)
        if user and user.is_active:
            request.user = user
            return True
        
        return False
   
 
class NotificationResource(ModelResource):
    
    class Meta:
        start_date = datetime.now()
        end_date = datetime(2013,12,20)

        queryset = Notification.objects.filter(expiration_date__gte=start_date,expiration_date__lte=end_date)
        resource_name = 'notifications'
        include_resource_uri = True

    '''
    def dehydrate(self,bundle):
        #return notification text only
        return bundle.data['text']
    '''
    def alter_list_data_to_serialize(self,request,data_dict):
        print "----------------"
        #print request.META["HTTP_USER"]
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                # Get rid of the "meta".
                del(data_dict['meta'])
                # Rename the objects.
                data_dict['notifications'] = data_dict['objects']
                del(data_dict['objects'])
        return data_dict


class StudentResource(ModelResource):

    class Meta:
        list_allowed_methods = ['get']
        #authorization = Authorization()
        #authentication = CustomAuthentication()
        queryset = Student.objects.all()
        resource_name = "students"
        include_resource_uri = True
        excludes = ['password']
        filtering = { 'email' : ALL }
    
    def alter_list_data_to_serialize(self,request,data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                # Get rid of the "meta".
                del(data_dict['meta'])
                # Rename the objects.
                data_dict['students'] = data_dict['objects']
                del(data_dict['objects'])
        return data_dict


class DocumentResource(ModelResource):

    class Meta:
        queryset = Document.objects.all()
        resource_name = "documents"
        include_resource_uri = True
    
    def alter_list_data_to_serialize(self,request,data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                # Get rid of the "meta".
                del(data_dict['meta'])
                # Rename the objects.
                data_dict['documents'] = data_dict['objects']
                del(data_dict['objects'])
        return data_dict



class DocumentEnquiryResource(ModelResource):
    
    document = fields.ForeignKey(DocumentResource,"document")
    student = fields.ForeignKey(StudentResource,"student")
 
    class Meta:
        queryset = DocumentEnquiry.objects.all()
        authentication = CustomAuthentication()
        authorization = Authorization()
        resource_name = "docenquiries"
        include_resource_uri = False
        filtering = {'student' : ALL_WITH_RELATIONS} 
    
    def get_object_list(self, request):
        student = Student.objects.get(email=request.user.email)
        return super(DocumentEnquiryResource, 
                self).get_object_list(request).filter(student=student)

    def alter_list_data_to_serialize(self,request,data_dict):
        #print request.META["HTTP_USER"]
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                # Get rid of the "meta".
                del(data_dict['meta'])
                # Rename the objects.
                data_dict['docenquiries'] = data_dict['objects']
                del(data_dict['objects'])
        return data_dict


class CourseResource(ModelResource):
    
    student = fields.ToManyField(StudentResource,"student")

    class Meta:
        queryset = Course.objects.all()
        authentication = CustomAuthentication()
        authorization = Authorization()
        resource_name = "courses"
        include_resource_uri = False
        filtering = {'student' : ALL_WITH_RELATIONS}
        excludes = ['students']
    
    def get_object_list(self, request):
        student = Student.objects.get(email=request.user.email)
        return super(CourseResource, 
                self).get_object_list(request).filter(students__email=student.email)

    def alter_list_data_to_serialize(self,request,data_dict):
        #print request.META["HTTP_USER"]
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                # Get rid of the "meta".
                del(data_dict['meta'])
                # Rename the objects.
                data_dict['courses'] = data_dict['objects']
                del(data_dict['objects'])
        return data_dict

