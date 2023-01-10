"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Microvisor
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.domain import Domain
from twilio.rest.Microvisor.v1 import V1

class Microvisor(Domain):
    def __init__(self, twilio):
        """
        Initialize the Microvisor Domain

        :returns: Domain for Microvisor
        :rtype: twilio.rest.v1.Microvisor
        """
        super(Microvisor, self).__init__(twilio)
        self.base_url = 'https://Microvisor.twilio.com'
        self._V1 = None

    @property
    def V1(self):
        """
        :returns: Versions v1 of Microvisor
        :rtype: twilio.rest.Microvisor.v1
        """
        if self._V1 is None:
            self._V1 = V1(self)
        return self._V1
    

    @property
    def apps(self):
        """
        :rtype: twilio.rest.v1.apps
        """
        return self.v1.apps
    

    @property
    def devices(self):
        """
        :rtype: twilio.rest.v1.devices
        """
        return self.v1.devices
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Microvisor>'
