# swagger_client.CreditNotesApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credit_note**](CreditNotesApi.md#create_credit_note) | **POST** /companies/{companyId}/connections/{connectionId}/push/creditNotes | Create credit note
[**get_create_update_credit_notes_model**](CreditNotesApi.md#get_create_update_credit_notes_model) | **GET** /companies/{companyId}/connections/{connectionId}/options/creditNotes | Get create/update credit note model
[**get_credit_note**](CreditNotesApi.md#get_credit_note) | **GET** /companies/{companyId}/data/creditNotes/{creditNoteId} | Get credit note
[**list_credit_notes**](CreditNotesApi.md#list_credit_notes) | **GET** /companies/{companyId}/data/creditNotes | List credit notes
[**update_credit_note**](CreditNotesApi.md#update_credit_note) | **PUT** /companies/{companyId}/connections/{connectionId}/push/creditNotes/{creditNoteId} | Update creditNote

# **create_credit_note**
> CreateCreditNoteResponse create_credit_note(body=body, timeout_in_minutes=timeout_in_minutes)

Create credit note

Push credit note   Required data may vary by integration. To see what data to post, first call [Get create/update credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-creditNotes-model).  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) to see which integrations support this endpoint. 

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
api_instance = swagger_client.CreditNotesApi(swagger_client.ApiClient(configuration))
body = {
  "value" : {
    "creditNoteNumber" : "09/03 17.15",
    "note" : "credit note 20230309 17.15",
    "status" : "Submitted",
    "customerRef" : {
      "id" : "80000002-1674552702"
    },
    "currency" : "USD",
    "currencyRate" : 1,
    "subTotal" : 10.2,
    "issueDate" : "2023-03-09T02:21:26.726327+00:00",
    "lineItems" : [ {
      "itemRef" : {
        "id" : "80000004-1675280003",
        "name" : "test income item 1"
      },
      "quantity" : 1,
      "subTotal" : 1.25,
      "taxAmount" : 0,
      "unitAmount" : 1.25,
      "description" : "banana",
      "totalAmount" : 1.25
    } ],
    "totalAmount" : 1.25,
    "totalDiscount" : 0,
    "totalTaxAmount" : 0,
    "discountPercentage" : 0,
    "remainingCredit" : 0
  }
} # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)

try:
    # Create credit note
    api_response = api_instance.create_credit_note(body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->create_credit_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 

### Return type

[**CreateCreditNoteResponse**](CreateCreditNoteResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_create_update_credit_notes_model**
> PushOption get_create_update_credit_notes_model()

Get create/update credit note model

﻿Get create/update credit note model. Returns the expected data for the request payload.  See the examples for integration-specific indicative models.  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support creating and updating a credit note.

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
api_instance = swagger_client.CreditNotesApi(swagger_client.ApiClient(configuration))

try:
    # Get create/update credit note model
    api_response = api_instance.get_create_update_credit_notes_model()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->get_create_update_credit_notes_model: %s\n" % e)
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

# **get_credit_note**
> CreditNote get_credit_note()

Get credit note

﻿Gets a single creditNote corresponding to the given ID.

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
api_instance = swagger_client.CreditNotesApi(swagger_client.ApiClient(configuration))

try:
    # Get credit note
    api_response = api_instance.get_credit_note()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->get_credit_note: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CreditNote**](CreditNote.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credit_notes**
> CreditNotes list_credit_notes(page=page, page_size=page_size, query=query, order_by=order_by)

List credit notes

﻿Gets a list of all credit notes for a company, with pagination.

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
api_instance = swagger_client.CreditNotesApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List credit notes
    api_response = api_instance.list_credit_notes(page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->list_credit_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credit_note**
> UpdateCreditNoteResponse update_credit_note(credit_note_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)

Update creditNote

﻿Posts an updated credit note to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call [Get create/update credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-creditNotes-model).  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support updating a credit note.

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
api_instance = swagger_client.CreditNotesApi(swagger_client.ApiClient(configuration))
credit_note_id = NULL # object | 
body = NULL # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)
force_update = false # object | When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting platform, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check. (optional) (default to false)

try:
    # Update creditNote
    api_response = api_instance.update_credit_note(credit_note_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->update_credit_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 
 **force_update** | [**object**](.md)| When updating data in the destination platform Codat checks the &#x60;sourceModifiedDate&#x60; against the &#x60;lastupdated&#x60; date from the accounting platform, if they&#x27;re different Codat will return an error suggesting you should initiate another pull of the data. If this is set to &#x60;true&#x60; then the update will override this check. | [optional] [default to false]

### Return type

[**UpdateCreditNoteResponse**](UpdateCreditNoteResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

