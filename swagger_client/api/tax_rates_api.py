# coding: utf-8

"""
    Accounting API

    A flexible API for pulling accounting data, normalized and aggregated from 20 accounting integrations.  Standardize how you connect to your customers’ accounting software. View, create, update, and delete data in the same way for all the leading accounting platforms.  [Read more...](https://docs.codat.io/accounting-api/overview)  [See our OpenAPI spec](https://github.com/codatio/oas)      # noqa: E501

    OpenAPI spec version: 2.1.0
    Contact: support@codat.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TaxRatesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_tax_rate(self, **kwargs):  # noqa: E501
        """Get tax rate  # noqa: E501

        Gets the specified tax rate for a given company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tax_rate(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: TaxRate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tax_rate_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_tax_rate_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_tax_rate_with_http_info(self, **kwargs):  # noqa: E501
        """Get tax rate  # noqa: E501

        Gets the specified tax rate for a given company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tax_rate_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: TaxRate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tax_rate" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth_header']  # noqa: E501

        return self.api_client.call_api(
            '/companies/{companyId}/data/taxRates/{taxRateId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaxRate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_tax_rates(self, **kwargs):  # noqa: E501
        """List all tax rates  # noqa: E501

        Gets the latest tax rates for a given company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_tax_rates(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: Page number. [Read more](https://docs.codat.io/using-the-api/paging).
        :param object page_size: Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
        :param object query: Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
        :param object order_by: Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
        :return: TaxRates
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_tax_rates_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_tax_rates_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_tax_rates_with_http_info(self, **kwargs):  # noqa: E501
        """List all tax rates  # noqa: E501

        Gets the latest tax rates for a given company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_tax_rates_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: Page number. [Read more](https://docs.codat.io/using-the-api/paging).
        :param object page_size: Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
        :param object query: Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
        :param object order_by: Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
        :return: TaxRates
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size', 'query', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_tax_rates" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('orderBy', params['order_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth_header']  # noqa: E501

        return self.api_client.call_api(
            '/companies/{companyId}/data/taxRates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaxRates',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
