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
from swagger_client.api.direct_costs_api import DirectCostsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDirectCostsApi(unittest.TestCase):
    """DirectCostsApi unit test stubs"""

    def setUp(self):
        self.api = DirectCostsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_direct_cost(self):
        """Test case for create_direct_cost

        Create direct cost  # noqa: E501
        """
        pass

    def test_download_direct_cost_attachment(self):
        """Test case for download_direct_cost_attachment

        Download direct cost attachment  # noqa: E501
        """
        pass

    def test_get_create_direct_costs_model(self):
        """Test case for get_create_direct_costs_model

        Get create direct cost model  # noqa: E501
        """
        pass

    def test_get_direct_cost(self):
        """Test case for get_direct_cost

        Get direct cost  # noqa: E501
        """
        pass

    def test_get_direct_cost_attachment(self):
        """Test case for get_direct_cost_attachment

        Get direct cost attachment  # noqa: E501
        """
        pass

    def test_list_direct_cost_attachments(self):
        """Test case for list_direct_cost_attachments

        List direct cost attachments  # noqa: E501
        """
        pass

    def test_list_direct_costs(self):
        """Test case for list_direct_costs

        List direct costs  # noqa: E501
        """
        pass

    def test_upload_direct_cost_attachment(self):
        """Test case for upload_direct_cost_attachment

        Upload direct cost attachment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
