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
from swagger_client.api.bank_account_transactions_api import BankAccountTransactionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBankAccountTransactionsApi(unittest.TestCase):
    """BankAccountTransactionsApi unit test stubs"""

    def setUp(self):
        self.api = BankAccountTransactionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_bank_transactions(self):
        """Test case for create_bank_transactions

        Create bank transactions  # noqa: E501
        """
        pass

    def test_get_create_bank_account_model(self):
        """Test case for get_create_bank_account_model

        List push options for bank account bank transactions  # noqa: E501
        """
        pass

    def test_list_bank_account_transactions(self):
        """Test case for list_bank_account_transactions

        List bank transactions for bank account  # noqa: E501
        """
        pass

    def test_list_bank_transactions(self):
        """Test case for list_bank_transactions

        List all bank transactions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
