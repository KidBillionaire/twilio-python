r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Sync
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
from twilio.rest.sync.v1.service.document import DocumentList
from twilio.rest.sync.v1.service.sync_list import SyncListList
from twilio.rest.sync.v1.service.sync_map import SyncMapList
from twilio.rest.sync.v1.service.sync_stream import SyncStreamList


class ServiceList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the ServiceList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.sync.v1.service.ServiceList
        :rtype: twilio.rest.sync.v1.service.ServiceList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Services".format(**self._solution)

    def create(
        self,
        friendly_name=values.unset,
        webhook_url=values.unset,
        reachability_webhooks_enabled=values.unset,
        acl_enabled=values.unset,
        reachability_debouncing_enabled=values.unset,
        reachability_debouncing_window=values.unset,
        webhooks_from_rest_enabled=values.unset,
    ):
        """
        Create the ServiceInstance

        :param str friendly_name: A string that you assign to describe the resource.
        :param str webhook_url: The URL we should call when Sync objects are manipulated.
        :param bool reachability_webhooks_enabled: Whether the service instance should call `webhook_url` when client endpoints connect to Sync. The default is `false`.
        :param bool acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource.
        :param bool reachability_debouncing_enabled: Whether every `endpoint_disconnected` event should occur after a configurable delay. The default is `false`, where the `endpoint_disconnected` event occurs immediately after disconnection. When `true`, intervening reconnections can prevent the `endpoint_disconnected` event.
        :param int reachability_debouncing_window: The reachability event delay in milliseconds if `reachability_debouncing_enabled` = `true`.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the `webhook_url` is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the call to `webhook_url`.
        :param bool webhooks_from_rest_enabled: Whether the Service instance should call `webhook_url` when the REST API is used to update Sync objects. The default is `false`.

        :returns: The created ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServiceInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "WebhookUrl": webhook_url,
                "ReachabilityWebhooksEnabled": reachability_webhooks_enabled,
                "AclEnabled": acl_enabled,
                "ReachabilityDebouncingEnabled": reachability_debouncing_enabled,
                "ReachabilityDebouncingWindow": reachability_debouncing_window,
                "WebhooksFromRestEnabled": webhooks_from_rest_enabled,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload)

    async def create_async(
        self,
        friendly_name=values.unset,
        webhook_url=values.unset,
        reachability_webhooks_enabled=values.unset,
        acl_enabled=values.unset,
        reachability_debouncing_enabled=values.unset,
        reachability_debouncing_window=values.unset,
        webhooks_from_rest_enabled=values.unset,
    ):
        """
        Asynchronously create the ServiceInstance

        :param str friendly_name: A string that you assign to describe the resource.
        :param str webhook_url: The URL we should call when Sync objects are manipulated.
        :param bool reachability_webhooks_enabled: Whether the service instance should call `webhook_url` when client endpoints connect to Sync. The default is `false`.
        :param bool acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource.
        :param bool reachability_debouncing_enabled: Whether every `endpoint_disconnected` event should occur after a configurable delay. The default is `false`, where the `endpoint_disconnected` event occurs immediately after disconnection. When `true`, intervening reconnections can prevent the `endpoint_disconnected` event.
        :param int reachability_debouncing_window: The reachability event delay in milliseconds if `reachability_debouncing_enabled` = `true`.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the `webhook_url` is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the call to `webhook_url`.
        :param bool webhooks_from_rest_enabled: Whether the Service instance should call `webhook_url` when the REST API is used to update Sync objects. The default is `false`.

        :returns: The created ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServiceInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "WebhookUrl": webhook_url,
                "ReachabilityWebhooksEnabled": reachability_webhooks_enabled,
                "AclEnabled": acl_enabled,
                "ReachabilityDebouncingEnabled": reachability_debouncing_enabled,
                "ReachabilityDebouncingWindow": reachability_debouncing_window,
                "WebhooksFromRestEnabled": webhooks_from_rest_enabled,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload)

    def stream(self, limit=None, page_size=None):
        """
        Streams ServiceInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.sync.v1.service.ServiceInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams ServiceInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.sync.v1.service.ServiceInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.sync.v1.service.ServiceInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.sync.v1.service.ServiceInstance]
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
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServicePage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ServicePage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServicePage
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
        return ServicePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServicePage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ServicePage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServicePage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ServicePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ServiceContext

        :param sid: The SID of the Service resource to update.

        :returns: twilio.rest.sync.v1.service.ServiceContext
        :rtype: twilio.rest.sync.v1.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a ServiceContext

        :param sid: The SID of the Service resource to update.

        :returns: twilio.rest.sync.v1.service.ServiceContext
        :rtype: twilio.rest.sync.v1.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Sync.V1.ServiceList>"


class ServicePage(Page):
    def get_instance(self, payload):
        """
        Build an instance of ServiceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.sync.v1.service.ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServiceInstance
        """
        return ServiceInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Sync.V1.ServicePage>"


class ServiceInstance(InstanceResource):
    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the ServiceInstance

        :returns: twilio.rest.sync.v1.service.ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServiceInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "unique_name": payload.get("unique_name"),
            "account_sid": payload.get("account_sid"),
            "friendly_name": payload.get("friendly_name"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "url": payload.get("url"),
            "webhook_url": payload.get("webhook_url"),
            "webhooks_from_rest_enabled": payload.get("webhooks_from_rest_enabled"),
            "reachability_webhooks_enabled": payload.get(
                "reachability_webhooks_enabled"
            ),
            "acl_enabled": payload.get("acl_enabled"),
            "reachability_debouncing_enabled": payload.get(
                "reachability_debouncing_enabled"
            ),
            "reachability_debouncing_window": deserialize.integer(
                payload.get("reachability_debouncing_window")
            ),
            "links": payload.get("links"),
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

        :returns: ServiceContext for this ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServiceContext
        """
        if self._context is None:
            self._context = ServiceContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Service resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource. It is a read-only property, it cannot be assigned using REST API.
        :rtype: str
        """
        return self._properties["unique_name"]

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties["friendly_name"]

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
        :returns: The absolute URL of the Service resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def webhook_url(self):
        """
        :returns: The URL we call when Sync objects are manipulated.
        :rtype: str
        """
        return self._properties["webhook_url"]

    @property
    def webhooks_from_rest_enabled(self):
        """
        :returns: Whether the Service instance should call `webhook_url` when the REST API is used to update Sync objects. The default is `false`.
        :rtype: bool
        """
        return self._properties["webhooks_from_rest_enabled"]

    @property
    def reachability_webhooks_enabled(self):
        """
        :returns: Whether the service instance calls `webhook_url` when client endpoints connect to Sync. The default is `false`.
        :rtype: bool
        """
        return self._properties["reachability_webhooks_enabled"]

    @property
    def acl_enabled(self):
        """
        :returns: Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource. It is disabled (false) by default.
        :rtype: bool
        """
        return self._properties["acl_enabled"]

    @property
    def reachability_debouncing_enabled(self):
        """
        :returns: Whether every `endpoint_disconnected` event should occur after a configurable delay. The default is `false`, where the `endpoint_disconnected` event occurs immediately after disconnection. When `true`, intervening reconnections can prevent the `endpoint_disconnected` event.
        :rtype: bool
        """
        return self._properties["reachability_debouncing_enabled"]

    @property
    def reachability_debouncing_window(self):
        """
        :returns: The reachability event delay in milliseconds if `reachability_debouncing_enabled` = `true`.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before `webhook_url` is called, if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the reachability event from occurring.
        :rtype: int
        """
        return self._properties["reachability_debouncing_window"]

    @property
    def links(self):
        """
        :returns: The URLs of related resources.
        :rtype: dict
        """
        return self._properties["links"]

    def delete(self):
        """
        Deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServiceInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServiceInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        webhook_url=values.unset,
        friendly_name=values.unset,
        reachability_webhooks_enabled=values.unset,
        acl_enabled=values.unset,
        reachability_debouncing_enabled=values.unset,
        reachability_debouncing_window=values.unset,
        webhooks_from_rest_enabled=values.unset,
    ):
        """
        Update the ServiceInstance

        :param str webhook_url: The URL we should call when Sync objects are manipulated.
        :param str friendly_name: A string that you assign to describe the resource.
        :param bool reachability_webhooks_enabled: Whether the service instance should call `webhook_url` when client endpoints connect to Sync. The default is `false`.
        :param bool acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource.
        :param bool reachability_debouncing_enabled: Whether every `endpoint_disconnected` event should occur after a configurable delay. The default is `false`, where the `endpoint_disconnected` event occurs immediately after disconnection. When `true`, intervening reconnections can prevent the `endpoint_disconnected` event.
        :param int reachability_debouncing_window: The reachability event delay in milliseconds if `reachability_debouncing_enabled` = `true`.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the webhook is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the webhook from being called.
        :param bool webhooks_from_rest_enabled: Whether the Service instance should call `webhook_url` when the REST API is used to update Sync objects. The default is `false`.

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServiceInstance
        """
        return self._proxy.update(
            webhook_url=webhook_url,
            friendly_name=friendly_name,
            reachability_webhooks_enabled=reachability_webhooks_enabled,
            acl_enabled=acl_enabled,
            reachability_debouncing_enabled=reachability_debouncing_enabled,
            reachability_debouncing_window=reachability_debouncing_window,
            webhooks_from_rest_enabled=webhooks_from_rest_enabled,
        )

    async def update_async(
        self,
        webhook_url=values.unset,
        friendly_name=values.unset,
        reachability_webhooks_enabled=values.unset,
        acl_enabled=values.unset,
        reachability_debouncing_enabled=values.unset,
        reachability_debouncing_window=values.unset,
        webhooks_from_rest_enabled=values.unset,
    ):
        """
        Asynchronous coroutine to update the ServiceInstance

        :param str webhook_url: The URL we should call when Sync objects are manipulated.
        :param str friendly_name: A string that you assign to describe the resource.
        :param bool reachability_webhooks_enabled: Whether the service instance should call `webhook_url` when client endpoints connect to Sync. The default is `false`.
        :param bool acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource.
        :param bool reachability_debouncing_enabled: Whether every `endpoint_disconnected` event should occur after a configurable delay. The default is `false`, where the `endpoint_disconnected` event occurs immediately after disconnection. When `true`, intervening reconnections can prevent the `endpoint_disconnected` event.
        :param int reachability_debouncing_window: The reachability event delay in milliseconds if `reachability_debouncing_enabled` = `true`.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the webhook is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the webhook from being called.
        :param bool webhooks_from_rest_enabled: Whether the Service instance should call `webhook_url` when the REST API is used to update Sync objects. The default is `false`.

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServiceInstance
        """
        return await self._proxy.update_async(
            webhook_url=webhook_url,
            friendly_name=friendly_name,
            reachability_webhooks_enabled=reachability_webhooks_enabled,
            acl_enabled=acl_enabled,
            reachability_debouncing_enabled=reachability_debouncing_enabled,
            reachability_debouncing_window=reachability_debouncing_window,
            webhooks_from_rest_enabled=webhooks_from_rest_enabled,
        )

    @property
    def documents(self):
        """
        Access the documents

        :returns: twilio.rest.sync.v1.service.DocumentList
        :rtype: twilio.rest.sync.v1.service.DocumentList
        """
        return self._proxy.documents

    @property
    def sync_lists(self):
        """
        Access the sync_lists

        :returns: twilio.rest.sync.v1.service.SyncListList
        :rtype: twilio.rest.sync.v1.service.SyncListList
        """
        return self._proxy.sync_lists

    @property
    def sync_maps(self):
        """
        Access the sync_maps

        :returns: twilio.rest.sync.v1.service.SyncMapList
        :rtype: twilio.rest.sync.v1.service.SyncMapList
        """
        return self._proxy.sync_maps

    @property
    def sync_streams(self):
        """
        Access the sync_streams

        :returns: twilio.rest.sync.v1.service.SyncStreamList
        :rtype: twilio.rest.sync.v1.service.SyncStreamList
        """
        return self._proxy.sync_streams

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Sync.V1.ServiceInstance {}>".format(context)


class ServiceContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the ServiceContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Service resource to update.

        :returns: twilio.rest.sync.v1.service.ServiceContext
        :rtype: twilio.rest.sync.v1.service.ServiceContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Services/{sid}".format(**self._solution)

        self._documents = None
        self._sync_lists = None
        self._sync_maps = None
        self._sync_streams = None

    def delete(self):
        """
        Deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServiceInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServiceInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        webhook_url=values.unset,
        friendly_name=values.unset,
        reachability_webhooks_enabled=values.unset,
        acl_enabled=values.unset,
        reachability_debouncing_enabled=values.unset,
        reachability_debouncing_window=values.unset,
        webhooks_from_rest_enabled=values.unset,
    ):
        """
        Update the ServiceInstance

        :param str webhook_url: The URL we should call when Sync objects are manipulated.
        :param str friendly_name: A string that you assign to describe the resource.
        :param bool reachability_webhooks_enabled: Whether the service instance should call `webhook_url` when client endpoints connect to Sync. The default is `false`.
        :param bool acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource.
        :param bool reachability_debouncing_enabled: Whether every `endpoint_disconnected` event should occur after a configurable delay. The default is `false`, where the `endpoint_disconnected` event occurs immediately after disconnection. When `true`, intervening reconnections can prevent the `endpoint_disconnected` event.
        :param int reachability_debouncing_window: The reachability event delay in milliseconds if `reachability_debouncing_enabled` = `true`.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the webhook is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the webhook from being called.
        :param bool webhooks_from_rest_enabled: Whether the Service instance should call `webhook_url` when the REST API is used to update Sync objects. The default is `false`.

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServiceInstance
        """
        data = values.of(
            {
                "WebhookUrl": webhook_url,
                "FriendlyName": friendly_name,
                "ReachabilityWebhooksEnabled": reachability_webhooks_enabled,
                "AclEnabled": acl_enabled,
                "ReachabilityDebouncingEnabled": reachability_debouncing_enabled,
                "ReachabilityDebouncingWindow": reachability_debouncing_window,
                "WebhooksFromRestEnabled": webhooks_from_rest_enabled,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        webhook_url=values.unset,
        friendly_name=values.unset,
        reachability_webhooks_enabled=values.unset,
        acl_enabled=values.unset,
        reachability_debouncing_enabled=values.unset,
        reachability_debouncing_window=values.unset,
        webhooks_from_rest_enabled=values.unset,
    ):
        """
        Asynchronous coroutine to update the ServiceInstance

        :param str webhook_url: The URL we should call when Sync objects are manipulated.
        :param str friendly_name: A string that you assign to describe the resource.
        :param bool reachability_webhooks_enabled: Whether the service instance should call `webhook_url` when client endpoints connect to Sync. The default is `false`.
        :param bool acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource.
        :param bool reachability_debouncing_enabled: Whether every `endpoint_disconnected` event should occur after a configurable delay. The default is `false`, where the `endpoint_disconnected` event occurs immediately after disconnection. When `true`, intervening reconnections can prevent the `endpoint_disconnected` event.
        :param int reachability_debouncing_window: The reachability event delay in milliseconds if `reachability_debouncing_enabled` = `true`.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the webhook is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the webhook from being called.
        :param bool webhooks_from_rest_enabled: Whether the Service instance should call `webhook_url` when the REST API is used to update Sync objects. The default is `false`.

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.sync.v1.service.ServiceInstance
        """
        data = values.of(
            {
                "WebhookUrl": webhook_url,
                "FriendlyName": friendly_name,
                "ReachabilityWebhooksEnabled": reachability_webhooks_enabled,
                "AclEnabled": acl_enabled,
                "ReachabilityDebouncingEnabled": reachability_debouncing_enabled,
                "ReachabilityDebouncingWindow": reachability_debouncing_window,
                "WebhooksFromRestEnabled": webhooks_from_rest_enabled,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def documents(self):
        """
        Access the documents

        :returns: twilio.rest.sync.v1.service.DocumentList
        :rtype: twilio.rest.sync.v1.service.DocumentList
        """
        if self._documents is None:
            self._documents = DocumentList(
                self._version,
                self._solution["sid"],
            )
        return self._documents

    @property
    def sync_lists(self):
        """
        Access the sync_lists

        :returns: twilio.rest.sync.v1.service.SyncListList
        :rtype: twilio.rest.sync.v1.service.SyncListList
        """
        if self._sync_lists is None:
            self._sync_lists = SyncListList(
                self._version,
                self._solution["sid"],
            )
        return self._sync_lists

    @property
    def sync_maps(self):
        """
        Access the sync_maps

        :returns: twilio.rest.sync.v1.service.SyncMapList
        :rtype: twilio.rest.sync.v1.service.SyncMapList
        """
        if self._sync_maps is None:
            self._sync_maps = SyncMapList(
                self._version,
                self._solution["sid"],
            )
        return self._sync_maps

    @property
    def sync_streams(self):
        """
        Access the sync_streams

        :returns: twilio.rest.sync.v1.service.SyncStreamList
        :rtype: twilio.rest.sync.v1.service.SyncStreamList
        """
        if self._sync_streams is None:
            self._sync_streams = SyncStreamList(
                self._version,
                self._solution["sid"],
            )
        return self._sync_streams

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Sync.V1.ServiceContext {}>".format(context)
