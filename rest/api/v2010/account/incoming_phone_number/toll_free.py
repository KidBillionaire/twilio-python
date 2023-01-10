"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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





class TollFreeInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str):
        super(TollFreeInstance, self).__init__(version)
        self._properties = { 
            'account_sid' = payload.get('account_sid'),
            'address_sid' = payload.get('address_sid'),
            'address_requirements' = payload.get('address_requirements'),
            'api_version' = payload.get('api_version'),
            'beta' = payload.get('beta'),
            'capabilities' = payload.get('capabilities'),
            'date_created' = payload.get('date_created'),
            'date_updated' = payload.get('date_updated'),
            'friendly_name' = payload.get('friendly_name'),
            'identity_sid' = payload.get('identity_sid'),
            'phone_number' = payload.get('phone_number'),
            'origin' = payload.get('origin'),
            'sid' = payload.get('sid'),
            'sms_application_sid' = payload.get('sms_application_sid'),
            'sms_fallback_method' = payload.get('sms_fallback_method'),
            'sms_fallback_url' = payload.get('sms_fallback_url'),
            'sms_method' = payload.get('sms_method'),
            'sms_url' = payload.get('sms_url'),
            'status_callback' = payload.get('status_callback'),
            'status_callback_method' = payload.get('status_callback_method'),
            'trunk_sid' = payload.get('trunk_sid'),
            'uri' = payload.get('uri'),
            'voice_receive_mode' = payload.get('voice_receive_mode'),
            'voice_application_sid' = payload.get('voice_application_sid'),
            'voice_caller_id_lookup' = payload.get('voice_caller_id_lookup'),
            'voice_fallback_method' = payload.get('voice_fallback_method'),
            'voice_fallback_url' = payload.get('voice_fallback_url'),
            'voice_method' = payload.get('voice_method'),
            'voice_url' = payload.get('voice_url'),
            'emergency_status' = payload.get('emergency_status'),
            'emergency_address_sid' = payload.get('emergency_address_sid'),
            'emergency_address_status' = payload.get('emergency_address_status'),
            'bundle_sid' = payload.get('bundle_sid'),
            'status' = payload.get('status'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = TollFreeContext(
                self._version,
                account_sid=self._solution['account_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.TollFreeInstance {}>'.format(context)



class TollFreeListInstance(ListResource):
    def __init__(self, version: V2010, account_sid: str):
        # TODO: needs autogenerated docs
        super(TollFreeListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = { account_sid,  }
        self._uri = '/Accounts/${account_sid}/IncomingPhoneNumbers/TollFree.json'
        
        
        def create(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.create(method='post', uri=self._uri, data=data, )

            return TollFreeInstance(self._version, payload, account_sid=self._solution['account_sid'])
            
        
        def page(self, beta, friendly_name, phone_number, origin, page_size):
            
            data = values.of({
                'beta': beta,'friendly_name': friendly_name,'phone_number': phone_number,'origin': origin,'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return TollFreePage(self._version, payload, account_sid=self._solution['account_sid'])
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.TollFreeListInstance>'

