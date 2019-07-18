# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CheckNameAvailabilityOutput(Model):
    """Output of check name availability API.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name_availability: Indicates whether the name is available. Possible
     values include: 'Available', 'Unavailable'
    :vartype name_availability: str or
     ~azure.mgmt.frontdoor.models.Availability
    :ivar reason: The reason why the name is not available.
    :vartype reason: str
    :ivar message: The detailed error message describing why the name is not
     available.
    :vartype message: str
    """

    _validation = {
        'name_availability': {'readonly': True},
        'reason': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'name_availability': {'key': 'nameAvailability', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CheckNameAvailabilityOutput, self).__init__(**kwargs)
        self.name_availability = None
        self.reason = None
        self.message = None
