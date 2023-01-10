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




class ReservationContext(InstanceContext):
    def __init__(self, version: V1, workspace_sid: str, task_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super(ReservationContextList, self).__init__(version)

        # Path Solution
        self._solution = { workspace_sid, task_sid, sid,  }
        self._uri = '/Workspaces/${workspace_sid}/Tasks/${task_sid}/Reservations/${sid}'
        
        
        def fetch(self):
            
            """
            Fetch the ReservationInstance

            :returns: The fetched ReservationInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return ReservationInstance(
                self._version,
                payload,
                workspace_sidtask_sidsid=self._solution['workspace_sid''task_sid''sid'],
            )
            
            
        
        def update(self, if_match, body):
            data = values.of({
                'if_match': if_match,'body': body,
            })

            payload = self._version.update(method='post', uri=self._uri, data=data, )

            return ReservationInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'], task_sid=self._solution['task_sid'], sid=self._solution['sid'], )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ReservationContext>'



class ReservationInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid: str, task_sid: str, sid: str):
        super(ReservationInstance, self).__init__(version)
        self._properties = { 
            'account_sid' = payload.get('account_sid'),
            'date_created' = payload.get('date_created'),
            'date_updated' = payload.get('date_updated'),
            'reservation_status' = payload.get('reservation_status'),
            'sid' = payload.get('sid'),
            'task_sid' = payload.get('task_sid'),
            'worker_name' = payload.get('worker_name'),
            'worker_sid' = payload.get('worker_sid'),
            'workspace_sid' = payload.get('workspace_sid'),
            'url' = payload.get('url'),
            'links' = payload.get('links'),
        }

        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid or self._properties['workspace_sid']'task_sid': task_sid or self._properties['task_sid']'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ReservationContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],task_sid=self._solution['task_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.ReservationInstance {}>'.format(context)



class ReservationListInstance(ListResource):
    def __init__(self, version: V1, workspace_sid: str, task_sid: str):
        # TODO: needs autogenerated docs
        super(ReservationListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = { workspace_sid, task_sid,  }
        self._uri = '/Workspaces/${workspace_sid}/Tasks/${task_sid}/Reservations'
        
        
        def page(self, reservation_status, worker_sid, page_size):
            
            data = values.of({
                'reservation_status': reservation_status,'worker_sid': worker_sid,'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return ReservationPage(self._version, payload, workspace_sid=self._solution['workspace_sid']task_sid=self._solution['task_sid'])
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ReservationListInstance>'

