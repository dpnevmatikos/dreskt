from tastypie.resources import ModelResource
from students.models import *
from datetime import datetime
from django.db.models import Q

class NotificationResource(ModelResource):
    
    class Meta:
        start_date = datetime.now()
        end_date = datetime(2013,12,20)

        queryset = Notification.objects.filter(Q(expiration_date__gte=start_date),Q(expiration_date__lte=end_date))
        resource_name = 'notifications'
        include_resource_uri = False

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
