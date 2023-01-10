"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Pricing
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




class NumberContext(InstanceContext):
    def __init__(self, version: V2, destination_number: str):
        # TODO: needs autogenerated docs
        super(NumberContextList, self).__init__(version)

        # Path Solution
        self._solution = { destination_number,  }
        self._uri = '/Trunking/Numbers/${destination_number}'
        
        
        def fetch(self, origination_number):
            
            """
            Fetch the NumberInstance

            :returns: The fetched NumberInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return NumberInstance(
                self._version,
                payload,
                destination_number=self._solution['destination_number'],
            )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.NumberContext>'



class NumberInstance(InstanceResource):
    def __init__(self, version, payload, destination_number: str):
        super(NumberInstance, self).__init__(version)
        self._properties = { 
            'destination_number' = payload.get('destination_number'),
            'origination_number' = payload.get('origination_number'),
            'country' = payload.get('country'),
            'iso_country' = payload.get('iso_country'),
            'terminating_prefix_prices' = payload.get('terminating_prefix_prices'),
            'originating_call_price' = payload.get('originating_call_price'),
            'price_unit' = payload.get('price_unit'),
            'url' = payload.get('url'),
        }

        self._context = None
        self._solution = {
            'destination_number': destination_number or self._properties['destination_number']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = NumberContext(
                self._version,
                destination_number=self._solution['destination_number'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2.NumberInstance {}>'.format(context)



class NumberListInstance(ListResource):
    def __init__(self, version: V2):
        # TODO: needs autogenerated docs
        super(NumberListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = ''
        
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.NumberListInstance>'

