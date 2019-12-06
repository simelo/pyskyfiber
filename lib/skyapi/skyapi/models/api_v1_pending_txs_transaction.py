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


class ApiV1PendingTxsTransaction(object):
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
        'length': 'int',
        'type': 'int',
        'txid': 'str',
        'inner_hash': 'str',
        'sigs': 'list[str]',
        'inputs': 'list[str]',
        'outputs': 'list[ApiV1PendingTxsTransactionOutputs]'
    }

    attribute_map = {
        'length': 'length',
        'type': 'type',
        'txid': 'txid',
        'inner_hash': 'inner_hash',
        'sigs': 'sigs',
        'inputs': 'inputs',
        'outputs': 'outputs'
    }

    def __init__(self, length=None, type=None, txid=None, inner_hash=None, sigs=None, inputs=None, outputs=None):  # noqa: E501
        """ApiV1PendingTxsTransaction - a model defined in OpenAPI"""  # noqa: E501

        self._length = None
        self._type = None
        self._txid = None
        self._inner_hash = None
        self._sigs = None
        self._inputs = None
        self._outputs = None
        self.discriminator = None

        if length is not None:
            self.length = length
        if type is not None:
            self.type = type
        if txid is not None:
            self.txid = txid
        if inner_hash is not None:
            self.inner_hash = inner_hash
        if sigs is not None:
            self.sigs = sigs
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs

    @property
    def length(self):
        """Gets the length of this ApiV1PendingTxsTransaction.  # noqa: E501


        :return: The length of this ApiV1PendingTxsTransaction.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this ApiV1PendingTxsTransaction.


        :param length: The length of this ApiV1PendingTxsTransaction.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def type(self):
        """Gets the type of this ApiV1PendingTxsTransaction.  # noqa: E501


        :return: The type of this ApiV1PendingTxsTransaction.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApiV1PendingTxsTransaction.


        :param type: The type of this ApiV1PendingTxsTransaction.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def txid(self):
        """Gets the txid of this ApiV1PendingTxsTransaction.  # noqa: E501


        :return: The txid of this ApiV1PendingTxsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this ApiV1PendingTxsTransaction.


        :param txid: The txid of this ApiV1PendingTxsTransaction.  # noqa: E501
        :type: str
        """

        self._txid = txid

    @property
    def inner_hash(self):
        """Gets the inner_hash of this ApiV1PendingTxsTransaction.  # noqa: E501


        :return: The inner_hash of this ApiV1PendingTxsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._inner_hash

    @inner_hash.setter
    def inner_hash(self, inner_hash):
        """Sets the inner_hash of this ApiV1PendingTxsTransaction.


        :param inner_hash: The inner_hash of this ApiV1PendingTxsTransaction.  # noqa: E501
        :type: str
        """

        self._inner_hash = inner_hash

    @property
    def sigs(self):
        """Gets the sigs of this ApiV1PendingTxsTransaction.  # noqa: E501


        :return: The sigs of this ApiV1PendingTxsTransaction.  # noqa: E501
        :rtype: list[str]
        """
        return self._sigs

    @sigs.setter
    def sigs(self, sigs):
        """Sets the sigs of this ApiV1PendingTxsTransaction.


        :param sigs: The sigs of this ApiV1PendingTxsTransaction.  # noqa: E501
        :type: list[str]
        """

        self._sigs = sigs

    @property
    def inputs(self):
        """Gets the inputs of this ApiV1PendingTxsTransaction.  # noqa: E501


        :return: The inputs of this ApiV1PendingTxsTransaction.  # noqa: E501
        :rtype: list[str]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this ApiV1PendingTxsTransaction.


        :param inputs: The inputs of this ApiV1PendingTxsTransaction.  # noqa: E501
        :type: list[str]
        """

        self._inputs = inputs

    @property
    def outputs(self):
        """Gets the outputs of this ApiV1PendingTxsTransaction.  # noqa: E501


        :return: The outputs of this ApiV1PendingTxsTransaction.  # noqa: E501
        :rtype: list[ApiV1PendingTxsTransactionOutputs]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this ApiV1PendingTxsTransaction.


        :param outputs: The outputs of this ApiV1PendingTxsTransaction.  # noqa: E501
        :type: list[ApiV1PendingTxsTransactionOutputs]
        """

        self._outputs = outputs

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
        if not isinstance(other, ApiV1PendingTxsTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
