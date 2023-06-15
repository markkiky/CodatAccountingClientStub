# swagger_client.AccountTransactionsApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_transaction**](AccountTransactionsApi.md#get_account_transaction) | **GET** /companies/{companyId}/connections/{connectionId}/data/accountTransactions/{accountTransactionId} | Get account transaction
[**list_account_transactions**](AccountTransactionsApi.md#list_account_transactions) | **GET** /companies/{companyId}/connections/{connectionId}/data/accountTransactions | List account transactions

# **get_account_transaction**
> AccountTransaction get_account_transaction(company_id, connection_id, account_transaction_id)

Get account transaction

﻿Returns a specific [account transaction](https://docs.codat.io/accounting-api#/schemas/AccountTransaction).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: auth_header
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AccountTransactionsApi(swagger_client.ApiClient(configuration))
company_id = NULL # object | 
connection_id = NULL # object | 
account_transaction_id = NULL # object | 

try:
    # Get account transaction
    api_response = api_instance.get_account_transaction(company_id, connection_id, account_transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountTransactionsApi->get_account_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**object**](.md)|  | 
 **connection_id** | [**object**](.md)|  | 
 **account_transaction_id** | [**object**](.md)|  | 

### Return type

[**AccountTransaction**](AccountTransaction.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_transactions**
> AccountTransactions list_account_transactions(company_id, connection_id, page=page, page_size=page_size, query=query, order_by=order_by)

List account transactions

﻿The *List account transactions* endpoint returns a list of [account transactions](https://docs.codat.io/accounting-api#/schemas/AccountTransaction) for a given company's connection. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: auth_header
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AccountTransactionsApi(swagger_client.ApiClient(configuration))
company_id = NULL # object | 
connection_id = NULL # object | 
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List account transactions
    api_response = api_instance.list_account_transactions(company_id, connection_id, page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountTransactionsApi->list_account_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**object**](.md)|  | 
 **connection_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**AccountTransactions**](AccountTransactions.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

