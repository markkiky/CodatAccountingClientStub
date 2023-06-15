# swagger_client.BankAccountTransactionsApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bank_transactions**](BankAccountTransactionsApi.md#create_bank_transactions) | **POST** /companies/{companyId}/connections/{connectionId}/push/bankAccounts/{accountId}/bankTransactions | Create bank transactions
[**get_create_bank_account_model**](BankAccountTransactionsApi.md#get_create_bank_account_model) | **GET** /companies/{companyId}/connections/{connectionId}/options/bankAccounts/{accountId}/bankTransactions | List push options for bank account bank transactions
[**list_bank_account_transactions**](BankAccountTransactionsApi.md#list_bank_account_transactions) | **GET** /companies/{companyId}/connections/{connectionId}/data/bankAccounts/{accountId}/bankTransactions | List bank transactions for bank account
[**list_bank_transactions**](BankAccountTransactionsApi.md#list_bank_transactions) | **GET** /companies/{companyId}/data/bankAccounts/{accountId}/transactions | List all bank transactions

# **create_bank_transactions**
> CreateBankTransactionsResponse create_bank_transactions(company_id, connection_id, account_id, body=body, timeout_in_minutes=timeout_in_minutes, allow_sync_on_push_complete=allow_sync_on_push_complete)

Create bank transactions

Posts bank transactions to the accounting package for a given company.  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankTransactions) to see which integrations support this endpoint.

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
api_instance = swagger_client.BankAccountTransactionsApi(swagger_client.ApiClient(configuration))
company_id = NULL # object | 
connection_id = NULL # object | 
account_id = NULL # object | Unique identifier for an account
body = NULL # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)
allow_sync_on_push_complete = true # object |  (optional) (default to true)

try:
    # Create bank transactions
    api_response = api_instance.create_bank_transactions(company_id, connection_id, account_id, body=body, timeout_in_minutes=timeout_in_minutes, allow_sync_on_push_complete=allow_sync_on_push_complete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountTransactionsApi->create_bank_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**object**](.md)|  | 
 **connection_id** | [**object**](.md)|  | 
 **account_id** | [**object**](.md)| Unique identifier for an account | 
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 
 **allow_sync_on_push_complete** | [**object**](.md)|  | [optional] [default to true]

### Return type

[**CreateBankTransactionsResponse**](CreateBankTransactionsResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_create_bank_account_model**
> PushOption get_create_bank_account_model(company_id, connection_id, account_id)

List push options for bank account bank transactions

Gets the options of pushing bank account transactions.

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
api_instance = swagger_client.BankAccountTransactionsApi(swagger_client.ApiClient(configuration))
company_id = NULL # object | 
connection_id = NULL # object | 
account_id = NULL # object | Unique identifier for an account

try:
    # List push options for bank account bank transactions
    api_response = api_instance.get_create_bank_account_model(company_id, connection_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountTransactionsApi->get_create_bank_account_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**object**](.md)|  | 
 **connection_id** | [**object**](.md)|  | 
 **account_id** | [**object**](.md)| Unique identifier for an account | 

### Return type

[**PushOption**](PushOption.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bank_account_transactions**
> BankTransactionsResponse list_bank_account_transactions(company_id, connection_id, account_id, page=page, page_size=page_size, query=query, order_by=order_by)

List bank transactions for bank account

Gets bank transactions for a given bank account ID

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
api_instance = swagger_client.BankAccountTransactionsApi(swagger_client.ApiClient(configuration))
company_id = NULL # object | 
connection_id = NULL # object | 
account_id = NULL # object | Unique identifier for an account
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List bank transactions for bank account
    api_response = api_instance.list_bank_account_transactions(company_id, connection_id, account_id, page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountTransactionsApi->list_bank_account_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**object**](.md)|  | 
 **connection_id** | [**object**](.md)|  | 
 **account_id** | [**object**](.md)| Unique identifier for an account | 
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**BankTransactionsResponse**](BankTransactionsResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bank_transactions**
> BankAccountTransactions list_bank_transactions(page=page, page_size=page_size, query=query, order_by=order_by)

List all bank transactions

Gets the latest bank transactions for given account ID and company. Doesn't require connection ID.

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
api_instance = swagger_client.BankAccountTransactionsApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List all bank transactions
    api_response = api_instance.list_bank_transactions(page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountTransactionsApi->list_bank_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**BankAccountTransactions**](BankAccountTransactions.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

