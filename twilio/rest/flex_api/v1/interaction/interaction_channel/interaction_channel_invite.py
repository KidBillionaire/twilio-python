r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class InteractionChannelInviteList(ListResource):
    def __init__(self, version: Version, interaction_sid: str, channel_sid: str):
        """
        Initialize the InteractionChannelInviteList

        :param Version version: Version that contains the resource
        :param interaction_sid: The Interaction SID for this Channel.
        :param channel_sid: The Channel SID for this Participant.

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite.InteractionChannelInviteList
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite.InteractionChannelInviteList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "interaction_sid": interaction_sid,
            "channel_sid": channel_sid,
        }
        self._uri = (
            "/Interactions/{interaction_sid}/Channels/{channel_sid}/Invites".format(
                **self._solution
            )
        )

    def create(self, routing):
        """
        Create the InteractionChannelInviteInstance

        :param object routing: The Interaction's routing logic.

        :returns: The created InteractionChannelInviteInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite.InteractionChannelInviteInstance
        """
        data = values.of(
            {
                "Routing": serialize.object(routing),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InteractionChannelInviteInstance(
            self._version,
            payload,
            interaction_sid=self._solution["interaction_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    async def create_async(self, routing):
        """
        Asynchronously create the InteractionChannelInviteInstance

        :param object routing: The Interaction's routing logic.

        :returns: The created InteractionChannelInviteInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite.InteractionChannelInviteInstance
        """
        data = values.of(
            {
                "Routing": serialize.object(routing),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InteractionChannelInviteInstance(
            self._version,
            payload,
            interaction_sid=self._solution["interaction_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams InteractionChannelInviteInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite.InteractionChannelInviteInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams InteractionChannelInviteInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite.InteractionChannelInviteInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists InteractionChannelInviteInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite.InteractionChannelInviteInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists InteractionChannelInviteInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite.InteractionChannelInviteInstance]
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
        Retrieve a single page of InteractionChannelInviteInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InteractionChannelInviteInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite.InteractionChannelInvitePage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return InteractionChannelInvitePage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of InteractionChannelInviteInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InteractionChannelInviteInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite.InteractionChannelInvitePage
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
        return InteractionChannelInvitePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of InteractionChannelInviteInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InteractionChannelInviteInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite.InteractionChannelInvitePage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return InteractionChannelInvitePage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of InteractionChannelInviteInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InteractionChannelInviteInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite.InteractionChannelInvitePage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return InteractionChannelInvitePage(self._version, response, self._solution)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.FlexApi.V1.InteractionChannelInviteList>"


class InteractionChannelInvitePage(Page):
    def get_instance(self, payload):
        """
        Build an instance of InteractionChannelInviteInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite.InteractionChannelInviteInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite.InteractionChannelInviteInstance
        """
        return InteractionChannelInviteInstance(
            self._version,
            payload,
            interaction_sid=self._solution["interaction_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InteractionChannelInvitePage>"


class InteractionChannelInviteInstance(InstanceResource):
    def __init__(self, version, payload, interaction_sid: str, channel_sid: str):
        """
        Initialize the InteractionChannelInviteInstance

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite.InteractionChannelInviteInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite.InteractionChannelInviteInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "interaction_sid": payload.get("interaction_sid"),
            "channel_sid": payload.get("channel_sid"),
            "routing": payload.get("routing"),
            "url": payload.get("url"),
        }

        self._context = None
        self._solution = {
            "interaction_sid": interaction_sid,
            "channel_sid": channel_sid,
        }

    @property
    def sid(self):
        """
        :returns: The unique string created by Twilio to identify an Interaction Channel Invite resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def interaction_sid(self):
        """
        :returns: The Interaction SID for this Channel.
        :rtype: str
        """
        return self._properties["interaction_sid"]

    @property
    def channel_sid(self):
        """
        :returns: The Channel SID for this Invite.
        :rtype: str
        """
        return self._properties["channel_sid"]

    @property
    def routing(self):
        """
        :returns: A JSON object representing the routing rules for the Interaction Channel. See [Outbound SMS Example](https://www.twilio.com/docs/flex/developer/conversations/interactions-api/interactions#agent-initiated-outbound-interactions) for an example Routing object. The Interactions resource uses TaskRouter for all routing functionality.   All attributes in the Routing object on your Interaction request body are added “as is” to the task. For a list of known attributes consumed by the Flex UI and/or Flex Insights, see [Known Task Attributes](https://www.twilio.com/docs/flex/developer/conversations/interactions-api#task-attributes).
        :rtype: dict
        """
        return self._properties["routing"]

    @property
    def url(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["url"]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InteractionChannelInviteInstance {}>".format(context)
