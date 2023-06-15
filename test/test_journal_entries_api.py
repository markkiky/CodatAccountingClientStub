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
from swagger_client.api.journal_entries_api import JournalEntriesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestJournalEntriesApi(unittest.TestCase):
    """JournalEntriesApi unit test stubs"""

    def setUp(self):
        self.api = JournalEntriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_journal_entry(self):
        """Test case for create_journal_entry

        Create journal entry  # noqa: E501
        """
        pass

    def test_delete_journal_entry(self):
        """Test case for delete_journal_entry

        Delete journal entry  # noqa: E501
        """
        pass

    def test_get_create_journal_entries_model(self):
        """Test case for get_create_journal_entries_model

        Get create journal entry model  # noqa: E501
        """
        pass

    def test_get_journal_entry(self):
        """Test case for get_journal_entry

        Get journal entry  # noqa: E501
        """
        pass

    def test_list_journal_entries(self):
        """Test case for list_journal_entries

        List journal entries  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
