r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.numbers.v2.regulatory_compliance import RegulatoryComplianceList


class V2(Version):
    def __init__(self, domain: Domain):
        """
        Initialize the V2 version of Numbers

        :param domain: The Twilio.numbers domain
        """
        super().__init__(domain, "v2")
        self._regulatory_compliance = None

    @property
    def regulatory_compliance(self) -> RegulatoryComplianceList:
        if self._regulatory_compliance is None:
            self._regulatory_compliance = RegulatoryComplianceList(self)
        return self._regulatory_compliance

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V2>"
