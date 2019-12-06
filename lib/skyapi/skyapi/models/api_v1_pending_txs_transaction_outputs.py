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


class ApiV1PendingTxsTransactionOutputs(object):
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
        'uxid': 'str',
        'dst': 'str',
        'coins': 'str',
        'hours': 'int'
    }

    attribute_map = {
        'uxid': 'uxid',
        'dst': 'dst',
        'coins': 'coins',
        'hours': 'hours'
    }

    def __init__(self, uxid=None, dst=None, coins=None, hours=None):  # noqa: E501
        """ApiV1PendingTxsTransactionOutputs - a model defined in OpenAPI"""  # noqa: E501

        self._uxid = None
        self._dst = None
        self._coins = None
        self._hours = None
        self.discriminator = None

        if uxid is not None:
            self.uxid = uxid
        if dst is not None:
            self.dst = dst
        if coins is not None:
            self.coins = coins
        if hours is not None:
            self.hours = hours

    @property
    def uxid(self):
        """Gets the uxid of this ApiV1PendingTxsTransactionOutputs.  # noqa: E501


        :return: The uxid of this ApiV1PendingTxsTransactionOutputs.  # noqa: E501
        :rtype: str
        """
        return self._uxid

    @uxid.setter
    def uxid(self, uxid):
        """Sets the uxid of this ApiV1PendingTxsTransactionOutputs.


        :param uxid: The uxid of this ApiV1PendingTxsTransactionOutputs.  # noqa: E501
        :type: str
        """

        self._uxid = uxid

    @property
    def dst(self):
        """Gets the dst of this ApiV1PendingTxsTransactionOutputs.  # noqa: E501


        :return: The dst of this ApiV1PendingTxsTransactionOutputs.  # noqa: E501
        :rtype: str
        """
        return self._dst

    @dst.setter
    def dst(self, dst):
        """Sets the dst of this ApiV1PendingTxsTransactionOutputs.


        :param dst: The dst of this ApiV1PendingTxsTransactionOutputs.  # noqa: E501
        :type: str
        """

        self._dst = dst

    @property
    def coins(self):
        """Gets the coins of this ApiV1PendingTxsTransactionOutputs.  # noqa: E501


        :return: The coins of this ApiV1PendingTxsTransactionOutputs.  # noqa: E501
        :rtype: str
        """
        return self._coins

    @coins.setter
    def coins(self, coins):
        """Sets the coins of this ApiV1PendingTxsTransactionOutputs.


        :param coins: The coins of this ApiV1PendingTxsTransactionOutputs.  # noqa: E501
        :type: str
        """

        self._coins = coins

    @property
    def hours(self):
        """Gets the hours of this ApiV1PendingTxsTransactionOutputs.  # noqa: E501


        :return: The hours of this ApiV1PendingTxsTransactionOutputs.  # noqa: E501
        :rtype: int
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Sets the hours of this ApiV1PendingTxsTransactionOutputs.


        :param hours: The hours of this ApiV1PendingTxsTransactionOutputs.  # noqa: E501
        :type: int
        """

        self._hours = hours

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
        if not isinstance(other, ApiV1PendingTxsTransactionOutputs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
