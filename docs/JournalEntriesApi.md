# swagger_client.JournalEntriesApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_journal_entry**](JournalEntriesApi.md#create_journal_entry) | **POST** /companies/{companyId}/connections/{connectionId}/push/journalEntries | Create journal entry
[**delete_journal_entry**](JournalEntriesApi.md#delete_journal_entry) | **DELETE** /companies/{companyId}/connections/{connectionId}/push/journalEntries/{journalEntryId} | Delete journal entry
[**get_create_journal_entries_model**](JournalEntriesApi.md#get_create_journal_entries_model) | **GET** /companies/{companyId}/connections/{connectionId}/options/journalEntries | Get create journal entry model
[**get_journal_entry**](JournalEntriesApi.md#get_journal_entry) | **GET** /companies/{companyId}/data/journalEntries/{journalEntryId} | Get journal entry
[**list_journal_entries**](JournalEntriesApi.md#list_journal_entries) | **GET** /companies/{companyId}/data/journalEntries | List journal entries

# **create_journal_entry**
> CreateJournalEntryResponse create_journal_entry(body=body, timeout_in_minutes=timeout_in_minutes)

Create journal entry

Posts a new journalEntry to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call [Get create journal entry model](https://docs.codat.io/accounting-api#/operations/get-create-journalEntries-model).  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries) to see which integrations support this endpoint. 

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
api_instance = swagger_client.JournalEntriesApi(swagger_client.ApiClient(configuration))
body = {
  "value" : {
    "description" : "record level description",
    "postedOn" : "2023-02-23T19:49:16.052Z",
    "createdOn" : "2023-02-22T19:49:16.052Z",
    "updatedOn" : "2023-02-21T19:49:16.052Z",
    "journalRef" : {
      "id" : "12"
    },
    "journalLines" : [ {
      "description" : "journalLines.description debit",
      "netAmount" : 23.02,
      "currency" : "USD",
      "accountRef" : {
        "id" : "80000019-1671793811",
        "name" : "Office Supplies"
      },
      "tracking" : {
        "recordRefs" : [ {
          "id" : "80000001-1674553252",
          "dataType" : "string"
        } ]
      }
    }, {
      "description" : "journalLines.description credit",
      "netAmount" : -23.02,
      "currency" : "USD",
      "accountRef" : {
        "id" : "8000001E-1671793811",
        "name" : "Utilities"
      },
      "tracking" : {
        "recordRefs" : [ {
          "id" : "80000002-1674553271",
          "dataType" : "trackingCategories"
        } ]
      }
    } ],
    "recordRef" : {
      "id" : "string",
      "dataType" : "string"
    },
    "metadata" : {
      "isDeleted" : true
    }
  }
} # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)

try:
    # Create journal entry
    api_response = api_instance.create_journal_entry(body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalEntriesApi->create_journal_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 

### Return type

[**CreateJournalEntryResponse**](CreateJournalEntryResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_journal_entry**
> PushOperationSummary delete_journal_entry()

Delete journal entry

﻿> **Use with caution** > >Because Journal Entries underpin every transaction in an accounting platform, deleting a Journal Entry can affect every transaction for a given company. >  > **Before you proceed, make sure you understand the implications of deleting Journal Entries from an accounting perspective.**  The _Delete Journal entries_ endpoint allows you to delete a specified Journal entry from an accounting platform.  ### Process 1. Pass the `{journalEntryId}` to the _Delete Journal Entries_ endpoint and store the `pushOperationKey` returned. 2. Check the status of the delete by checking the status of push operation either via    1. [Push operation webhook](/introduction/webhooks/core-rules-types#push-operation-status-has-changed) (advised),    2. [Push operation status endpoint](https://docs.codat.io/codat-api#/operations/get-push-operation).         A `Success` status indicates that the Journal Entry object was deleted from the accounting platform. 3. (Optional) Check that the Journal Entry was deleted from the accounting platform.  ### Effect on related objects  Be aware that deleting a Journal Entry from an accounting platform might cause related objects to be modified. For example, if you delete the Journal Entry for a paid invoice in QuickBooks Online, the invoice is deleted but the payment against that invoice is not. The payment is converted to a payment on account.  ## Integration specifics Integrations that support soft delete do not permanently delete the object in the accounting platform.  | Integration | Soft Deleted |  |-------------|--------------| | QuickBooks Online | Yes    |         > **Supported Integrations** >  > This functionality is currently only supported for our QuickBooks Online integration. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.

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
api_instance = swagger_client.JournalEntriesApi(swagger_client.ApiClient(configuration))

try:
    # Delete journal entry
    api_response = api_instance.delete_journal_entry()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalEntriesApi->delete_journal_entry: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PushOperationSummary**](PushOperationSummary.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_create_journal_entries_model**
> PushOption get_create_journal_entries_model()

Get create journal entry model

﻿Get create journal entry model. Returns the expected data for the request payload.  See the examples for integration-specific indicative models.  > **Supported Integrations** >  > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries) for integrations that support creating journal entries.

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
api_instance = swagger_client.JournalEntriesApi(swagger_client.ApiClient(configuration))

try:
    # Get create journal entry model
    api_response = api_instance.get_create_journal_entries_model()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalEntriesApi->get_create_journal_entries_model: %s\n" % e)
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

# **get_journal_entry**
> JournalEntry get_journal_entry(journal_entry_id, company_id)

Get journal entry

Gets a single JournalEntry corresponding to the given ID.

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
api_instance = swagger_client.JournalEntriesApi(swagger_client.ApiClient(configuration))
journal_entry_id = NULL # object | 
company_id = NULL # object | 

try:
    # Get journal entry
    api_response = api_instance.get_journal_entry(journal_entry_id, company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalEntriesApi->get_journal_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_entry_id** | [**object**](.md)|  | 
 **company_id** | [**object**](.md)|  | 

### Return type

[**JournalEntry**](JournalEntry.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_journal_entries**
> JournalEntries list_journal_entries(page=page, page_size=page_size, query=query, order_by=order_by)

List journal entries

﻿Gets the latest journal entries for a company, with pagination.

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
api_instance = swagger_client.JournalEntriesApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List journal entries
    api_response = api_instance.list_journal_entries(page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalEntriesApi->list_journal_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**JournalEntries**](JournalEntries.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

