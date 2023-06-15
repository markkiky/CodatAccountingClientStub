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


class BankAccountsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_bank_account(self, **kwargs):  # noqa: E501
        """Create bank account  # noqa: E501

        Posts a new bank account to the accounting package for a given company.    Required data may vary by integration. To see what data to post, first call [Get create/update bank account model](https://docs.codat.io/accounting-api#/operations/get-create-update-bankAccounts-model).    Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) to see which integrations support this endpoint.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_bank_account(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :param object allow_sync_on_push_complete:
        :param object timeout_in_minutes:
        :return: CreateBankAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_bank_account_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_bank_account_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_bank_account_with_http_info(self, **kwargs):  # noqa: E501
        """Create bank account  # noqa: E501

        Posts a new bank account to the accounting package for a given company.    Required data may vary by integration. To see what data to post, first call [Get create/update bank account model](https://docs.codat.io/accounting-api#/operations/get-create-update-bankAccounts-model).    Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) to see which integrations support this endpoint.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_bank_account_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :param object allow_sync_on_push_complete:
        :param object timeout_in_minutes:
        :return: CreateBankAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'allow_sync_on_push_complete', 'timeout_in_minutes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_bank_account" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'allow_sync_on_push_complete' in params:
            query_params.append(('allowSyncOnPushComplete', params['allow_sync_on_push_complete']))  # noqa: E501
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
            '/companies/{companyId}/connections/{connectionId}/push/bankAccounts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateBankAccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_bank_account(self, **kwargs):  # noqa: E501
        """Get bank account  # noqa: E501

        Gets the bank account for given account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_bank_account(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
        :return: BankStatementAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_bank_account_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_bank_account_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_bank_account_with_http_info(self, **kwargs):  # noqa: E501
        """Get bank account  # noqa: E501

        Gets the bank account for given account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_bank_account_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
        :return: BankStatementAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_bank_account" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501

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
            '/companies/{companyId}/data/bankAccounts/{accountId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BankStatementAccount',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bank_account(self, **kwargs):  # noqa: E501
        """Get bank account  # noqa: E501

        Gets the bank account with a given ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bank_account(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: BankAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bank_account_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_bank_account_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_bank_account_with_http_info(self, **kwargs):  # noqa: E501
        """Get bank account  # noqa: E501

        Gets the bank account with a given ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bank_account_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: BankAccount
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
                    " to method get_bank_account" % key
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
            '/companies/{companyId}/connections/{connectionId}/data/bankAccounts/{accountId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BankAccount',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_create_update_bank_accounts_model(self, **kwargs):  # noqa: E501
        """Get create/update bank account model  # noqa: E501

        Get create/update bank account model. Returns the expected data for the request payload.    See the examples for integration-specific indicative models.    > **Supported Integrations**  >   > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support creating and updating bank accounts.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_create_update_bank_accounts_model(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PushOption
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_create_update_bank_accounts_model_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_create_update_bank_accounts_model_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_create_update_bank_accounts_model_with_http_info(self, **kwargs):  # noqa: E501
        """Get create/update bank account model  # noqa: E501

        Get create/update bank account model. Returns the expected data for the request payload.    See the examples for integration-specific indicative models.    > **Supported Integrations**  >   > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support creating and updating bank accounts.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_create_update_bank_accounts_model_with_http_info(async_req=True)
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
                    " to method get_create_update_bank_accounts_model" % key
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
            '/companies/{companyId}/connections/{connectionId}/options/bankAccounts', 'GET',
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

    def list_bank_accounts(self, **kwargs):  # noqa: E501
        """List bank accounts  # noqa: E501

        Gets the list of bank accounts for a given connection  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_bank_accounts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: Page number. [Read more](https://docs.codat.io/using-the-api/paging).
        :param object page_size: Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
        :param object query: Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
        :param object order_by: Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
        :return: BankAccounts
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_bank_accounts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_bank_accounts_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_bank_accounts_with_http_info(self, **kwargs):  # noqa: E501
        """List bank accounts  # noqa: E501

        Gets the list of bank accounts for a given connection  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_bank_accounts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: Page number. [Read more](https://docs.codat.io/using-the-api/paging).
        :param object page_size: Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
        :param object query: Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
        :param object order_by: Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
        :return: BankAccounts
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
                    " to method list_bank_accounts" % key
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
            '/companies/{companyId}/connections/{connectionId}/data/bankAccounts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BankAccounts',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_bank_account(self, **kwargs):  # noqa: E501
        """Update bank account  # noqa: E501

        Posts an updated bank account to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call []().  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support updating bank accounts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_bank_account(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :param object timeout_in_minutes:
        :param object force_update: When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting platform, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check.
        :return: UpdateBankAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_bank_account_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_bank_account_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_bank_account_with_http_info(self, **kwargs):  # noqa: E501
        """Update bank account  # noqa: E501

        Posts an updated bank account to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call []().  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support updating bank accounts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_bank_account_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :param object timeout_in_minutes:
        :param object force_update: When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting platform, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check.
        :return: UpdateBankAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'timeout_in_minutes', 'force_update']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_bank_account" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/companies/{companyId}/connections/{connectionId}/push/bankAccounts/{bankAccountId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpdateBankAccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)