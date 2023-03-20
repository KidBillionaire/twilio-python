r"""
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


from typing import Optional
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.api.v2010.account.available_phone_number_country.local import LocalList
from twilio.rest.api.v2010.account.available_phone_number_country.machine_to_machine import (
    MachineToMachineList,
)
from twilio.rest.api.v2010.account.available_phone_number_country.mobile import (
    MobileList,
)
from twilio.rest.api.v2010.account.available_phone_number_country.national import (
    NationalList,
)
from twilio.rest.api.v2010.account.available_phone_number_country.shared_cost import (
    SharedCostList,
)
from twilio.rest.api.v2010.account.available_phone_number_country.toll_free import (
    TollFreeList,
)
from twilio.rest.api.v2010.account.available_phone_number_country.voip import VoipList


class AvailablePhoneNumberCountryList(ListResource):
    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the AvailablePhoneNumberCountryList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the available phone number Country resources.

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryList
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/AvailablePhoneNumbers.json".format(
            **self._solution
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams AvailablePhoneNumberCountryInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams AvailablePhoneNumberCountryInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists AvailablePhoneNumberCountryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists AvailablePhoneNumberCountryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryInstance]
        """
        return list(
            await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Retrieve a single page of AvailablePhoneNumberCountryInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AvailablePhoneNumberCountryPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of AvailablePhoneNumberCountryInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return AvailablePhoneNumberCountryPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AvailablePhoneNumberCountryInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AvailablePhoneNumberCountryPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of AvailablePhoneNumberCountryInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AvailablePhoneNumberCountryPage(self._version, response, self._solution)

    def get(self, country_code):
        """
        Constructs a AvailablePhoneNumberCountryContext

        :param country_code: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country to fetch available phone number information about.

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryContext
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryContext
        """
        return AvailablePhoneNumberCountryContext(
            self._version,
            account_sid=self._solution["account_sid"],
            country_code=country_code,
        )

    def __call__(self, country_code):
        """
        Constructs a AvailablePhoneNumberCountryContext

        :param country_code: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country to fetch available phone number information about.

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryContext
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryContext
        """
        return AvailablePhoneNumberCountryContext(
            self._version,
            account_sid=self._solution["account_sid"],
            country_code=country_code,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Api.V2010.AvailablePhoneNumberCountryList>"


class AvailablePhoneNumberCountryPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of AvailablePhoneNumberCountryInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryInstance
        """
        return AvailablePhoneNumberCountryInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.AvailablePhoneNumberCountryPage>"


class AvailablePhoneNumberCountryInstance(InstanceResource):
    def __init__(
        self, version, payload, account_sid: str, country_code: Optional[str] = None
    ):
        """
        Initialize the AvailablePhoneNumberCountryInstance

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryInstance
        """
        super().__init__(version)

        self._properties = {
            "country_code": payload.get("country_code"),
            "country": payload.get("country"),
            "uri": payload.get("uri"),
            "beta": payload.get("beta"),
            "subresource_uris": payload.get("subresource_uris"),
        }

        self._context = None
        self._solution = {
            "account_sid": account_sid,
            "country_code": country_code or self._properties["country_code"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AvailablePhoneNumberCountryContext for this AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryContext
        """
        if self._context is None:
            self._context = AvailablePhoneNumberCountryContext(
                self._version,
                account_sid=self._solution["account_sid"],
                country_code=self._solution["country_code"],
            )
        return self._context

    @property
    def country_code(self):
        """
        :returns: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country.
        :rtype: str
        """
        return self._properties["country_code"]

    @property
    def country(self):
        """
        :returns: The name of the country.
        :rtype: str
        """
        return self._properties["country"]

    @property
    def uri(self):
        """
        :returns: The URI of the Country resource, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties["uri"]

    @property
    def beta(self):
        """
        :returns: Whether all phone numbers available in the country are new to the Twilio platform. `true` if they are and `false` if all numbers are not in the Twilio Phone Number Beta program.
        :rtype: bool
        """
        return self._properties["beta"]

    @property
    def subresource_uris(self):
        """
        :returns: A list of related AvailablePhoneNumber resources identified by their URIs relative to `https://api.twilio.com`.
        :rtype: dict
        """
        return self._properties["subresource_uris"]

    def fetch(self):
        """
        Fetch the AvailablePhoneNumberCountryInstance


        :returns: The fetched AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AvailablePhoneNumberCountryInstance


        :returns: The fetched AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryInstance
        """
        return await self._proxy.fetch_async()

    @property
    def local(self):
        """
        Access the local

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.LocalList
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.LocalList
        """
        return self._proxy.local

    @property
    def machine_to_machine(self):
        """
        Access the machine_to_machine

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.MachineToMachineList
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.MachineToMachineList
        """
        return self._proxy.machine_to_machine

    @property
    def mobile(self):
        """
        Access the mobile

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.MobileList
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.MobileList
        """
        return self._proxy.mobile

    @property
    def national(self):
        """
        Access the national

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.NationalList
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.NationalList
        """
        return self._proxy.national

    @property
    def shared_cost(self):
        """
        Access the shared_cost

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.SharedCostList
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.SharedCostList
        """
        return self._proxy.shared_cost

    @property
    def toll_free(self):
        """
        Access the toll_free

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.TollFreeList
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.TollFreeList
        """
        return self._proxy.toll_free

    @property
    def voip(self):
        """
        Access the voip

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.VoipList
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.VoipList
        """
        return self._proxy.voip

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AvailablePhoneNumberCountryInstance {}>".format(
            context
        )


class AvailablePhoneNumberCountryContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, country_code: str):
        """
        Initialize the AvailablePhoneNumberCountryContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the available phone number Country resource.
        :param country_code: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country to fetch available phone number information about.

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryContext
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "country_code": country_code,
        }
        self._uri = (
            "/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}.json".format(
                **self._solution
            )
        )

        self._local = None
        self._machine_to_machine = None
        self._mobile = None
        self._national = None
        self._shared_cost = None
        self._toll_free = None
        self._voip = None

    def fetch(self):
        """
        Fetch the AvailablePhoneNumberCountryInstance


        :returns: The fetched AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AvailablePhoneNumberCountryInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            country_code=self._solution["country_code"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AvailablePhoneNumberCountryInstance


        :returns: The fetched AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.AvailablePhoneNumberCountryInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AvailablePhoneNumberCountryInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            country_code=self._solution["country_code"],
        )

    @property
    def local(self):
        """
        Access the local

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.LocalList
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.LocalList
        """
        if self._local is None:
            self._local = LocalList(
                self._version,
                self._solution["account_sid"],
                self._solution["country_code"],
            )
        return self._local

    @property
    def machine_to_machine(self):
        """
        Access the machine_to_machine

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.MachineToMachineList
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.MachineToMachineList
        """
        if self._machine_to_machine is None:
            self._machine_to_machine = MachineToMachineList(
                self._version,
                self._solution["account_sid"],
                self._solution["country_code"],
            )
        return self._machine_to_machine

    @property
    def mobile(self):
        """
        Access the mobile

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.MobileList
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.MobileList
        """
        if self._mobile is None:
            self._mobile = MobileList(
                self._version,
                self._solution["account_sid"],
                self._solution["country_code"],
            )
        return self._mobile

    @property
    def national(self):
        """
        Access the national

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.NationalList
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.NationalList
        """
        if self._national is None:
            self._national = NationalList(
                self._version,
                self._solution["account_sid"],
                self._solution["country_code"],
            )
        return self._national

    @property
    def shared_cost(self):
        """
        Access the shared_cost

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.SharedCostList
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.SharedCostList
        """
        if self._shared_cost is None:
            self._shared_cost = SharedCostList(
                self._version,
                self._solution["account_sid"],
                self._solution["country_code"],
            )
        return self._shared_cost

    @property
    def toll_free(self):
        """
        Access the toll_free

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.TollFreeList
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.TollFreeList
        """
        if self._toll_free is None:
            self._toll_free = TollFreeList(
                self._version,
                self._solution["account_sid"],
                self._solution["country_code"],
            )
        return self._toll_free

    @property
    def voip(self):
        """
        Access the voip

        :returns: twilio.rest.api.v2010.account.available_phone_number_country.VoipList
        :rtype: twilio.rest.api.v2010.account.available_phone_number_country.VoipList
        """
        if self._voip is None:
            self._voip = VoipList(
                self._version,
                self._solution["account_sid"],
                self._solution["country_code"],
            )
        return self._voip

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AvailablePhoneNumberCountryContext {}>".format(
            context
        )
