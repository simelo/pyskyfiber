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


class NetworkConnectionSchema(object):
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
        'address': 'str',
        'connected_at': 'int',
        'height': 'int',
        'id': 'int',
        'is_trusted_peer': 'bool',
        'last_received': 'int',
        'last_sent': 'int',
        'listen_port': 'int',
        'mirror': 'int',
        'outgoing': 'bool',
        'state': 'str',
        'unconfirmed_verify_transaction': 'NetworkConnectionSchemaUnconfirmedVerifyTransaction',
        'user_agent': 'str'
    }

    attribute_map = {
        'address': 'address',
        'connected_at': 'connected_at',
        'height': 'height',
        'id': 'id',
        'is_trusted_peer': 'is_trusted_peer',
        'last_received': 'last_received',
        'last_sent': 'last_sent',
        'listen_port': 'listen_port',
        'mirror': 'mirror',
        'outgoing': 'outgoing',
        'state': 'state',
        'unconfirmed_verify_transaction': 'unconfirmed_verify_transaction',
        'user_agent': 'user_agent'
    }

    def __init__(self, address=None, connected_at=None, height=None, id=None, is_trusted_peer=None, last_received=None, last_sent=None, listen_port=None, mirror=None, outgoing=None, state=None, unconfirmed_verify_transaction=None, user_agent=None):  # noqa: E501
        """NetworkConnectionSchema - a model defined in OpenAPI"""  # noqa: E501

        self._address = None
        self._connected_at = None
        self._height = None
        self._id = None
        self._is_trusted_peer = None
        self._last_received = None
        self._last_sent = None
        self._listen_port = None
        self._mirror = None
        self._outgoing = None
        self._state = None
        self._unconfirmed_verify_transaction = None
        self._user_agent = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if connected_at is not None:
            self.connected_at = connected_at
        if height is not None:
            self.height = height
        if id is not None:
            self.id = id
        if is_trusted_peer is not None:
            self.is_trusted_peer = is_trusted_peer
        if last_received is not None:
            self.last_received = last_received
        if last_sent is not None:
            self.last_sent = last_sent
        if listen_port is not None:
            self.listen_port = listen_port
        if mirror is not None:
            self.mirror = mirror
        if outgoing is not None:
            self.outgoing = outgoing
        if state is not None:
            self.state = state
        if unconfirmed_verify_transaction is not None:
            self.unconfirmed_verify_transaction = unconfirmed_verify_transaction
        if user_agent is not None:
            self.user_agent = user_agent

    @property
    def address(self):
        """Gets the address of this NetworkConnectionSchema.  # noqa: E501


        :return: The address of this NetworkConnectionSchema.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this NetworkConnectionSchema.


        :param address: The address of this NetworkConnectionSchema.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def connected_at(self):
        """Gets the connected_at of this NetworkConnectionSchema.  # noqa: E501


        :return: The connected_at of this NetworkConnectionSchema.  # noqa: E501
        :rtype: int
        """
        return self._connected_at

    @connected_at.setter
    def connected_at(self, connected_at):
        """Sets the connected_at of this NetworkConnectionSchema.


        :param connected_at: The connected_at of this NetworkConnectionSchema.  # noqa: E501
        :type: int
        """

        self._connected_at = connected_at

    @property
    def height(self):
        """Gets the height of this NetworkConnectionSchema.  # noqa: E501


        :return: The height of this NetworkConnectionSchema.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this NetworkConnectionSchema.


        :param height: The height of this NetworkConnectionSchema.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def id(self):
        """Gets the id of this NetworkConnectionSchema.  # noqa: E501


        :return: The id of this NetworkConnectionSchema.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetworkConnectionSchema.


        :param id: The id of this NetworkConnectionSchema.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_trusted_peer(self):
        """Gets the is_trusted_peer of this NetworkConnectionSchema.  # noqa: E501


        :return: The is_trusted_peer of this NetworkConnectionSchema.  # noqa: E501
        :rtype: bool
        """
        return self._is_trusted_peer

    @is_trusted_peer.setter
    def is_trusted_peer(self, is_trusted_peer):
        """Sets the is_trusted_peer of this NetworkConnectionSchema.


        :param is_trusted_peer: The is_trusted_peer of this NetworkConnectionSchema.  # noqa: E501
        :type: bool
        """

        self._is_trusted_peer = is_trusted_peer

    @property
    def last_received(self):
        """Gets the last_received of this NetworkConnectionSchema.  # noqa: E501


        :return: The last_received of this NetworkConnectionSchema.  # noqa: E501
        :rtype: int
        """
        return self._last_received

    @last_received.setter
    def last_received(self, last_received):
        """Sets the last_received of this NetworkConnectionSchema.


        :param last_received: The last_received of this NetworkConnectionSchema.  # noqa: E501
        :type: int
        """

        self._last_received = last_received

    @property
    def last_sent(self):
        """Gets the last_sent of this NetworkConnectionSchema.  # noqa: E501


        :return: The last_sent of this NetworkConnectionSchema.  # noqa: E501
        :rtype: int
        """
        return self._last_sent

    @last_sent.setter
    def last_sent(self, last_sent):
        """Sets the last_sent of this NetworkConnectionSchema.


        :param last_sent: The last_sent of this NetworkConnectionSchema.  # noqa: E501
        :type: int
        """

        self._last_sent = last_sent

    @property
    def listen_port(self):
        """Gets the listen_port of this NetworkConnectionSchema.  # noqa: E501


        :return: The listen_port of this NetworkConnectionSchema.  # noqa: E501
        :rtype: int
        """
        return self._listen_port

    @listen_port.setter
    def listen_port(self, listen_port):
        """Sets the listen_port of this NetworkConnectionSchema.


        :param listen_port: The listen_port of this NetworkConnectionSchema.  # noqa: E501
        :type: int
        """

        self._listen_port = listen_port

    @property
    def mirror(self):
        """Gets the mirror of this NetworkConnectionSchema.  # noqa: E501


        :return: The mirror of this NetworkConnectionSchema.  # noqa: E501
        :rtype: int
        """
        return self._mirror

    @mirror.setter
    def mirror(self, mirror):
        """Sets the mirror of this NetworkConnectionSchema.


        :param mirror: The mirror of this NetworkConnectionSchema.  # noqa: E501
        :type: int
        """

        self._mirror = mirror

    @property
    def outgoing(self):
        """Gets the outgoing of this NetworkConnectionSchema.  # noqa: E501


        :return: The outgoing of this NetworkConnectionSchema.  # noqa: E501
        :rtype: bool
        """
        return self._outgoing

    @outgoing.setter
    def outgoing(self, outgoing):
        """Sets the outgoing of this NetworkConnectionSchema.


        :param outgoing: The outgoing of this NetworkConnectionSchema.  # noqa: E501
        :type: bool
        """

        self._outgoing = outgoing

    @property
    def state(self):
        """Gets the state of this NetworkConnectionSchema.  # noqa: E501


        :return: The state of this NetworkConnectionSchema.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this NetworkConnectionSchema.


        :param state: The state of this NetworkConnectionSchema.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "connected", "introduced"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def unconfirmed_verify_transaction(self):
        """Gets the unconfirmed_verify_transaction of this NetworkConnectionSchema.  # noqa: E501


        :return: The unconfirmed_verify_transaction of this NetworkConnectionSchema.  # noqa: E501
        :rtype: NetworkConnectionSchemaUnconfirmedVerifyTransaction
        """
        return self._unconfirmed_verify_transaction

    @unconfirmed_verify_transaction.setter
    def unconfirmed_verify_transaction(self, unconfirmed_verify_transaction):
        """Sets the unconfirmed_verify_transaction of this NetworkConnectionSchema.


        :param unconfirmed_verify_transaction: The unconfirmed_verify_transaction of this NetworkConnectionSchema.  # noqa: E501
        :type: NetworkConnectionSchemaUnconfirmedVerifyTransaction
        """

        self._unconfirmed_verify_transaction = unconfirmed_verify_transaction

    @property
    def user_agent(self):
        """Gets the user_agent of this NetworkConnectionSchema.  # noqa: E501


        :return: The user_agent of this NetworkConnectionSchema.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this NetworkConnectionSchema.


        :param user_agent: The user_agent of this NetworkConnectionSchema.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

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
        if not isinstance(other, NetworkConnectionSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
