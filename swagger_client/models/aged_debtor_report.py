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

class AgedDebtorReport(object):
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
        'generated': 'datetime',
        'report_date': 'datetime',
        'data': 'object'
    }

    attribute_map = {
        'generated': 'generated',
        'report_date': 'reportDate',
        'data': 'data'
    }

    def __init__(self, generated=None, report_date=None, data=None):  # noqa: E501
        """AgedDebtorReport - a model defined in Swagger"""  # noqa: E501
        self._generated = None
        self._report_date = None
        self._data = None
        self.discriminator = None
        if generated is not None:
            self.generated = generated
        if report_date is not None:
            self.report_date = report_date
        if data is not None:
            self.data = data

    @property
    def generated(self):
        """Gets the generated of this AgedDebtorReport.  # noqa: E501

        Date and time the report was generated.  # noqa: E501

        :return: The generated of this AgedDebtorReport.  # noqa: E501
        :rtype: datetime
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this AgedDebtorReport.

        Date and time the report was generated.  # noqa: E501

        :param generated: The generated of this AgedDebtorReport.  # noqa: E501
        :type: datetime
        """

        self._generated = generated

    @property
    def report_date(self):
        """Gets the report_date of this AgedDebtorReport.  # noqa: E501

        Date the report is generated up to.  # noqa: E501

        :return: The report_date of this AgedDebtorReport.  # noqa: E501
        :rtype: datetime
        """
        return self._report_date

    @report_date.setter
    def report_date(self, report_date):
        """Sets the report_date of this AgedDebtorReport.

        Date the report is generated up to.  # noqa: E501

        :param report_date: The report_date of this AgedDebtorReport.  # noqa: E501
        :type: datetime
        """

        self._report_date = report_date

    @property
    def data(self):
        """Gets the data of this AgedDebtorReport.  # noqa: E501

        Array of aged debtors.  # noqa: E501

        :return: The data of this AgedDebtorReport.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AgedDebtorReport.

        Array of aged debtors.  # noqa: E501

        :param data: The data of this AgedDebtorReport.  # noqa: E501
        :type: object
        """

        self._data = data

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
        if issubclass(AgedDebtorReport, dict):
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
        if not isinstance(other, AgedDebtorReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
