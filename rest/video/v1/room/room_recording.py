"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
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




class RoomRecordingContext(InstanceContext):
    def __init__(self, version: V1, room_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super(RoomRecordingContextList, self).__init__(version)

        # Path Solution
        self._solution = { room_sid, sid,  }
        self._uri = '/Rooms/${room_sid}/Recordings/${sid}'
        
        
        def delete(self):
            
            
            """
            Deletes the RoomRecordingInstance

            :returns: True if delete succeeds, False otherwise
            :rtype: bool
            """
            return self._version.delete(method='DELETE', uri=self._uri, )
        
        def fetch(self):
            
            """
            Fetch the RoomRecordingInstance

            :returns: The fetched RoomRecordingInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return RoomRecordingInstance(
                self._version,
                payload,
                room_sidsid=self._solution['room_sid''sid'],
            )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.RoomRecordingContext>'



class RoomRecordingInstance(InstanceResource):
    def __init__(self, version, payload, room_sid: str, sid: str):
        super(RoomRecordingInstance, self).__init__(version)
        self._properties = { 
            'account_sid' = payload.get('account_sid'),
            'status' = payload.get('status'),
            'date_created' = payload.get('date_created'),
            'sid' = payload.get('sid'),
            'source_sid' = payload.get('source_sid'),
            'size' = payload.get('size'),
            'url' = payload.get('url'),
            'type' = payload.get('type'),
            'duration' = payload.get('duration'),
            'container_format' = payload.get('container_format'),
            'codec' = payload.get('codec'),
            'grouping_sids' = payload.get('grouping_sids'),
            'track_name' = payload.get('track_name'),
            'offset' = payload.get('offset'),
            'media_external_location' = payload.get('media_external_location'),
            'room_sid' = payload.get('room_sid'),
            'links' = payload.get('links'),
        }

        self._context = None
        self._solution = {
            'room_sid': room_sid or self._properties['room_sid']'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = RoomRecordingContext(
                self._version,
                room_sid=self._solution['room_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.RoomRecordingInstance {}>'.format(context)



class RoomRecordingListInstance(ListResource):
    def __init__(self, version: V1, room_sid: str):
        # TODO: needs autogenerated docs
        super(RoomRecordingListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = { room_sid,  }
        self._uri = '/Rooms/${room_sid}/Recordings'
        
        
        def page(self, status, source_sid, date_created_after, date_created_before, page_size):
            
            data = values.of({
                'status': status,'source_sid': source_sid,'date_created_after': date_created_after,'date_created_before': date_created_before,'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return RoomRecordingPage(self._version, payload, room_sid=self._solution['room_sid'])
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.RoomRecordingListInstance>'

