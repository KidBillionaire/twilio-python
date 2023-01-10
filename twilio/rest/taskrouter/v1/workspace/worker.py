"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Taskrouter
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

from twilio.rest.worker.reservation import ReservationListInstancefrom twilio.rest.worker.worker_channel import WorkerChannelListInstancefrom twilio.rest.worker.worker_statistics import WorkerStatisticsListInstancefrom twilio.rest.worker.workers_cumulative_statistics import WorkersCumulativeStatisticsListInstancefrom twilio.rest.worker.workers_real_time_statistics import WorkersRealTimeStatisticsListInstancefrom twilio.rest.worker.workers_statistics import WorkersStatisticsListInstance


class WorkerContext(InstanceContext):
    def __init__(self, version: V1, workspace_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super(WorkerContextList, self).__init__(version)

        # Path Solution
        self._solution = { workspace_sid, sid,  }
        self._uri = '/Workspaces/${workspace_sid}/Workers/${sid}'
        
        self._reservations = None
        self._worker_channels = None
        self._statistics = None
        
        def delete(self, if_match):
            
            
            """
            Deletes the WorkerInstance

            :returns: True if delete succeeds, False otherwise
            :rtype: bool
            """
            return self._version.delete(method='DELETE', uri=self._uri, )
        
        def fetch(self):
            
            """
            Fetch the WorkerInstance

            :returns: The fetched WorkerInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return WorkerInstance(
                self._version,
                payload,
                workspace_sidsid=self._solution['workspace_sid''sid'],
            )
            
            
        
        def update(self, if_match, body):
            data = values.of({
                'if_match': if_match,'body': body,
            })

            payload = self._version.update(method='post', uri=self._uri, data=data, )

            return WorkerInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'], sid=self._solution['sid'], )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.WorkerContext>'



class WorkerInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid: str, sid: str):
        super(WorkerInstance, self).__init__(version)
        self._properties = { 
            'account_sid' = payload.get('account_sid'),
            'activity_name' = payload.get('activity_name'),
            'activity_sid' = payload.get('activity_sid'),
            'attributes' = payload.get('attributes'),
            'available' = payload.get('available'),
            'date_created' = payload.get('date_created'),
            'date_status_changed' = payload.get('date_status_changed'),
            'date_updated' = payload.get('date_updated'),
            'friendly_name' = payload.get('friendly_name'),
            'sid' = payload.get('sid'),
            'workspace_sid' = payload.get('workspace_sid'),
            'url' = payload.get('url'),
            'links' = payload.get('links'),
        }

        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid or self._properties['workspace_sid']'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = WorkerContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def reservations(self):
        return self._proxy.reservations
    @property
    def worker_channels(self):
        return self._proxy.worker_channels
    @property
    def statistics(self):
        return self._proxy.statistics
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.WorkerInstance {}>'.format(context)



class WorkerListInstance(ListResource):
    def __init__(self, version: V1, workspace_sid: str):
        # TODO: needs autogenerated docs
        super(WorkerListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = { workspace_sid,  }
        self._uri = '/Workspaces/${workspace_sid}/Workers'
        
        self._cumulative_statistics = None
        self._real_time_statistics = None
        self._statistics = None
        
        def create(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.create(method='post', uri=self._uri, data=data, )

            return WorkerInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'])
            
        
        def page(self, activity_name, activity_sid, available, friendly_name, target_workers_expression, task_queue_name, task_queue_sid, ordering, page_size):
            
            data = values.of({
                'activity_name': activity_name,'activity_sid': activity_sid,'available': available,'friendly_name': friendly_name,'target_workers_expression': target_workers_expression,'task_queue_name': task_queue_name,'task_queue_sid': task_queue_sid,'ordering': ordering,'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return WorkerPage(self._version, payload, workspace_sid=self._solution['workspace_sid'])
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.WorkerListInstance>'

