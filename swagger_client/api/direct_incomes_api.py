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


class DirectIncomesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_direct_income(self, **kwargs):  # noqa: E501
        """Create direct income  # noqa: E501

        Posts a new direct income to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call [Get create direct income model](https://docs.codat.io/accounting-api#/operations/get-create-directIncomes-model).  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) to see which integrations support this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_direct_income(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :param object timeout_in_minutes:
        :return: CreateDirectIncomeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_direct_income_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_direct_income_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_direct_income_with_http_info(self, **kwargs):  # noqa: E501
        """Create direct income  # noqa: E501

        Posts a new direct income to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call [Get create direct income model](https://docs.codat.io/accounting-api#/operations/get-create-directIncomes-model).  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) to see which integrations support this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_direct_income_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :param object timeout_in_minutes:
        :return: CreateDirectIncomeResponse
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
                    " to method create_direct_income" % key
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
            '/companies/{companyId}/connections/{connectionId}/push/directIncomes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateDirectIncomeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_direct_income_attachment(self, attachment_id, **kwargs):  # noqa: E501
        """Download direct income attachment  # noqa: E501

        Downloads an attachment for the specified direct income for a given company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_direct_income_attachment(attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object attachment_id: Unique identifier for an attachment (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_direct_income_attachment_with_http_info(attachment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.download_direct_income_attachment_with_http_info(attachment_id, **kwargs)  # noqa: E501
            return data

    def download_direct_income_attachment_with_http_info(self, attachment_id, **kwargs):  # noqa: E501
        """Download direct income attachment  # noqa: E501

        Downloads an attachment for the specified direct income for a given company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_direct_income_attachment_with_http_info(attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object attachment_id: Unique identifier for an attachment (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['attachment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_direct_income_attachment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'attachment_id' is set
        if ('attachment_id' not in params or
                params['attachment_id'] is None):
            raise ValueError("Missing the required parameter `attachment_id` when calling `download_direct_income_attachment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'attachment_id' in params:
            path_params['attachmentId'] = params['attachment_id']  # noqa: E501

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
            '/companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId}/attachments/{attachmentId}/download', 'GET',
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

    def get_create_direct_incomes_model(self, **kwargs):  # noqa: E501
        """Get create direct income model  # noqa: E501

        Get create direct income model. Returns the expected data for the request payload.  See the examples for integration-specific indicative models.  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support creating direct incomes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_create_direct_incomes_model(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PushOption
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_create_direct_incomes_model_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_create_direct_incomes_model_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_create_direct_incomes_model_with_http_info(self, **kwargs):  # noqa: E501
        """Get create direct income model  # noqa: E501

        Get create direct income model. Returns the expected data for the request payload.  See the examples for integration-specific indicative models.  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support creating direct incomes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_create_direct_incomes_model_with_http_info(async_req=True)
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
                    " to method get_create_direct_incomes_model" % key
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
            '/companies/{companyId}/connections/{connectionId}/options/directIncomes', 'GET',
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

    def get_direct_income(self, direct_income_id, company_id, connection_id, **kwargs):  # noqa: E501
        """Get direct income  # noqa: E501

        Gets the specified direct income for a given company and connection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_direct_income(direct_income_id, company_id, connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object direct_income_id: (required)
        :param object company_id: (required)
        :param object connection_id: (required)
        :return: DirectIncome
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_direct_income_with_http_info(direct_income_id, company_id, connection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_direct_income_with_http_info(direct_income_id, company_id, connection_id, **kwargs)  # noqa: E501
            return data

    def get_direct_income_with_http_info(self, direct_income_id, company_id, connection_id, **kwargs):  # noqa: E501
        """Get direct income  # noqa: E501

        Gets the specified direct income for a given company and connection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_direct_income_with_http_info(direct_income_id, company_id, connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object direct_income_id: (required)
        :param object company_id: (required)
        :param object connection_id: (required)
        :return: DirectIncome
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['direct_income_id', 'company_id', 'connection_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_direct_income" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'direct_income_id' is set
        if ('direct_income_id' not in params or
                params['direct_income_id'] is None):
            raise ValueError("Missing the required parameter `direct_income_id` when calling `get_direct_income`")  # noqa: E501
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `get_direct_income`")  # noqa: E501
        # verify the required parameter 'connection_id' is set
        if ('connection_id' not in params or
                params['connection_id'] is None):
            raise ValueError("Missing the required parameter `connection_id` when calling `get_direct_income`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'direct_income_id' in params:
            path_params['directIncomeId'] = params['direct_income_id']  # noqa: E501
        if 'company_id' in params:
            path_params['companyId'] = params['company_id']  # noqa: E501
        if 'connection_id' in params:
            path_params['connectionId'] = params['connection_id']  # noqa: E501

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
            '/companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectIncome',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_direct_income_attachment(self, **kwargs):  # noqa: E501
        """Get direct income attachment  # noqa: E501

        Gets the specified direct income attachment for a given company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_direct_income_attachment(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object timeout_in_minutes:
        :return: Attachment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_direct_income_attachment_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_direct_income_attachment_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_direct_income_attachment_with_http_info(self, **kwargs):  # noqa: E501
        """Get direct income attachment  # noqa: E501

        Gets the specified direct income attachment for a given company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_direct_income_attachment_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object timeout_in_minutes:
        :return: Attachment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['timeout_in_minutes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_direct_income_attachment" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth_header']  # noqa: E501

        return self.api_client.call_api(
            '/companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId}/attachments/{attachmentId}', 'GET',
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

    def list_direct_income_attachments(self, **kwargs):  # noqa: E501
        """List direct income attachments  # noqa: E501

        Gets all attachments for the specified direct income for a given company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_direct_income_attachments(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AttachmentsDataset
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_direct_income_attachments_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_direct_income_attachments_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_direct_income_attachments_with_http_info(self, **kwargs):  # noqa: E501
        """List direct income attachments  # noqa: E501

        Gets all attachments for the specified direct income for a given company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_direct_income_attachments_with_http_info(async_req=True)
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
                    " to method list_direct_income_attachments" % key
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
            '/companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId}/attachments', 'GET',
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

    def list_direct_incomes(self, **kwargs):  # noqa: E501
        """List direct incomes  # noqa: E501

        Lists the direct incomes for a given company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_direct_incomes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: Page number. [Read more](https://docs.codat.io/using-the-api/paging).
        :param object page_size: Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
        :param object query: Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
        :param object order_by: Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
        :return: DirectIncomes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_direct_incomes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_direct_incomes_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_direct_incomes_with_http_info(self, **kwargs):  # noqa: E501
        """List direct incomes  # noqa: E501

        Lists the direct incomes for a given company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_direct_incomes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: Page number. [Read more](https://docs.codat.io/using-the-api/paging).
        :param object page_size: Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
        :param object query: Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
        :param object order_by: Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
        :return: DirectIncomes
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
                    " to method list_direct_incomes" % key
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
            '/companies/{companyId}/connections/{connectionId}/data/directIncomes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectIncomes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload_direct_income_attachment(self, direct_income_id, company_id, connection_id, **kwargs):  # noqa: E501
        """Create direct income attachment  # noqa: E501

        Posts a new direct income attachment for a given company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_direct_income_attachment(direct_income_id, company_id, connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object direct_income_id: (required)
        :param object company_id: (required)
        :param object connection_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upload_direct_income_attachment_with_http_info(direct_income_id, company_id, connection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.upload_direct_income_attachment_with_http_info(direct_income_id, company_id, connection_id, **kwargs)  # noqa: E501
            return data

    def upload_direct_income_attachment_with_http_info(self, direct_income_id, company_id, connection_id, **kwargs):  # noqa: E501
        """Create direct income attachment  # noqa: E501

        Posts a new direct income attachment for a given company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_direct_income_attachment_with_http_info(direct_income_id, company_id, connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object direct_income_id: (required)
        :param object company_id: (required)
        :param object connection_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['direct_income_id', 'company_id', 'connection_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_direct_income_attachment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'direct_income_id' is set
        if ('direct_income_id' not in params or
                params['direct_income_id'] is None):
            raise ValueError("Missing the required parameter `direct_income_id` when calling `upload_direct_income_attachment`")  # noqa: E501
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `upload_direct_income_attachment`")  # noqa: E501
        # verify the required parameter 'connection_id' is set
        if ('connection_id' not in params or
                params['connection_id'] is None):
            raise ValueError("Missing the required parameter `connection_id` when calling `upload_direct_income_attachment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'direct_income_id' in params:
            path_params['directIncomeId'] = params['direct_income_id']  # noqa: E501
        if 'company_id' in params:
            path_params['companyId'] = params['company_id']  # noqa: E501
        if 'connection_id' in params:
            path_params['connectionId'] = params['connection_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth_header']  # noqa: E501

        return self.api_client.call_api(
            '/companies/{companyId}/connections/{connectionId}/push/directIncomes/{directIncomeId}/attachment', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
