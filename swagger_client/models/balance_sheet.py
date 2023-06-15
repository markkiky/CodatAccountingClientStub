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

class BalanceSheet(object):
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
        'currency': 'TransferdefinitionstransferAccountpropertiescurrency',
        'reports': 'object',
        'most_recent_available_month': 'datetime',
        'earliest_available_month': 'datetime'
    }

    attribute_map = {
        'currency': 'currency',
        'reports': 'reports',
        'most_recent_available_month': 'mostRecentAvailableMonth',
        'earliest_available_month': 'earliestAvailableMonth'
    }

    def __init__(self, currency=None, reports=None, most_recent_available_month=None, earliest_available_month=None):  # noqa: E501
        """BalanceSheet - a model defined in Swagger"""  # noqa: E501
        self._currency = None
        self._reports = None
        self._most_recent_available_month = None
        self._earliest_available_month = None
        self.discriminator = None
        self.currency = currency
        self.reports = reports
        if most_recent_available_month is not None:
            self.most_recent_available_month = most_recent_available_month
        if earliest_available_month is not None:
            self.earliest_available_month = earliest_available_month

    @property
    def currency(self):
        """Gets the currency of this BalanceSheet.  # noqa: E501

        Currency of the balance sheet.  # noqa: E501

        :return: The currency of this BalanceSheet.  # noqa: E501
        :rtype: TransferdefinitionstransferAccountpropertiescurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this BalanceSheet.

        Currency of the balance sheet.  # noqa: E501

        :param currency: The currency of this BalanceSheet.  # noqa: E501
        :type: TransferdefinitionstransferAccountpropertiescurrency
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def reports(self):
        """Gets the reports of this BalanceSheet.  # noqa: E501

        An array of balance sheet reports.  # noqa: E501

        :return: The reports of this BalanceSheet.  # noqa: E501
        :rtype: object
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """Sets the reports of this BalanceSheet.

        An array of balance sheet reports.  # noqa: E501

        :param reports: The reports of this BalanceSheet.  # noqa: E501
        :type: object
        """
        if reports is None:
            raise ValueError("Invalid value for `reports`, must not be `None`")  # noqa: E501

        self._reports = reports

    @property
    def most_recent_available_month(self):
        """Gets the most_recent_available_month of this BalanceSheet.  # noqa: E501

        Most recent available monthly report data.  # noqa: E501

        :return: The most_recent_available_month of this BalanceSheet.  # noqa: E501
        :rtype: datetime
        """
        return self._most_recent_available_month

    @most_recent_available_month.setter
    def most_recent_available_month(self, most_recent_available_month):
        """Sets the most_recent_available_month of this BalanceSheet.

        Most recent available monthly report data.  # noqa: E501

        :param most_recent_available_month: The most_recent_available_month of this BalanceSheet.  # noqa: E501
        :type: datetime
        """

        self._most_recent_available_month = most_recent_available_month

    @property
    def earliest_available_month(self):
        """Gets the earliest_available_month of this BalanceSheet.  # noqa: E501

        Earliest available monthly report data.  # noqa: E501

        :return: The earliest_available_month of this BalanceSheet.  # noqa: E501
        :rtype: datetime
        """
        return self._earliest_available_month

    @earliest_available_month.setter
    def earliest_available_month(self, earliest_available_month):
        """Sets the earliest_available_month of this BalanceSheet.

        Earliest available monthly report data.  # noqa: E501

        :param earliest_available_month: The earliest_available_month of this BalanceSheet.  # noqa: E501
        :type: datetime
        """

        self._earliest_available_month = earliest_available_month

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
        if issubclass(BalanceSheet, dict):
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
        if not isinstance(other, BalanceSheet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
