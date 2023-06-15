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


class CustomersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_customer(self, **kwargs):  # noqa: E501
        """Create customer  # noqa: E501

        Posts an individual customer for a given company.  Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) to see which integrations support this endpoint.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_customer(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :param object timeout_in_minutes:
        :return: CreateCustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_customer_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_customer_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_customer_with_http_info(self, **kwargs):  # noqa: E501
        """Create customer  # noqa: E501

        Posts an individual customer for a given company.  Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) to see which integrations support this endpoint.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_customer_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :param object timeout_in_minutes:
        :return: CreateCustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'timeout_in_minutes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_customer" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'timeout_in_minutes' in params:
            query_params.append(('timeoutInMinutes', params['timeout_in_minutes']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth_header']  # noqa: E501

        return self.api_client.call_api(
            '/companies/{companyId}/connections/{connectionId}/push/customers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateCustomerResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_customer_attachment(self, **kwargs):  # noqa: E501
        """Download customer attachment  # noqa: E501

        ﻿Download customer attachment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_customer_attachment(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_customer_attachment_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.download_customer_attachment_with_http_info(**kwargs)  # noqa: E501
            return data

    def download_customer_attachment_with_http_info(self, **kwargs):  # noqa: E501
        """Download customer attachment  # noqa: E501

        ﻿Download customer attachment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_customer_attachment_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
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
                    " to method download_customer_attachment" % key
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
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth_header']  # noqa: E501

        return self.api_client.call_api(
            '/companies/{companyId}/connections/{connectionId}/data/customers/{customerId}/attachments/{attachmentId}/download', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_create_update_customers_model(self, **kwargs):  # noqa: E501
        """Get create/update customer model  # noqa: E501

        ﻿Get create/update customer model. Returns the expected data for the request payload.  See the examples for integration-specific indicative models.  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating and updating customers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_create_update_customers_model(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PushOption
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_create_update_customers_model_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_create_update_customers_model_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_create_update_customers_model_with_http_info(self, **kwargs):  # noqa: E501
        """Get create/update customer model  # noqa: E501

        ﻿Get create/update customer model. Returns the expected data for the request payload.  See the examples for integration-specific indicative models.  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating and updating customers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_create_update_customers_model_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PushOption
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
                    " to method get_create_update_customers_model" % key
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
            '/companies/{companyId}/connections/{connectionId}/options/customers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PushOption',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_customer(self, **kwargs):  # noqa: E501
        """Get customer  # noqa: E501

        ﻿Gets a single customer corresponding to the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_customer(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Customer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_customer_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_customer_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_customer_with_http_info(self, **kwargs):  # noqa: E501
        """Get customer  # noqa: E501

        ﻿Gets a single customer corresponding to the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_customer_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Customer
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
                    " to method get_customer" % key
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
            '/companies/{companyId}/data/customers/{customerId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Customer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_customer_attachment(self, **kwargs):  # noqa: E501
        """Get customer attachment  # noqa: E501

        ﻿Get  customer attachment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_customer_attachment(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Attachment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_customer_attachment_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_customer_attachment_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_customer_attachment_with_http_info(self, **kwargs):  # noqa: E501
        """Get customer attachment  # noqa: E501

        ﻿Get  customer attachment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_customer_attachment_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Attachment
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
                    " to method get_customer_attachment" % key
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
            '/companies/{companyId}/connections/{connectionId}/data/customers/{customerId}/attachments/{attachmentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Attachment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_customer_attachments(self, **kwargs):  # noqa: E501
        """List customer attachments  # noqa: E501

        ﻿List customer attachments  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_customer_attachments(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AttachmentsDataset
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_customer_attachments_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_customer_attachments_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_customer_attachments_with_http_info(self, **kwargs):  # noqa: E501
        """List customer attachments  # noqa: E501

        ﻿List customer attachments  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_customer_attachments_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AttachmentsDataset
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
                    " to method list_customer_attachments" % key
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
            '/companies/{companyId}/connections/{connectionId}/data/customers/{customerId}/attachments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AttachmentsDataset',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_customers(self, **kwargs):  # noqa: E501
        """List customers  # noqa: E501

        ﻿Gets the latest customers for a company, with pagination.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_customers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: Page number. [Read more](https://docs.codat.io/using-the-api/paging).
        :param object page_size: Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
        :param object query: Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
        :param object order_by: Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
        :return: Customers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_customers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_customers_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_customers_with_http_info(self, **kwargs):  # noqa: E501
        """List customers  # noqa: E501

        ﻿Gets the latest customers for a company, with pagination.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_customers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: Page number. [Read more](https://docs.codat.io/using-the-api/paging).
        :param object page_size: Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
        :param object query: Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
        :param object order_by: Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
        :return: Customers
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size', 'query', 'order_by', 'company_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_customers" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {
            "companyId": params['company_id']
        }

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
            '/companies/{companyId}/data/customers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Customers',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_customer(self, customer_id, **kwargs):  # noqa: E501
        """Update customer  # noqa: E501

        ﻿Posts an updated customer for a given company.  Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support updating customers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_customer(customer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object customer_id: (required)
        :param object body:
        :param object timeout_in_minutes:
        :param object force_update: When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting platform, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check.
        :return: UpdateCustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_customer_with_http_info(customer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_customer_with_http_info(customer_id, **kwargs)  # noqa: E501
            return data

    def update_customer_with_http_info(self, customer_id, **kwargs):  # noqa: E501
        """Update customer  # noqa: E501

        ﻿Posts an updated customer for a given company.  Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support updating customers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_customer_with_http_info(customer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object customer_id: (required)
        :param object body:
        :param object timeout_in_minutes:
        :param object force_update: When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting platform, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check.
        :return: UpdateCustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'body', 'timeout_in_minutes', 'force_update']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_customer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `update_customer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']  # noqa: E501

        query_params = []
        if 'timeout_in_minutes' in params:
            query_params.append(('timeoutInMinutes', params['timeout_in_minutes']))  # noqa: E501
        if 'force_update' in params:
            query_params.append(('forceUpdate', params['force_update']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth_header']  # noqa: E501

        return self.api_client.call_api(
            '/companies/{companyId}/connections/{connectionId}/push/customers/{customerId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpdateCustomerResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
