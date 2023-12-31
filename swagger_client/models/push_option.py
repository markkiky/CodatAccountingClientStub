# coding: utf-8

"""
    Accounting API

    A flexible API for pulling accounting data, normalized and aggregated from 20 accounting integrations.  Standardize how you connect to your customers’ accounting software. View, create, update, and delete data in the same way for all the leading accounting platforms.  [Read more...](https://docs.codat.io/accounting-api/overview)  [See our OpenAPI spec](https://github.com/codatio/oas)      # noqa: E501

    OpenAPI spec version: 2.1.0
    Contact: support@codat.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PushOption(object):
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
        'type': 'PushOptiondefinitionspushOptionType',
        'display_name': 'object',
        'description': 'object',
        'properties': 'object',
        'required': 'object',
        'options': 'object',
        'validation': 'PushOptiondefinitionspushValidationInfo'
    }

    attribute_map = {
        'type': 'type',
        'display_name': 'displayName',
        'description': 'description',
        'properties': 'properties',
        'required': 'required',
        'options': 'options',
        'validation': 'validation'
    }

    def __init__(self, type=None, display_name=None, description=None, properties=None, required=None, options=None, validation=None):  # noqa: E501
        """PushOption - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._display_name = None
        self._description = None
        self._properties = None
        self._required = None
        self._options = None
        self._validation = None
        self.discriminator = None
        self.type = type
        self.display_name = display_name
        if description is not None:
            self.description = description
        if properties is not None:
            self.properties = properties
        self.required = required
        if options is not None:
            self.options = options
        if validation is not None:
            self.validation = validation

    @property
    def type(self):
        """Gets the type of this PushOption.  # noqa: E501


        :return: The type of this PushOption.  # noqa: E501
        :rtype: PushOptiondefinitionspushOptionType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PushOption.


        :param type: The type of this PushOption.  # noqa: E501
        :type: PushOptiondefinitionspushOptionType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def display_name(self):
        """Gets the display_name of this PushOption.  # noqa: E501


        :return: The display_name of this PushOption.  # noqa: E501
        :rtype: object
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PushOption.


        :param display_name: The display_name of this PushOption.  # noqa: E501
        :type: object
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this PushOption.  # noqa: E501


        :return: The description of this PushOption.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PushOption.


        :param description: The description of this PushOption.  # noqa: E501
        :type: object
        """

        self._description = description

    @property
    def properties(self):
        """Gets the properties of this PushOption.  # noqa: E501


        :return: The properties of this PushOption.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this PushOption.


        :param properties: The properties of this PushOption.  # noqa: E501
        :type: object
        """

        self._properties = properties

    @property
    def required(self):
        """Gets the required of this PushOption.  # noqa: E501


        :return: The required of this PushOption.  # noqa: E501
        :rtype: object
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this PushOption.


        :param required: The required of this PushOption.  # noqa: E501
        :type: object
        """
        if required is None:
            raise ValueError("Invalid value for `required`, must not be `None`")  # noqa: E501

        self._required = required

    @property
    def options(self):
        """Gets the options of this PushOption.  # noqa: E501


        :return: The options of this PushOption.  # noqa: E501
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PushOption.


        :param options: The options of this PushOption.  # noqa: E501
        :type: object
        """

        self._options = options

    @property
    def validation(self):
        """Gets the validation of this PushOption.  # noqa: E501


        :return: The validation of this PushOption.  # noqa: E501
        :rtype: PushOptiondefinitionspushValidationInfo
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        """Sets the validation of this PushOption.


        :param validation: The validation of this PushOption.  # noqa: E501
        :type: PushOptiondefinitionspushValidationInfo
        """

        self._validation = validation

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
        if issubclass(PushOption, dict):
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
        if not isinstance(other, PushOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
