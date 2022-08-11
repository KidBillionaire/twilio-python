# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class PhoneNumberList(ListResource):

    def __init__(self, version):
        """
        Initialize the PhoneNumberList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.routes.v2.phone_number.PhoneNumberList
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberList
        """
        super(PhoneNumberList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self, phone_number):
        """
        Constructs a PhoneNumberContext

        :param phone_number: The phone number

        :returns: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, phone_number=phone_number, )

    def __call__(self, phone_number):
        """
        Constructs a PhoneNumberContext

        :param phone_number: The phone number

        :returns: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, phone_number=phone_number, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Routes.V2.PhoneNumberList>'


class PhoneNumberPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the PhoneNumberPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.routes.v2.phone_number.PhoneNumberPage
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberPage
        """
        super(PhoneNumberPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of PhoneNumberInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.routes.v2.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberInstance
        """
        return PhoneNumberInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Routes.V2.PhoneNumberPage>'


class PhoneNumberContext(InstanceContext):

    def __init__(self, version, phone_number):
        """
        Initialize the PhoneNumberContext

        :param Version version: Version that contains the resource
        :param phone_number: The phone number

        :returns: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        """
        super(PhoneNumberContext, self).__init__(version)

        # Path Solution
        self._solution = {'phone_number': phone_number, }
        self._uri = '/PhoneNumbers/{phone_number}'.format(**self._solution)

    def create(self, voice_region=values.unset, friendly_name=values.unset):
        """
        Create the PhoneNumberInstance

        :param unicode voice_region: The Inbound Processing Region used for this phone number for voice
        :param unicode friendly_name: A human readable description of this resource.

        :returns: The created PhoneNumberInstance
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberInstance
        """
        data = values.of({'VoiceRegion': voice_region, 'FriendlyName': friendly_name, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return PhoneNumberInstance(self._version, payload, phone_number=self._solution['phone_number'], )

    def update(self, voice_region, friendly_name):
        """
        Update the PhoneNumberInstance

        :param unicode voice_region: The Inbound Processing Region used for this phone number for voice
        :param unicode friendly_name: A human readable description of this resource.

        :returns: The updated PhoneNumberInstance
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberInstance
        """
        data = values.of({'VoiceRegion': voice_region, 'FriendlyName': friendly_name, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return PhoneNumberInstance(self._version, payload, phone_number=self._solution['phone_number'], )

    def fetch(self):
        """
        Fetch the PhoneNumberInstance

        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return PhoneNumberInstance(self._version, payload, phone_number=self._solution['phone_number'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Routes.V2.PhoneNumberContext {}>'.format(context)


class PhoneNumberInstance(InstanceResource):

    def __init__(self, version, payload, phone_number=None):
        """
        Initialize the PhoneNumberInstance

        :returns: twilio.rest.routes.v2.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberInstance
        """
        super(PhoneNumberInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'phone_number': payload.get('phone_number'),
            'url': payload.get('url'),
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'voice_region': payload.get('voice_region'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
        }

        # Context
        self._context = None
        self._solution = {'phone_number': phone_number or self._properties['phone_number'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: PhoneNumberContext for this PhoneNumberInstance
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        """
        if self._context is None:
            self._context = PhoneNumberContext(self._version, phone_number=self._solution['phone_number'], )
        return self._context

    @property
    def phone_number(self):
        """
        :returns: The phone number
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies the Inbound Processing Region assignments for this phone number.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description of the Inbound Processing Region assignments for this phone number.
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def voice_region(self):
        """
        :returns: The Inbound Processing Region used for this phone number for voice.
        :rtype: unicode
        """
        return self._properties['voice_region']

    @property
    def date_created(self):
        """
        :returns: The date that this phone number was assigned an Inbound Processing Region.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date that the Inbound Processing Region was updated for this phone number.
        :rtype: datetime
        """
        return self._properties['date_updated']

    def create(self, voice_region=values.unset, friendly_name=values.unset):
        """
        Create the PhoneNumberInstance

        :param unicode voice_region: The Inbound Processing Region used for this phone number for voice
        :param unicode friendly_name: A human readable description of this resource.

        :returns: The created PhoneNumberInstance
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberInstance
        """
        return self._proxy.create(voice_region=voice_region, friendly_name=friendly_name, )

    def update(self, voice_region, friendly_name):
        """
        Update the PhoneNumberInstance

        :param unicode voice_region: The Inbound Processing Region used for this phone number for voice
        :param unicode friendly_name: A human readable description of this resource.

        :returns: The updated PhoneNumberInstance
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberInstance
        """
        return self._proxy.update(voice_region, friendly_name, )

    def fetch(self):
        """
        Fetch the PhoneNumberInstance

        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Routes.V2.PhoneNumberInstance {}>'.format(context)