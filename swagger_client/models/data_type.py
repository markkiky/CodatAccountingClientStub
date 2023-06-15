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

class DataType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ACCOUNTTRANSACTIONS = "accountTransactions"
    BALANCESHEET = "balanceSheet"
    BANKACCOUNTS = "bankAccounts"
    BANKTRANSACTIONS = "bankTransactions"
    BILLCREDITNOTES = "billCreditNotes"
    BILLPAYMENTS = "billPayments"
    BILLS = "bills"
    CASHFLOWSTATEMENT = "cashFlowStatement"
    CHARTOFACCOUNTS = "chartOfAccounts"
    COMPANY = "company"
    CREDITNOTES = "creditNotes"
    CUSTOMERS = "customers"
    DIRECTCOSTS = "directCosts"
    DIRECTINCOMES = "directIncomes"
    INVOICES = "invoices"
    ITEMS = "items"
    JOURNALENTRIES = "journalEntries"
    JOURNALS = "journals"
    PAYMENTMETHODS = "paymentMethods"
    PAYMENTS = "payments"
    PROFITANDLOSS = "profitAndLoss"
    PURCHASEORDERS = "purchaseOrders"
    SALESORDERS = "salesOrders"
    SUPPLIERS = "suppliers"
    TAXRATES = "taxRates"
    TRACKINGCATEGORIES = "trackingCategories"
    TRANSFERS = "transfers"
    BANKING_ACCOUNTBALANCES = "banking-accountBalances"
    BANKING_ACCOUNTS = "banking-accounts"
    BANKING_TRANSACTIONCATEGORIES = "banking-transactionCategories"
    BANKING_TRANSACTIONS = "banking-transactions"
    COMMERCE_COMPANYINFO = "commerce-companyInfo"
    COMMERCE_CUSTOMERS = "commerce-customers"
    COMMERCE_DISPUTES = "commerce-disputes"
    COMMERCE_LOCATIONS = "commerce-locations"
    COMMERCE_ORDERS = "commerce-orders"
    COMMERCE_PAYMENTMETHODS = "commerce-paymentMethods"
    COMMERCE_PAYMENTS = "commerce-payments"
    COMMERCE_PRODUCTCATEGORIES = "commerce-productCategories"
    COMMERCE_PRODUCTS = "commerce-products"
    COMMERCE_TAXCOMPONENTS = "commerce-taxComponents"
    COMMERCE_TRANSACTIONS = "commerce-transactions"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """DataType - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(DataType, dict):
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
        if not isinstance(other, DataType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
