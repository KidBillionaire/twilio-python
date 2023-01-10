"""
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

from twilio.base.domain import Domain
from twilio.rest.Api.v2010 import V2010

class Api(Domain):
    def __init__(self, twilio):
        """
        Initialize the Api Domain

        :returns: Domain for Api
        :rtype: twilio.rest.v2010.Api
        """
        super(Api, self).__init__(twilio)
        self.base_url = 'https://Api.twilio.com'
        self._V2010 = None

    @property
    def V2010(self):
        """
        :returns: Versions v2010 of Api
        :rtype: twilio.rest.Api.v2010
        """
        if self._V2010 is None:
            self._V2010 = V2010(self)
        return self._V2010
    

    @property
    def accounts(self):
        """
        :rtype: twilio.rest.v2010.accounts
        """
        return self.v2010.accounts
    

    @property
    def account(self):
        """
        :rtype: twilio.rest.v2010.account
        """
        return self.v2010.account
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api>'
