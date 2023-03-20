r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Chat
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.chat.v1.service.channel.invite import InviteList
from twilio.rest.chat.v1.service.channel.member import MemberList
from twilio.rest.chat.v1.service.channel.message import MessageList


class ChannelList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the ChannelList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from.

        :returns: twilio.rest.chat.v1.service.channel.ChannelList
        :rtype: twilio.rest.chat.v1.service.channel.ChannelList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Channels".format(**self._solution)

    def create(
        self,
        friendly_name=values.unset,
        unique_name=values.unset,
        attributes=values.unset,
        type=values.unset,
    ):
        """
        Create the ChannelInstance

        :param str friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL. This value must be 64 characters or less in length and be unique within the Service.
        :param str attributes: A valid JSON string that contains application-specific data.
        :param ChannelInstance.ChannelType type:

        :returns: The created ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "UniqueName": unique_name,
                "Attributes": attributes,
                "Type": type,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ChannelInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self,
        friendly_name=values.unset,
        unique_name=values.unset,
        attributes=values.unset,
        type=values.unset,
    ):
        """
        Asynchronously create the ChannelInstance

        :param str friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL. This value must be 64 characters or less in length and be unique within the Service.
        :param str attributes: A valid JSON string that contains application-specific data.
        :param ChannelInstance.ChannelType type:

        :returns: The created ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "UniqueName": unique_name,
                "Attributes": attributes,
                "Type": type,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ChannelInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(self, type=values.unset, limit=None, page_size=None):
        """
        Streams ChannelInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param list[ChannelInstance.ChannelType] type: The visibility of the Channels to read. Can be: `public` or `private` and defaults to `public`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v1.service.channel.ChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(type=type, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, type=values.unset, limit=None, page_size=None):
        """
        Asynchronously streams ChannelInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param list[ChannelInstance.ChannelType] type: The visibility of the Channels to read. Can be: `public` or `private` and defaults to `public`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v1.service.channel.ChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(type=type, page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, type=values.unset, limit=None, page_size=None):
        """
        Lists ChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param list[ChannelInstance.ChannelType] type: The visibility of the Channels to read. Can be: `public` or `private` and defaults to `public`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v1.service.channel.ChannelInstance]
        """
        return list(
            self.stream(
                type=type,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, type=values.unset, limit=None, page_size=None):
        """
        Asynchronously lists ChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param list[ChannelInstance.ChannelType] type: The visibility of the Channels to read. Can be: `public` or `private` and defaults to `public`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v1.service.channel.ChannelInstance]
        """
        return list(
            await self.stream_async(
                type=type,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        type=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of ChannelInstance records from the API.
        Request is executed immediately

        :param list[ChannelInstance.ChannelType] type: The visibility of the Channels to read. Can be: `public` or `private` and defaults to `public`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelPage
        """
        data = values.of(
            {
                "Type": serialize.map(type, lambda e: e),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ChannelPage(self._version, response, self._solution)

    async def page_async(
        self,
        type=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of ChannelInstance records from the API.
        Request is executed immediately

        :param list[ChannelInstance.ChannelType] type: The visibility of the Channels to read. Can be: `public` or `private` and defaults to `public`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelPage
        """
        data = values.of(
            {
                "Type": serialize.map(type, lambda e: e),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return ChannelPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ChannelPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of ChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ChannelPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ChannelContext

        :param sid: The Twilio-provided string that uniquely identifies the Channel resource to update.

        :returns: twilio.rest.chat.v1.service.channel.ChannelContext
        :rtype: twilio.rest.chat.v1.service.channel.ChannelContext
        """
        return ChannelContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid):
        """
        Constructs a ChannelContext

        :param sid: The Twilio-provided string that uniquely identifies the Channel resource to update.

        :returns: twilio.rest.chat.v1.service.channel.ChannelContext
        :rtype: twilio.rest.chat.v1.service.channel.ChannelContext
        """
        return ChannelContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Chat.V1.ChannelList>"


class ChannelPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of ChannelInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.chat.v1.service.channel.ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelInstance
        """
        return ChannelInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Chat.V1.ChannelPage>"


class ChannelInstance(InstanceResource):
    class ChannelType(object):
        PUBLIC = "public"
        PRIVATE = "private"

    def __init__(self, version, payload, service_sid: str, sid: Optional[str] = None):
        """
        Initialize the ChannelInstance

        :returns: twilio.rest.chat.v1.service.channel.ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "service_sid": payload.get("service_sid"),
            "friendly_name": payload.get("friendly_name"),
            "unique_name": payload.get("unique_name"),
            "attributes": payload.get("attributes"),
            "type": payload.get("type"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "created_by": payload.get("created_by"),
            "members_count": deserialize.integer(payload.get("members_count")),
            "messages_count": deserialize.integer(payload.get("messages_count")),
            "url": payload.get("url"),
            "links": payload.get("links"),
        }

        self._context = None
        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self._properties["sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ChannelContext for this ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelContext
        """
        if self._context is None:
            self._context = ChannelContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Channel resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/api/rest/account) that created the Channel resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def service_sid(self):
        """
        :returns: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) the resource is associated with.
        :rtype: str
        """
        return self._properties["service_sid"]

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.
        :rtype: str
        """
        return self._properties["unique_name"]

    @property
    def attributes(self):
        """
        :returns: The JSON string that stores application-specific data. **Note** If this property has been assigned a value, it's only  displayed in a FETCH action that returns a single resource; otherwise, it's null. If the attributes have not been set, `{}` is returned.
        :rtype: str
        """
        return self._properties["attributes"]

    @property
    def type(self):
        """
        :returns:
        :rtype: ChannelInstance.ChannelType
        """
        return self._properties["type"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def created_by(self):
        """
        :returns: The `identity` of the User that created the channel. If the Channel was created by using the API, the value is `system`.
        :rtype: str
        """
        return self._properties["created_by"]

    @property
    def members_count(self):
        """
        :returns: The number of Members in the Channel.
        :rtype: int
        """
        return self._properties["members_count"]

    @property
    def messages_count(self):
        """
        :returns: The number of Messages in the Channel.
        :rtype: int
        """
        return self._properties["messages_count"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the Channel resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def links(self):
        """
        :returns: The absolute URLs of the [Members](https://www.twilio.com/docs/chat/api/members), [Messages](https://www.twilio.com/docs/chat/api/messages) , [Invites](https://www.twilio.com/docs/chat/api/invites) and, if it exists, the last [Message](https://www.twilio.com/docs/chat/api/messages) for the Channel.
        :rtype: dict
        """
        return self._properties["links"]

    def delete(self):
        """
        Deletes the ChannelInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the ChannelInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the ChannelInstance


        :returns: The fetched ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the ChannelInstance


        :returns: The fetched ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name=values.unset,
        unique_name=values.unset,
        attributes=values.unset,
    ):
        """
        Update the ChannelInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL. This value must be 64 characters or less in length and be unique within the Service.
        :param str attributes: A valid JSON string that contains application-specific data.

        :returns: The updated ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            unique_name=unique_name,
            attributes=attributes,
        )

    async def update_async(
        self,
        friendly_name=values.unset,
        unique_name=values.unset,
        attributes=values.unset,
    ):
        """
        Asynchronous coroutine to update the ChannelInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL. This value must be 64 characters or less in length and be unique within the Service.
        :param str attributes: A valid JSON string that contains application-specific data.

        :returns: The updated ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            unique_name=unique_name,
            attributes=attributes,
        )

    @property
    def invites(self):
        """
        Access the invites

        :returns: twilio.rest.chat.v1.service.channel.InviteList
        :rtype: twilio.rest.chat.v1.service.channel.InviteList
        """
        return self._proxy.invites

    @property
    def members(self):
        """
        Access the members

        :returns: twilio.rest.chat.v1.service.channel.MemberList
        :rtype: twilio.rest.chat.v1.service.channel.MemberList
        """
        return self._proxy.members

    @property
    def messages(self):
        """
        Access the messages

        :returns: twilio.rest.chat.v1.service.channel.MessageList
        :rtype: twilio.rest.chat.v1.service.channel.MessageList
        """
        return self._proxy.messages

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Chat.V1.ChannelInstance {}>".format(context)


class ChannelContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the ChannelContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to update the resource from.
        :param sid: The Twilio-provided string that uniquely identifies the Channel resource to update.

        :returns: twilio.rest.chat.v1.service.channel.ChannelContext
        :rtype: twilio.rest.chat.v1.service.channel.ChannelContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Channels/{sid}".format(**self._solution)

        self._invites = None
        self._members = None
        self._messages = None

    def delete(self):
        """
        Deletes the ChannelInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the ChannelInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the ChannelInstance


        :returns: The fetched ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the ChannelInstance


        :returns: The fetched ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name=values.unset,
        unique_name=values.unset,
        attributes=values.unset,
    ):
        """
        Update the ChannelInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL. This value must be 64 characters or less in length and be unique within the Service.
        :param str attributes: A valid JSON string that contains application-specific data.

        :returns: The updated ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "UniqueName": unique_name,
                "Attributes": attributes,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        friendly_name=values.unset,
        unique_name=values.unset,
        attributes=values.unset,
    ):
        """
        Asynchronous coroutine to update the ChannelInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL. This value must be 64 characters or less in length and be unique within the Service.
        :param str attributes: A valid JSON string that contains application-specific data.

        :returns: The updated ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "UniqueName": unique_name,
                "Attributes": attributes,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    @property
    def invites(self):
        """
        Access the invites

        :returns: twilio.rest.chat.v1.service.channel.InviteList
        :rtype: twilio.rest.chat.v1.service.channel.InviteList
        """
        if self._invites is None:
            self._invites = InviteList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._invites

    @property
    def members(self):
        """
        Access the members

        :returns: twilio.rest.chat.v1.service.channel.MemberList
        :rtype: twilio.rest.chat.v1.service.channel.MemberList
        """
        if self._members is None:
            self._members = MemberList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._members

    @property
    def messages(self):
        """
        Access the messages

        :returns: twilio.rest.chat.v1.service.channel.MessageList
        :rtype: twilio.rest.chat.v1.service.channel.MessageList
        """
        if self._messages is None:
            self._messages = MessageList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._messages

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Chat.V1.ChannelContext {}>".format(context)
