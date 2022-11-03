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

from typing import TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.mgmt.core import ARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin

from ._configuration import MarketplaceRPServiceConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class MarketplaceRPService(MultiApiClientMixin, _SDKClient):
    """REST APIs for Azure Marketplace.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param market: The Market to use for the request. Default value is "US".
    :type market: str
    :param include_stop_sold_plans: The Market to use for the request. Default value is "true".
    :type include_stop_sold_plans: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2018-08-01-beta'
    _PROFILE_TAG = "azure.mgmt.marketplace.MarketplaceRPService"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        market="US",  # type: Optional[str]
        include_stop_sold_plans="true",  # type: Optional[str]
        api_version=None, # type: Optional[str]
        base_url="https://management.azure.com",  # type: str
        profile=KnownProfiles.default, # type: KnownProfiles
        **kwargs  # type: Any
    ):
        self._config = MarketplaceRPServiceConfiguration(credential, "US", "true", **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(MarketplaceRPService, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2018-08-01-beta: :mod:`v2018_08_01_beta.models<azure.mgmt.marketplace.v2018_08_01_beta.models>`
        """
        if api_version == '2018-08-01-beta':
            from .v2018_08_01_beta import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def offer(self):
        """Instance depends on the API version:

           * 2018-08-01-beta: :class:`OfferOperations<azure.mgmt.marketplace.v2018_08_01_beta.operations.OfferOperations>`
        """
        api_version = self._get_api_version('offer')
        if api_version == '2018-08-01-beta':
            from .v2018_08_01_beta.operations import OfferOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'offer'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
