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
from swagger_client.api.account_transactions_api import AccountTransactionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAccountTransactionsApi(unittest.TestCase):
    """AccountTransactionsApi unit test stubs"""

    def setUp(self):
        self.api = AccountTransactionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_account_transaction(self):
        """Test case for get_account_transaction

        Get account transaction  # noqa: E501
        """
        pass

    def test_list_account_transactions(self):
        """Test case for list_account_transactions

        List account transactions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()