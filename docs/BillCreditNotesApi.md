# swagger_client.BillCreditNotesApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bill_credit_note**](BillCreditNotesApi.md#create_bill_credit_note) | **POST** /companies/{companyId}/connections/{connectionId}/push/billCreditNotes | Create bill credit note
[**get_bill_credit_note**](BillCreditNotesApi.md#get_bill_credit_note) | **GET** /companies/{companyId}/data/billCreditNotes/{billCreditNoteId} | Get bill credit note
[**get_create_update_bill_credit_notes_model**](BillCreditNotesApi.md#get_create_update_bill_credit_notes_model) | **GET** /companies/{companyId}/connections/{connectionId}/options/billCreditNotes | Get create/update bill credit note model
[**list_bill_credit_notes**](BillCreditNotesApi.md#list_bill_credit_notes) | **GET** /companies/{companyId}/data/billCreditNotes | List bill credit notes
[**update_bill_credit_note**](BillCreditNotesApi.md#update_bill_credit_note) | **PUT** /companies/{companyId}/connections/{connectionId}/push/billCreditNotes/{billCreditNoteId} | Update bill credit note

# **create_bill_credit_note**
> CreateBillCreditNoteResponse create_bill_credit_note(body=body, timeout_in_minutes=timeout_in_minutes)

Create bill credit note

Posts a new billCreditNote to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-billCreditNotes-model).  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) to see which integrations support this endpoint. 

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
api_instance = swagger_client.BillCreditNotesApi(swagger_client.ApiClient(configuration))
body = {
  "value" : {
    "billCreditNoteNumber" : "309",
    "supplierRef" : {
      "id" : "87",
      "supplierName" : "Ankunding Inc"
    },
    "withholdingTax" : [ ],
    "totalAmount" : 100,
    "totalDiscount" : 0,
    "subTotal" : 100,
    "totalTaxAmount" : 0,
    "discountPercentage" : 0,
    "remainingCredit" : 100,
    "status" : "Submitted",
    "issueDate" : "2023-04-20T00:00:00",
    "currency" : "GBP",
    "currencyRate" : 1.242097,
    "lineItems" : [ {
      "description" : "",
      "unitAmount" : 100,
      "quantity" : 1,
      "subTotal" : 100,
      "taxAmount" : 0,
      "totalAmount" : 100,
      "accountRef" : {
        "id" : "7"
      },
      "taxRateRef" : {
        "id" : "NON",
        "name" : "NON",
        "effectiveTaxRate" : 0
      },
      "trackingCategoryRefs" : [ ],
      "tracking" : {
        "categoryRefs" : [ ],
        "isBilledTo" : "Unknown",
        "isRebilledTo" : "NotApplicable"
      }
    } ]
  }
} # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)

try:
    # Create bill credit note
    api_response = api_instance.create_bill_credit_note(body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillCreditNotesApi->create_bill_credit_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 

### Return type

[**CreateBillCreditNoteResponse**](CreateBillCreditNoteResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bill_credit_note**
> BillCreditNote get_bill_credit_note()

Get bill credit note

﻿Gets a single billCreditNote corresponding to the given ID.

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
api_instance = swagger_client.BillCreditNotesApi(swagger_client.ApiClient(configuration))

try:
    # Get bill credit note
    api_response = api_instance.get_bill_credit_note()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillCreditNotesApi->get_bill_credit_note: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BillCreditNote**](BillCreditNote.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_create_update_bill_credit_notes_model**
> PushOption get_create_update_bill_credit_notes_model()

Get create/update bill credit note model

﻿Get create/update bill credit note model.  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating and updating bill credit notes.

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
api_instance = swagger_client.BillCreditNotesApi(swagger_client.ApiClient(configuration))

try:
    # Get create/update bill credit note model
    api_response = api_instance.get_create_update_bill_credit_notes_model()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillCreditNotesApi->get_create_update_bill_credit_notes_model: %s\n" % e)
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

# **list_bill_credit_notes**
> BillCreditNotes list_bill_credit_notes(page=page, page_size=page_size, query=query, order_by=order_by)

List bill credit notes

﻿Gets a list of all bill credit notes for a company, with pagination.

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
api_instance = swagger_client.BillCreditNotesApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List bill credit notes
    api_response = api_instance.list_bill_credit_notes(page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillCreditNotesApi->list_bill_credit_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**BillCreditNotes**](BillCreditNotes.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bill_credit_note**
> UpdateBillCreditNoteResponse update_bill_credit_note(bill_credit_note_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)

Update bill credit note

﻿Posts an updated billCreditNote to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-billCreditNotes-model).  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support updating bill credit notes.

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
api_instance = swagger_client.BillCreditNotesApi(swagger_client.ApiClient(configuration))
bill_credit_note_id = NULL # object | 
body = NULL # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)
force_update = false # object | When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting platform, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check. (optional) (default to false)

try:
    # Update bill credit note
    api_response = api_instance.update_bill_credit_note(bill_credit_note_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillCreditNotesApi->update_bill_credit_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_credit_note_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 
 **force_update** | [**object**](.md)| When updating data in the destination platform Codat checks the &#x60;sourceModifiedDate&#x60; against the &#x60;lastupdated&#x60; date from the accounting platform, if they&#x27;re different Codat will return an error suggesting you should initiate another pull of the data. If this is set to &#x60;true&#x60; then the update will override this check. | [optional] [default to false]

### Return type

[**UpdateBillCreditNoteResponse**](UpdateBillCreditNoteResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

