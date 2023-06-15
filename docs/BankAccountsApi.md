# swagger_client.BankAccountsApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bank_account**](BankAccountsApi.md#create_bank_account) | **POST** /companies/{companyId}/connections/{connectionId}/push/bankAccounts | Create bank account
[**get_all_bank_account**](BankAccountsApi.md#get_all_bank_account) | **GET** /companies/{companyId}/data/bankAccounts/{accountId} | Get bank account
[**get_bank_account**](BankAccountsApi.md#get_bank_account) | **GET** /companies/{companyId}/connections/{connectionId}/data/bankAccounts/{accountId} | Get bank account
[**get_create_update_bank_accounts_model**](BankAccountsApi.md#get_create_update_bank_accounts_model) | **GET** /companies/{companyId}/connections/{connectionId}/options/bankAccounts | Get create/update bank account model
[**list_bank_accounts**](BankAccountsApi.md#list_bank_accounts) | **GET** /companies/{companyId}/connections/{connectionId}/data/bankAccounts | List bank accounts
[**update_bank_account**](BankAccountsApi.md#update_bank_account) | **PUT** /companies/{companyId}/connections/{connectionId}/push/bankAccounts/{bankAccountId} | Update bank account

# **create_bank_account**
> CreateBankAccountResponse create_bank_account(body=body, allow_sync_on_push_complete=allow_sync_on_push_complete, timeout_in_minutes=timeout_in_minutes)

Create bank account

Posts a new bank account to the accounting package for a given company.    Required data may vary by integration. To see what data to post, first call [Get create/update bank account model](https://docs.codat.io/accounting-api#/operations/get-create-update-bankAccounts-model).    Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) to see which integrations support this endpoint.  

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
api_instance = swagger_client.BankAccountsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)
allow_sync_on_push_complete = true # object |  (optional) (default to true)
timeout_in_minutes = NULL # object |  (optional)

try:
    # Create bank account
    api_response = api_instance.create_bank_account(body=body, allow_sync_on_push_complete=allow_sync_on_push_complete, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountsApi->create_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **allow_sync_on_push_complete** | [**object**](.md)|  | [optional] [default to true]
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 

### Return type

[**CreateBankAccountResponse**](CreateBankAccountResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_bank_account**
> BankStatementAccount get_all_bank_account(query=query)

Get bank account

Gets the bank account for given account ID.

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
api_instance = swagger_client.BankAccountsApi(swagger_client.ApiClient(configuration))
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)

try:
    # Get bank account
    api_response = api_instance.get_all_bank_account(query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountsApi->get_all_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 

### Return type

[**BankStatementAccount**](BankStatementAccount.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_account**
> BankAccount get_bank_account()

Get bank account

Gets the bank account with a given ID

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
api_instance = swagger_client.BankAccountsApi(swagger_client.ApiClient(configuration))

try:
    # Get bank account
    api_response = api_instance.get_bank_account()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountsApi->get_bank_account: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_create_update_bank_accounts_model**
> PushOption get_create_update_bank_accounts_model()

Get create/update bank account model

Get create/update bank account model. Returns the expected data for the request payload.    See the examples for integration-specific indicative models.    > **Supported Integrations**  >   > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support creating and updating bank accounts.  

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
api_instance = swagger_client.BankAccountsApi(swagger_client.ApiClient(configuration))

try:
    # Get create/update bank account model
    api_response = api_instance.get_create_update_bank_accounts_model()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountsApi->get_create_update_bank_accounts_model: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PushOption**](PushOption.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bank_accounts**
> BankAccounts list_bank_accounts(page=page, page_size=page_size, query=query, order_by=order_by)

List bank accounts

Gets the list of bank accounts for a given connection

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
api_instance = swagger_client.BankAccountsApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List bank accounts
    api_response = api_instance.list_bank_accounts(page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountsApi->list_bank_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**BankAccounts**](BankAccounts.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bank_account**
> UpdateBankAccountResponse update_bank_account(body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)

Update bank account

Posts an updated bank account to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call []().  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support updating bank accounts.

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
api_instance = swagger_client.BankAccountsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)
force_update = false # object | When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting platform, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check. (optional) (default to false)

try:
    # Update bank account
    api_response = api_instance.update_bank_account(body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountsApi->update_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 
 **force_update** | [**object**](.md)| When updating data in the destination platform Codat checks the &#x60;sourceModifiedDate&#x60; against the &#x60;lastupdated&#x60; date from the accounting platform, if they&#x27;re different Codat will return an error suggesting you should initiate another pull of the data. If this is set to &#x60;true&#x60; then the update will override this check. | [optional] [default to false]

### Return type

[**UpdateBankAccountResponse**](UpdateBankAccountResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

