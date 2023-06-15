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
from swagger_client.api.bank_accounts_api import BankAccountsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBankAccountsApi(unittest.TestCase):
    """BankAccountsApi unit test stubs"""

    def setUp(self):
        self.api = BankAccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_bank_account(self):
        """Test case for create_bank_account

        Create bank account  # noqa: E501
        """
        pass

    def test_get_all_bank_account(self):
        """Test case for get_all_bank_account

        Get bank account  # noqa: E501
        """
        pass

    def test_get_bank_account(self):
        """Test case for get_bank_account

        Get bank account  # noqa: E501
        """
        pass

    def test_get_create_update_bank_accounts_model(self):
        """Test case for get_create_update_bank_accounts_model

        Get create/update bank account model  # noqa: E501
        """
        pass

    def test_list_bank_accounts(self):
        """Test case for list_bank_accounts

        List bank accounts  # noqa: E501
        """
        pass

    def test_update_bank_account(self):
        """Test case for update_bank_account

        Update bank account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()