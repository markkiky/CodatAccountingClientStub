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
from swagger_client.api.reports_api import ReportsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestReportsApi(unittest.TestCase):
    """ReportsApi unit test stubs"""

    def setUp(self):
        self.api = ReportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_aged_creditors_report(self):
        """Test case for get_aged_creditors_report

        Aged creditors report  # noqa: E501
        """
        pass

    def test_get_aged_debtors_report(self):
        """Test case for get_aged_debtors_report

        Aged debtors report  # noqa: E501
        """
        pass

    def test_get_balance_sheet(self):
        """Test case for get_balance_sheet

        Get balance sheet  # noqa: E501
        """
        pass

    def test_get_cash_flow_statement(self):
        """Test case for get_cash_flow_statement

        Get cash flow statement  # noqa: E501
        """
        pass

    def test_get_profit_and_loss(self):
        """Test case for get_profit_and_loss

        Get profit and loss  # noqa: E501
        """
        pass

    def test_is_aged_creditors_report_available(self):
        """Test case for is_aged_creditors_report_available

        Aged creditors report available  # noqa: E501
        """
        pass

    def test_is_aged_debtor_report_available(self):
        """Test case for is_aged_debtor_report_available

        Aged debtors report available  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
