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


class BrandRegistrationList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version):
        """
        Initialize the BrandRegistrationList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.messaging.v1.brand_registration.BrandRegistrationList
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationList
        """
        super(BrandRegistrationList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/a2p/BrandRegistrations'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams BrandRegistrationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists BrandRegistrationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of BrandRegistrationInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return BrandRegistrationPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of BrandRegistrationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return BrandRegistrationPage(self._version, response, self._solution)

    def create(self, customer_profile_bundle_sid, a2p_profile_bundle_sid,
               brand_type=values.unset, mock=values.unset,
               skip_automatic_sec_vet=values.unset):
        """
        Create the BrandRegistrationInstance

        :param unicode customer_profile_bundle_sid: Customer Profile Bundle Sid
        :param unicode a2p_profile_bundle_sid: A2P Messaging Profile Bundle Sid
        :param unicode brand_type: Type of brand being created. One of: "STANDARD", "STARTER".
        :param bool mock: A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.
        :param bool skip_automatic_sec_vet: Skip Automatic Secondary Vetting

        :returns: The created BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """
        data = values.of({
            'CustomerProfileBundleSid': customer_profile_bundle_sid,
            'A2PProfileBundleSid': a2p_profile_bundle_sid,
            'BrandType': brand_type,
            'Mock': mock,
            'SkipAutomaticSecVet': skip_automatic_sec_vet,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return BrandRegistrationInstance(self._version, payload, )

    def get(self, sid):
        """
        Constructs a BrandRegistrationContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.messaging.v1.brand_registration.BrandRegistrationContext
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationContext
        """
        return BrandRegistrationContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a BrandRegistrationContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.messaging.v1.brand_registration.BrandRegistrationContext
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationContext
        """
        return BrandRegistrationContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.BrandRegistrationList>'


class BrandRegistrationPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the BrandRegistrationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.messaging.v1.brand_registration.BrandRegistrationPage
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationPage
        """
        super(BrandRegistrationPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of BrandRegistrationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """
        return BrandRegistrationInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.BrandRegistrationPage>'


class BrandRegistrationContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, sid):
        """
        Initialize the BrandRegistrationContext

        :param Version version: Version that contains the resource
        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.messaging.v1.brand_registration.BrandRegistrationContext
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationContext
        """
        super(BrandRegistrationContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/a2p/BrandRegistrations/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the BrandRegistrationInstance

        :returns: The fetched BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return BrandRegistrationInstance(self._version, payload, sid=self._solution['sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.BrandRegistrationContext {}>'.format(context)


class BrandRegistrationInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class Status(object):
        PENDING = "PENDING"
        APPROVED = "APPROVED"
        FAILED = "FAILED"

    class IdentityStatus(object):
        SELF_DECLARED = "SELF_DECLARED"
        UNVERIFIED = "UNVERIFIED"
        VERIFIED = "VERIFIED"
        VETTED_VERIFIED = "VETTED_VERIFIED"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the BrandRegistrationInstance

        :returns: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """
        super(BrandRegistrationInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'customer_profile_bundle_sid': payload.get('customer_profile_bundle_sid'),
            'a2p_profile_bundle_sid': payload.get('a2p_profile_bundle_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'brand_type': payload.get('brand_type'),
            'status': payload.get('status'),
            'tcr_id': payload.get('tcr_id'),
            'failure_reason': payload.get('failure_reason'),
            'url': payload.get('url'),
            'brand_score': deserialize.integer(payload.get('brand_score')),
            'identity_status': payload.get('identity_status'),
            'russell_3000': payload.get('russell_3000'),
            'tax_exempt_status': payload.get('tax_exempt_status'),
            'skip_automatic_sec_vet': payload.get('skip_automatic_sec_vet'),
            'mock': payload.get('mock'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: BrandRegistrationContext for this BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationContext
        """
        if self._context is None:
            self._context = BrandRegistrationContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: A2P BrandRegistration Sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def customer_profile_bundle_sid(self):
        """
        :returns: A2P Messaging Profile Bundle BundleSid
        :rtype: unicode
        """
        return self._properties['customer_profile_bundle_sid']

    @property
    def a2p_profile_bundle_sid(self):
        """
        :returns: A2P Messaging Profile Bundle BundleSid
        :rtype: unicode
        """
        return self._properties['a2p_profile_bundle_sid']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def brand_type(self):
        """
        :returns: Type of brand. One of: "STANDARD", "STARTER".
        :rtype: unicode
        """
        return self._properties['brand_type']

    @property
    def status(self):
        """
        :returns: Brand Registration status
        :rtype: BrandRegistrationInstance.Status
        """
        return self._properties['status']

    @property
    def tcr_id(self):
        """
        :returns: Campaign Registry (TCR) Brand ID
        :rtype: unicode
        """
        return self._properties['tcr_id']

    @property
    def failure_reason(self):
        """
        :returns: A reason why brand registration has failed
        :rtype: unicode
        """
        return self._properties['failure_reason']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Brand Registration
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def brand_score(self):
        """
        :returns: Brand score
        :rtype: unicode
        """
        return self._properties['brand_score']

    @property
    def identity_status(self):
        """
        :returns: Identity Status
        :rtype: BrandRegistrationInstance.IdentityStatus
        """
        return self._properties['identity_status']

    @property
    def russell_3000(self):
        """
        :returns: Russell 3000
        :rtype: bool
        """
        return self._properties['russell_3000']

    @property
    def tax_exempt_status(self):
        """
        :returns: Tax Exempt Status
        :rtype: unicode
        """
        return self._properties['tax_exempt_status']

    @property
    def skip_automatic_sec_vet(self):
        """
        :returns: Skip Automatic Secondary Vetting
        :rtype: bool
        """
        return self._properties['skip_automatic_sec_vet']

    @property
    def mock(self):
        """
        :returns: A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.
        :rtype: bool
        """
        return self._properties['mock']

    def fetch(self):
        """
        Fetch the BrandRegistrationInstance

        :returns: The fetched BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.BrandRegistrationInstance {}>'.format(context)
