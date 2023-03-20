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
from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.api.v2010.account.address.dependent_phone_number import (
    DependentPhoneNumberList,
)


class AddressList(ListResource):
    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the AddressList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to read.

        :returns: twilio.rest.api.v2010.account.address.AddressList
        :rtype: twilio.rest.api.v2010.account.address.AddressList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/Addresses.json".format(**self._solution)

    def create(
        self,
        customer_name,
        street,
        city,
        region,
        postal_code,
        iso_country,
        friendly_name=values.unset,
        emergency_enabled=values.unset,
        auto_correct_address=values.unset,
        street_secondary=values.unset,
    ):
        """
        Create the AddressInstance

        :param str customer_name: The name to associate with the new address.
        :param str street: The number and street address of the new address.
        :param str city: The city of the new address.
        :param str region: The state or region of the new address.
        :param str postal_code: The postal code of the new address.
        :param str iso_country: The ISO country code of the new address.
        :param str friendly_name: A descriptive string that you create to describe the new address. It can be up to 64 characters long.
        :param bool emergency_enabled: Whether to enable emergency calling on the new address. Can be: `true` or `false`.
        :param bool auto_correct_address: Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.
        :param str street_secondary: The additional number and street address of the address.

        :returns: The created AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressInstance
        """
        data = values.of(
            {
                "CustomerName": customer_name,
                "Street": street,
                "City": city,
                "Region": region,
                "PostalCode": postal_code,
                "IsoCountry": iso_country,
                "FriendlyName": friendly_name,
                "EmergencyEnabled": emergency_enabled,
                "AutoCorrectAddress": auto_correct_address,
                "StreetSecondary": street_secondary,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AddressInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    async def create_async(
        self,
        customer_name,
        street,
        city,
        region,
        postal_code,
        iso_country,
        friendly_name=values.unset,
        emergency_enabled=values.unset,
        auto_correct_address=values.unset,
        street_secondary=values.unset,
    ):
        """
        Asynchronously create the AddressInstance

        :param str customer_name: The name to associate with the new address.
        :param str street: The number and street address of the new address.
        :param str city: The city of the new address.
        :param str region: The state or region of the new address.
        :param str postal_code: The postal code of the new address.
        :param str iso_country: The ISO country code of the new address.
        :param str friendly_name: A descriptive string that you create to describe the new address. It can be up to 64 characters long.
        :param bool emergency_enabled: Whether to enable emergency calling on the new address. Can be: `true` or `false`.
        :param bool auto_correct_address: Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.
        :param str street_secondary: The additional number and street address of the address.

        :returns: The created AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressInstance
        """
        data = values.of(
            {
                "CustomerName": customer_name,
                "Street": street,
                "City": city,
                "Region": region,
                "PostalCode": postal_code,
                "IsoCountry": iso_country,
                "FriendlyName": friendly_name,
                "EmergencyEnabled": emergency_enabled,
                "AutoCorrectAddress": auto_correct_address,
                "StreetSecondary": street_secondary,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AddressInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def stream(
        self,
        customer_name=values.unset,
        friendly_name=values.unset,
        iso_country=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Streams AddressInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str customer_name: The `customer_name` of the Address resources to read.
        :param str friendly_name: The string that identifies the Address resources to read.
        :param str iso_country: The ISO country code of the Address resources to read.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.address.AddressInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            customer_name=customer_name,
            friendly_name=friendly_name,
            iso_country=iso_country,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        customer_name=values.unset,
        friendly_name=values.unset,
        iso_country=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously streams AddressInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str customer_name: The `customer_name` of the Address resources to read.
        :param str friendly_name: The string that identifies the Address resources to read.
        :param str iso_country: The ISO country code of the Address resources to read.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.address.AddressInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            customer_name=customer_name,
            friendly_name=friendly_name,
            iso_country=iso_country,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        customer_name=values.unset,
        friendly_name=values.unset,
        iso_country=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Lists AddressInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str customer_name: The `customer_name` of the Address resources to read.
        :param str friendly_name: The string that identifies the Address resources to read.
        :param str iso_country: The ISO country code of the Address resources to read.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.address.AddressInstance]
        """
        return list(
            self.stream(
                customer_name=customer_name,
                friendly_name=friendly_name,
                iso_country=iso_country,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        customer_name=values.unset,
        friendly_name=values.unset,
        iso_country=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously lists AddressInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str customer_name: The `customer_name` of the Address resources to read.
        :param str friendly_name: The string that identifies the Address resources to read.
        :param str iso_country: The ISO country code of the Address resources to read.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.address.AddressInstance]
        """
        return list(
            await self.stream_async(
                customer_name=customer_name,
                friendly_name=friendly_name,
                iso_country=iso_country,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        customer_name=values.unset,
        friendly_name=values.unset,
        iso_country=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of AddressInstance records from the API.
        Request is executed immediately

        :param str customer_name: The `customer_name` of the Address resources to read.
        :param str friendly_name: The string that identifies the Address resources to read.
        :param str iso_country: The ISO country code of the Address resources to read.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressPage
        """
        data = values.of(
            {
                "CustomerName": customer_name,
                "FriendlyName": friendly_name,
                "IsoCountry": iso_country,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AddressPage(self._version, response, self._solution)

    async def page_async(
        self,
        customer_name=values.unset,
        friendly_name=values.unset,
        iso_country=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of AddressInstance records from the API.
        Request is executed immediately

        :param str customer_name: The `customer_name` of the Address resources to read.
        :param str friendly_name: The string that identifies the Address resources to read.
        :param str iso_country: The ISO country code of the Address resources to read.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressPage
        """
        data = values.of(
            {
                "CustomerName": customer_name,
                "FriendlyName": friendly_name,
                "IsoCountry": iso_country,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return AddressPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AddressInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AddressPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of AddressInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AddressPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a AddressContext

        :param sid: The Twilio-provided string that uniquely identifies the Address resource to update.

        :returns: twilio.rest.api.v2010.account.address.AddressContext
        :rtype: twilio.rest.api.v2010.account.address.AddressContext
        """
        return AddressContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __call__(self, sid):
        """
        Constructs a AddressContext

        :param sid: The Twilio-provided string that uniquely identifies the Address resource to update.

        :returns: twilio.rest.api.v2010.account.address.AddressContext
        :rtype: twilio.rest.api.v2010.account.address.AddressContext
        """
        return AddressContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Api.V2010.AddressList>"


class AddressPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of AddressInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.address.AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressInstance
        """
        return AddressInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.AddressPage>"


class AddressInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, sid: Optional[str] = None):
        """
        Initialize the AddressInstance

        :returns: twilio.rest.api.v2010.account.address.AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "city": payload.get("city"),
            "customer_name": payload.get("customer_name"),
            "date_created": deserialize.rfc2822_datetime(payload.get("date_created")),
            "date_updated": deserialize.rfc2822_datetime(payload.get("date_updated")),
            "friendly_name": payload.get("friendly_name"),
            "iso_country": payload.get("iso_country"),
            "postal_code": payload.get("postal_code"),
            "region": payload.get("region"),
            "sid": payload.get("sid"),
            "street": payload.get("street"),
            "uri": payload.get("uri"),
            "emergency_enabled": payload.get("emergency_enabled"),
            "validated": payload.get("validated"),
            "verified": payload.get("verified"),
            "street_secondary": payload.get("street_secondary"),
        }

        self._context = None
        self._solution = {
            "account_sid": account_sid,
            "sid": sid or self._properties["sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AddressContext for this AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressContext
        """
        if self._context is None:
            self._context = AddressContext(
                self._version,
                account_sid=self._solution["account_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def city(self):
        """
        :returns: The city in which the address is located.
        :rtype: str
        """
        return self._properties["city"]

    @property
    def customer_name(self):
        """
        :returns: The name associated with the address.This property has a maximum length of 16 4-byte characters, or 21 3-byte characters.
        :rtype: str
        """
        return self._properties["customer_name"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def iso_country(self):
        """
        :returns: The ISO country code of the address.
        :rtype: str
        """
        return self._properties["iso_country"]

    @property
    def postal_code(self):
        """
        :returns: The postal code of the address.
        :rtype: str
        """
        return self._properties["postal_code"]

    @property
    def region(self):
        """
        :returns: The state or region of the address.
        :rtype: str
        """
        return self._properties["region"]

    @property
    def sid(self):
        """
        :returns: The unique string that that we created to identify the Address resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def street(self):
        """
        :returns: The number and street address of the address.
        :rtype: str
        """
        return self._properties["street"]

    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties["uri"]

    @property
    def emergency_enabled(self):
        """
        :returns: Whether emergency calling has been enabled on this number.
        :rtype: bool
        """
        return self._properties["emergency_enabled"]

    @property
    def validated(self):
        """
        :returns: Whether the address has been validated to comply with local regulation. In countries that require valid addresses, an invalid address will not be accepted. `true` indicates the Address has been validated. `false` indicate the country doesn't require validation or the Address is not valid.
        :rtype: bool
        """
        return self._properties["validated"]

    @property
    def verified(self):
        """
        :returns: Whether the address has been verified to comply with regulation. In countries that require valid addresses, an invalid address will not be accepted. `true` indicates the Address has been verified. `false` indicate the country doesn't require verified or the Address is not valid.
        :rtype: bool
        """
        return self._properties["verified"]

    @property
    def street_secondary(self):
        """
        :returns: The additional number and street address of the address.
        :rtype: str
        """
        return self._properties["street_secondary"]

    def delete(self):
        """
        Deletes the AddressInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the AddressInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the AddressInstance


        :returns: The fetched AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AddressInstance


        :returns: The fetched AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name=values.unset,
        customer_name=values.unset,
        street=values.unset,
        city=values.unset,
        region=values.unset,
        postal_code=values.unset,
        emergency_enabled=values.unset,
        auto_correct_address=values.unset,
        street_secondary=values.unset,
    ):
        """
        Update the AddressInstance

        :param str friendly_name: A descriptive string that you create to describe the address. It can be up to 64 characters long.
        :param str customer_name: The name to associate with the address.
        :param str street: The number and street address of the address.
        :param str city: The city of the address.
        :param str region: The state or region of the address.
        :param str postal_code: The postal code of the address.
        :param bool emergency_enabled: Whether to enable emergency calling on the address. Can be: `true` or `false`.
        :param bool auto_correct_address: Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.
        :param str street_secondary: The additional number and street address of the address.

        :returns: The updated AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            customer_name=customer_name,
            street=street,
            city=city,
            region=region,
            postal_code=postal_code,
            emergency_enabled=emergency_enabled,
            auto_correct_address=auto_correct_address,
            street_secondary=street_secondary,
        )

    async def update_async(
        self,
        friendly_name=values.unset,
        customer_name=values.unset,
        street=values.unset,
        city=values.unset,
        region=values.unset,
        postal_code=values.unset,
        emergency_enabled=values.unset,
        auto_correct_address=values.unset,
        street_secondary=values.unset,
    ):
        """
        Asynchronous coroutine to update the AddressInstance

        :param str friendly_name: A descriptive string that you create to describe the address. It can be up to 64 characters long.
        :param str customer_name: The name to associate with the address.
        :param str street: The number and street address of the address.
        :param str city: The city of the address.
        :param str region: The state or region of the address.
        :param str postal_code: The postal code of the address.
        :param bool emergency_enabled: Whether to enable emergency calling on the address. Can be: `true` or `false`.
        :param bool auto_correct_address: Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.
        :param str street_secondary: The additional number and street address of the address.

        :returns: The updated AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            customer_name=customer_name,
            street=street,
            city=city,
            region=region,
            postal_code=postal_code,
            emergency_enabled=emergency_enabled,
            auto_correct_address=auto_correct_address,
            street_secondary=street_secondary,
        )

    @property
    def dependent_phone_numbers(self):
        """
        Access the dependent_phone_numbers

        :returns: twilio.rest.api.v2010.account.address.DependentPhoneNumberList
        :rtype: twilio.rest.api.v2010.account.address.DependentPhoneNumberList
        """
        return self._proxy.dependent_phone_numbers

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AddressInstance {}>".format(context)


class AddressContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the AddressContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to update.
        :param sid: The Twilio-provided string that uniquely identifies the Address resource to update.

        :returns: twilio.rest.api.v2010.account.address.AddressContext
        :rtype: twilio.rest.api.v2010.account.address.AddressContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/Addresses/{sid}.json".format(
            **self._solution
        )

        self._dependent_phone_numbers = None

    def delete(self):
        """
        Deletes the AddressInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the AddressInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the AddressInstance


        :returns: The fetched AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AddressInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AddressInstance


        :returns: The fetched AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AddressInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name=values.unset,
        customer_name=values.unset,
        street=values.unset,
        city=values.unset,
        region=values.unset,
        postal_code=values.unset,
        emergency_enabled=values.unset,
        auto_correct_address=values.unset,
        street_secondary=values.unset,
    ):
        """
        Update the AddressInstance

        :param str friendly_name: A descriptive string that you create to describe the address. It can be up to 64 characters long.
        :param str customer_name: The name to associate with the address.
        :param str street: The number and street address of the address.
        :param str city: The city of the address.
        :param str region: The state or region of the address.
        :param str postal_code: The postal code of the address.
        :param bool emergency_enabled: Whether to enable emergency calling on the address. Can be: `true` or `false`.
        :param bool auto_correct_address: Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.
        :param str street_secondary: The additional number and street address of the address.

        :returns: The updated AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "CustomerName": customer_name,
                "Street": street,
                "City": city,
                "Region": region,
                "PostalCode": postal_code,
                "EmergencyEnabled": emergency_enabled,
                "AutoCorrectAddress": auto_correct_address,
                "StreetSecondary": street_secondary,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AddressInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        friendly_name=values.unset,
        customer_name=values.unset,
        street=values.unset,
        city=values.unset,
        region=values.unset,
        postal_code=values.unset,
        emergency_enabled=values.unset,
        auto_correct_address=values.unset,
        street_secondary=values.unset,
    ):
        """
        Asynchronous coroutine to update the AddressInstance

        :param str friendly_name: A descriptive string that you create to describe the address. It can be up to 64 characters long.
        :param str customer_name: The name to associate with the address.
        :param str street: The number and street address of the address.
        :param str city: The city of the address.
        :param str region: The state or region of the address.
        :param str postal_code: The postal code of the address.
        :param bool emergency_enabled: Whether to enable emergency calling on the address. Can be: `true` or `false`.
        :param bool auto_correct_address: Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.
        :param str street_secondary: The additional number and street address of the address.

        :returns: The updated AddressInstance
        :rtype: twilio.rest.api.v2010.account.address.AddressInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "CustomerName": customer_name,
                "Street": street,
                "City": city,
                "Region": region,
                "PostalCode": postal_code,
                "EmergencyEnabled": emergency_enabled,
                "AutoCorrectAddress": auto_correct_address,
                "StreetSecondary": street_secondary,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AddressInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    @property
    def dependent_phone_numbers(self):
        """
        Access the dependent_phone_numbers

        :returns: twilio.rest.api.v2010.account.address.DependentPhoneNumberList
        :rtype: twilio.rest.api.v2010.account.address.DependentPhoneNumberList
        """
        if self._dependent_phone_numbers is None:
            self._dependent_phone_numbers = DependentPhoneNumberList(
                self._version,
                self._solution["account_sid"],
                self._solution["sid"],
            )
        return self._dependent_phone_numbers

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AddressContext {}>".format(context)
