# coding: utf-8

"""
    Skycoin REST API.

    Skycoin is a next-generation cryptocurrency.  # noqa: E501

    The version of the OpenAPI document: 0.27.0
    Contact: contact@skycoin.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BlockVerboseSchemaBody(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'txns': 'list[object]'
    }

    attribute_map = {
        'txns': 'txns'
    }

    def __init__(self, txns=None):  # noqa: E501
        """BlockVerboseSchemaBody - a model defined in OpenAPI"""  # noqa: E501

        self._txns = None
        self.discriminator = None

        if txns is not None:
            self.txns = txns

    @property
    def txns(self):
        """Gets the txns of this BlockVerboseSchemaBody.  # noqa: E501


        :return: The txns of this BlockVerboseSchemaBody.  # noqa: E501
        :rtype: list[object]
        """
        return self._txns

    @txns.setter
    def txns(self, txns):
        """Sets the txns of this BlockVerboseSchemaBody.


        :param txns: The txns of this BlockVerboseSchemaBody.  # noqa: E501
        :type: list[object]
        """

        self._txns = txns

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BlockVerboseSchemaBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
