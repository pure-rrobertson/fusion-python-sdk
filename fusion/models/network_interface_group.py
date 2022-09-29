# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from fusion.models.resource_metadata import ResourceMetadata  # noqa: F401,E501

class NetworkInterfaceGroup(ResourceMetadata):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'region': 'RegionRef',
        'availability_zone': 'AvailabilityZoneRef',
        'group_type': 'str',
        'eth': 'NetworkInterfaceGroupEth'
    }
    if hasattr(ResourceMetadata, "swagger_types"):
        swagger_types.update(ResourceMetadata.swagger_types)

    attribute_map = {
        'region': 'region',
        'availability_zone': 'availability_zone',
        'group_type': 'group_type',
        'eth': 'eth'
    }
    if hasattr(ResourceMetadata, "attribute_map"):
        attribute_map.update(ResourceMetadata.attribute_map)

    def __init__(self, region=None, availability_zone=None, group_type=None, eth=None, *args, **kwargs):  # noqa: E501
        """NetworkInterfaceGroup - a model defined in Swagger"""  # noqa: E501
        self._region = None
        self._availability_zone = None
        self._group_type = None
        self._eth = None
        self.discriminator = None
        if region is not None:
            self.region = region
        if availability_zone is not None:
            self.availability_zone = availability_zone
        self.group_type = group_type
        if eth is not None:
            self.eth = eth
        ResourceMetadata.__init__(self, *args, **kwargs)

    @property
    def region(self):
        """Gets the region of this NetworkInterfaceGroup.  # noqa: E501


        :return: The region of this NetworkInterfaceGroup.  # noqa: E501
        :rtype: RegionRef
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this NetworkInterfaceGroup.


        :param region: The region of this NetworkInterfaceGroup.  # noqa: E501
        :type: RegionRef
        """

        self._region = region

    @property
    def availability_zone(self):
        """Gets the availability_zone of this NetworkInterfaceGroup.  # noqa: E501


        :return: The availability_zone of this NetworkInterfaceGroup.  # noqa: E501
        :rtype: AvailabilityZoneRef
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this NetworkInterfaceGroup.


        :param availability_zone: The availability_zone of this NetworkInterfaceGroup.  # noqa: E501
        :type: AvailabilityZoneRef
        """

        self._availability_zone = availability_zone

    @property
    def group_type(self):
        """Gets the group_type of this NetworkInterfaceGroup.  # noqa: E501

        The type of this Network Interface Group.  # noqa: E501

        :return: The group_type of this NetworkInterfaceGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this NetworkInterfaceGroup.

        The type of this Network Interface Group.  # noqa: E501

        :param group_type: The group_type of this NetworkInterfaceGroup.  # noqa: E501
        :type: str
        """
        if group_type is None:
            raise ValueError("Invalid value for `group_type`, must not be `None`")  # noqa: E501
        allowed_values = ["eth"]  # noqa: E501
        if group_type not in allowed_values:
            raise ValueError(
                "Invalid value for `group_type` ({0}), must be one of {1}"  # noqa: E501
                .format(group_type, allowed_values)
            )

        self._group_type = group_type

    @property
    def eth(self):
        """Gets the eth of this NetworkInterfaceGroup.  # noqa: E501


        :return: The eth of this NetworkInterfaceGroup.  # noqa: E501
        :rtype: NetworkInterfaceGroupEth
        """
        return self._eth

    @eth.setter
    def eth(self, eth):
        """Sets the eth of this NetworkInterfaceGroup.


        :param eth: The eth of this NetworkInterfaceGroup.  # noqa: E501
        :type: NetworkInterfaceGroupEth
        """

        self._eth = eth

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NetworkInterfaceGroup, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NetworkInterfaceGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
