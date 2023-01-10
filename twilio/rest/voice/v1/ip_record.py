"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Voice
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource

from twilio.base.page import Page




class IpRecordContext(InstanceContext):
    def __init__(self, version: V1, sid: str):
        # TODO: needs autogenerated docs
        super(IpRecordContextList, self).__init__(version)

        # Path Solution
        self._solution = { sid,  }
        self._uri = '/IpRecords/${sid}'
        
        
        def delete(self):
            
            
            """
            Deletes the IpRecordInstance

            :returns: True if delete succeeds, False otherwise
            :rtype: bool
            """
            return self._version.delete(method='DELETE', uri=self._uri, )
        
        def fetch(self):
            
            """
            Fetch the IpRecordInstance

            :returns: The fetched IpRecordInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return IpRecordInstance(
                self._version,
                payload,
                sid=self._solution['sid'],
            )
            
            
        
        def update(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.update(method='post', uri=self._uri, data=data, )

            return IpRecordInstance(self._version, payload, sid=self._solution['sid'], )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.IpRecordContext>'



class IpRecordInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super(IpRecordInstance, self).__init__(version)
        self._properties = { 
            'account_sid' = payload.get('account_sid'),
            'sid' = payload.get('sid'),
            'friendly_name' = payload.get('friendly_name'),
            'ip_address' = payload.get('ip_address'),
            'cidr_prefix_length' = payload.get('cidr_prefix_length'),
            'date_created' = payload.get('date_created'),
            'date_updated' = payload.get('date_updated'),
            'url' = payload.get('url'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = IpRecordContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.IpRecordInstance {}>'.format(context)



class IpRecordListInstance(ListResource):
    def __init__(self, version: V1):
        # TODO: needs autogenerated docs
        super(IpRecordListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/IpRecords'
        
        
        def create(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.create(method='post', uri=self._uri, data=data, )

            return IpRecordInstance(self._version, payload, )
            
        
        def page(self, page_size):
            
            data = values.of({
                'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return IpRecordPage(self._version, payload, )
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.IpRecordListInstance>'

