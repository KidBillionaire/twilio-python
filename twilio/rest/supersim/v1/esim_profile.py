r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Supersim
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class EsimProfileList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the EsimProfileList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.supersim.v1.esim_profile.EsimProfileList
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/ESimProfiles".format(**self._solution)

    def create(
        self,
        callback_url=values.unset,
        callback_method=values.unset,
        generate_matching_id=values.unset,
        eid=values.unset,
    ):
        """
        Create the EsimProfileInstance

        :param str callback_url: The URL we should call using the `callback_method` when the status of the eSIM Profile changes. At this stage of the eSIM Profile pilot, the a request to the URL will only be called when the ESimProfile resource changes from `reserving` to `available`.
        :param str callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
        :param bool generate_matching_id: When set to `true`, a value for `Eid` does not need to be provided. Instead, when the eSIM profile is reserved, a matching ID will be generated and returned via the `matching_id` property. This identifies the specific eSIM profile that can be used by any capable device to claim and download the profile.
        :param str eid: Identifier of the eUICC that will claim the eSIM Profile.

        :returns: The created EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        """
        data = values.of(
            {
                "CallbackUrl": callback_url,
                "CallbackMethod": callback_method,
                "GenerateMatchingId": generate_matching_id,
                "Eid": eid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return EsimProfileInstance(self._version, payload)

    async def create_async(
        self,
        callback_url=values.unset,
        callback_method=values.unset,
        generate_matching_id=values.unset,
        eid=values.unset,
    ):
        """
        Asynchronously create the EsimProfileInstance

        :param str callback_url: The URL we should call using the `callback_method` when the status of the eSIM Profile changes. At this stage of the eSIM Profile pilot, the a request to the URL will only be called when the ESimProfile resource changes from `reserving` to `available`.
        :param str callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
        :param bool generate_matching_id: When set to `true`, a value for `Eid` does not need to be provided. Instead, when the eSIM profile is reserved, a matching ID will be generated and returned via the `matching_id` property. This identifies the specific eSIM profile that can be used by any capable device to claim and download the profile.
        :param str eid: Identifier of the eUICC that will claim the eSIM Profile.

        :returns: The created EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        """
        data = values.of(
            {
                "CallbackUrl": callback_url,
                "CallbackMethod": callback_method,
                "GenerateMatchingId": generate_matching_id,
                "Eid": eid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return EsimProfileInstance(self._version, payload)

    def stream(
        self,
        eid=values.unset,
        sim_sid=values.unset,
        status=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Streams EsimProfileInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str eid: List the eSIM Profiles that have been associated with an EId.
        :param str sim_sid: Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/wireless/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records.
        :param EsimProfileInstance.Status status: List the eSIM Profiles that are in a given status.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.esim_profile.EsimProfileInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            eid=eid, sim_sid=sim_sid, status=status, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        eid=values.unset,
        sim_sid=values.unset,
        status=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously streams EsimProfileInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str eid: List the eSIM Profiles that have been associated with an EId.
        :param str sim_sid: Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/wireless/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records.
        :param EsimProfileInstance.Status status: List the eSIM Profiles that are in a given status.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.esim_profile.EsimProfileInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            eid=eid, sim_sid=sim_sid, status=status, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        eid=values.unset,
        sim_sid=values.unset,
        status=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Lists EsimProfileInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str eid: List the eSIM Profiles that have been associated with an EId.
        :param str sim_sid: Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/wireless/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records.
        :param EsimProfileInstance.Status status: List the eSIM Profiles that are in a given status.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.esim_profile.EsimProfileInstance]
        """
        return list(
            self.stream(
                eid=eid,
                sim_sid=sim_sid,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        eid=values.unset,
        sim_sid=values.unset,
        status=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously lists EsimProfileInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str eid: List the eSIM Profiles that have been associated with an EId.
        :param str sim_sid: Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/wireless/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records.
        :param EsimProfileInstance.Status status: List the eSIM Profiles that are in a given status.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.esim_profile.EsimProfileInstance]
        """
        return list(
            await self.stream_async(
                eid=eid,
                sim_sid=sim_sid,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        eid=values.unset,
        sim_sid=values.unset,
        status=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of EsimProfileInstance records from the API.
        Request is executed immediately

        :param str eid: List the eSIM Profiles that have been associated with an EId.
        :param str sim_sid: Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/wireless/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records.
        :param EsimProfileInstance.Status status: List the eSIM Profiles that are in a given status.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfilePage
        """
        data = values.of(
            {
                "Eid": eid,
                "SimSid": sim_sid,
                "Status": status,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return EsimProfilePage(self._version, response, self._solution)

    async def page_async(
        self,
        eid=values.unset,
        sim_sid=values.unset,
        status=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of EsimProfileInstance records from the API.
        Request is executed immediately

        :param str eid: List the eSIM Profiles that have been associated with an EId.
        :param str sim_sid: Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/wireless/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records.
        :param EsimProfileInstance.Status status: List the eSIM Profiles that are in a given status.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfilePage
        """
        data = values.of(
            {
                "Eid": eid,
                "SimSid": sim_sid,
                "Status": status,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return EsimProfilePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of EsimProfileInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfilePage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return EsimProfilePage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of EsimProfileInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfilePage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return EsimProfilePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a EsimProfileContext

        :param sid: The SID of the eSIM Profile resource to fetch.

        :returns: twilio.rest.supersim.v1.esim_profile.EsimProfileContext
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileContext
        """
        return EsimProfileContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a EsimProfileContext

        :param sid: The SID of the eSIM Profile resource to fetch.

        :returns: twilio.rest.supersim.v1.esim_profile.EsimProfileContext
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileContext
        """
        return EsimProfileContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Supersim.V1.EsimProfileList>"


class EsimProfilePage(Page):
    def get_instance(self, payload):
        """
        Build an instance of EsimProfileInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        """
        return EsimProfileInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.EsimProfilePage>"


class EsimProfileInstance(InstanceResource):
    class Status(object):
        NEW = "new"
        RESERVING = "reserving"
        AVAILABLE = "available"
        DOWNLOADED = "downloaded"
        INSTALLED = "installed"
        FAILED = "failed"

    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the EsimProfileInstance

        :returns: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "iccid": payload.get("iccid"),
            "sim_sid": payload.get("sim_sid"),
            "status": payload.get("status"),
            "eid": payload.get("eid"),
            "smdp_plus_address": payload.get("smdp_plus_address"),
            "matching_id": payload.get("matching_id"),
            "activation_code": payload.get("activation_code"),
            "error_code": payload.get("error_code"),
            "error_message": payload.get("error_message"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "url": payload.get("url"),
        }

        self._context = None
        self._solution = {
            "sid": sid or self._properties["sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: EsimProfileContext for this EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileContext
        """
        if self._context is None:
            self._context = EsimProfileContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the eSIM Profile resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) to which the eSIM Profile resource belongs.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def iccid(self):
        """
        :returns: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with the Sim resource.
        :rtype: str
        """
        return self._properties["iccid"]

    @property
    def sim_sid(self):
        """
        :returns: The SID of the [Sim](https://www.twilio.com/docs/wireless/api/sim-resource) resource that this eSIM Profile controls.
        :rtype: str
        """
        return self._properties["sim_sid"]

    @property
    def status(self):
        """
        :returns:
        :rtype: EsimProfileInstance.Status
        """
        return self._properties["status"]

    @property
    def eid(self):
        """
        :returns: Identifier of the eUICC that can claim the eSIM Profile.
        :rtype: str
        """
        return self._properties["eid"]

    @property
    def smdp_plus_address(self):
        """
        :returns: Address of the SM-DP+ server from which the Profile will be downloaded. The URL will appear once the eSIM Profile reaches the status `available`.
        :rtype: str
        """
        return self._properties["smdp_plus_address"]

    @property
    def matching_id(self):
        """
        :returns: Unique identifier of the eSIM profile that can be used to identify and download the eSIM profile from the SM-DP+ server. Populated if `generate_matching_id` is set to `true` when creating the eSIM profile reservation.
        :rtype: str
        """
        return self._properties["matching_id"]

    @property
    def activation_code(self):
        """
        :returns: Combined machine-readable activation code for acquiring an eSIM Profile with the Activation Code download method. Can be used in a QR code to download an eSIM profile.
        :rtype: str
        """
        return self._properties["activation_code"]

    @property
    def error_code(self):
        """
        :returns: Code indicating the failure if the download of the SIM Profile failed and the eSIM Profile is in `failed` state.
        :rtype: str
        """
        return self._properties["error_code"]

    @property
    def error_message(self):
        """
        :returns: Error message describing the failure if the download of the SIM Profile failed and the eSIM Profile is in `failed` state.
        :rtype: str
        """
        return self._properties["error_message"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the eSIM Profile resource.
        :rtype: str
        """
        return self._properties["url"]

    def fetch(self):
        """
        Fetch the EsimProfileInstance


        :returns: The fetched EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the EsimProfileInstance


        :returns: The fetched EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.EsimProfileInstance {}>".format(context)


class EsimProfileContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the EsimProfileContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the eSIM Profile resource to fetch.

        :returns: twilio.rest.supersim.v1.esim_profile.EsimProfileContext
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/ESimProfiles/{sid}".format(**self._solution)

    def fetch(self):
        """
        Fetch the EsimProfileInstance


        :returns: The fetched EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return EsimProfileInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the EsimProfileInstance


        :returns: The fetched EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return EsimProfileInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.EsimProfileContext {}>".format(context)
