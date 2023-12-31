# coding: utf-8

"""
    Accounting API

    A flexible API for pulling accounting data, normalized and aggregated from 20 accounting integrations.  Standardize how you connect to your customers’ accounting software. View, create, update, and delete data in the same way for all the leading accounting platforms.  [Read more...](https://docs.codat.io/accounting-api/overview)  [See our OpenAPI spec](https://github.com/codatio/oas)      # noqa: E501

    OpenAPI spec version: 2.1.0
    Contact: support@codat.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.bill_payments_api import BillPaymentsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBillPaymentsApi(unittest.TestCase):
    """BillPaymentsApi unit test stubs"""

    def setUp(self):
        self.api = BillPaymentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_bill_payment(self):
        """Test case for create_bill_payment

        Create bill payments  # noqa: E501
        """
        pass

    def test_delete_bill_payment(self):
        """Test case for delete_bill_payment

        Delete bill payment  # noqa: E501
        """
        pass

    def test_get_bill_payments(self):
        """Test case for get_bill_payments

        Get bill payment  # noqa: E501
        """
        pass

    def test_get_create_bill_payments_model(self):
        """Test case for get_create_bill_payments_model

        Get create bill payment model  # noqa: E501
        """
        pass

    def test_list_bill_payments(self):
        """Test case for list_bill_payments

        List bill payments  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
