# swagger_client.BillsApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bill**](BillsApi.md#create_bill) | **POST** /companies/{companyId}/connections/{connectionId}/push/bills | Create bill
[**delete_bill**](BillsApi.md#delete_bill) | **DELETE** /companies/{companyId}/connections/{connectionId}/push/bills/{billId} | Delete bill
[**download_bill_attachment**](BillsApi.md#download_bill_attachment) | **GET** /companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments/{attachmentId}/download | Download bill attachment
[**get_bill**](BillsApi.md#get_bill) | **GET** /companies/{companyId}/data/bills/{billId} | Get bill
[**get_bill_attachment**](BillsApi.md#get_bill_attachment) | **GET** /companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments/{attachmentId} | Get bill attachment
[**get_create_update_bills_model**](BillsApi.md#get_create_update_bills_model) | **GET** /companies/{companyId}/connections/{connectionId}/options/bills | Get create/update bill model
[**list_bill_attachments**](BillsApi.md#list_bill_attachments) | **GET** /companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments | List bill attachments
[**list_bills**](BillsApi.md#list_bills) | **GET** /companies/{companyId}/data/bills | List bills
[**update_bill**](BillsApi.md#update_bill) | **PUT** /companies/{companyId}/connections/{connectionId}/push/bills/{billId} | Update bill
[**upload_bill_attachment**](BillsApi.md#upload_bill_attachment) | **POST** /companies/{companyId}/connections/{connectionId}/push/bills/{billId}/attachments | Upload bill attachment

# **create_bill**
> CreateBillResponse create_bill(body=body, timeout_in_minutes=timeout_in_minutes)

Create bill

Posts a new bill to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call [Get create/update bill model](https://docs.codat.io/accounting-api#/operations/get-create-update-bills-model).  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) to see which integrations support this endpoint. 

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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))
body = {
  "value" : {
    "reference" : "20230308 15.16",
    "supplierRef" : {
      "id" : "80000001-1671793885",
      "supplierName" : "string"
    },
    "purchaseOrderRefs" : [ {
      "id" : "string",
      "purchaseOrderNumber" : "string"
    } ],
    "issueDate" : "2023-03-08T09:21:18.558Z",
    "dueDate" : "2023-03-14T09:21:18.558Z",
    "currency" : "USD",
    "currencyRate" : 1,
    "lineItems" : [ {
      "description" : "line 1 description",
      "unitAmount" : 1.625,
      "quantity" : 2,
      "discountAmount" : 0,
      "subTotal" : 3.25,
      "taxAmount" : 0,
      "totalAmount" : 3.25,
      "discountPercentage" : 0,
      "itemRef" : {
        "id" : "80000001-1674566705",
        "name" : "string"
      },
      "trackingCategoryRefs" : [ {
        "id" : "80000003-1674553958",
        "name" : "Class 2"
      } ],
      "tracking" : {
        "categoryRefs" : [ {
          "id" : "80000001-1674553252",
          "name" : "Class 1"
        } ],
        "customerRef" : {
          "id" : "80000002-1674552702",
          "companyName" : "string"
        },
        "projectRef" : {
          "id" : "string",
          "name" : "string"
        },
        "isBilledTo" : "Unknown",
        "isRebilledTo" : "Customer"
      },
      "isDirectCost" : true
    } ],
    "withholdingTax" : [ {
      "name" : "string",
      "amount" : 0
    } ],
    "status" : "Open",
    "subTotal" : 3.25,
    "taxAmount" : 0,
    "totalAmount" : 3.25,
    "amountDue" : 115.899999984,
    "note" : "note",
    "paymentAllocations" : [ ]
  }
} # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)

try:
    # Create bill
    api_response = api_instance.create_bill(body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->create_bill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 

### Return type

[**CreateBillResponse**](CreateBillResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bill**
> PushOperationSummary delete_bill()

Delete bill

﻿The _Delete Bills_ endpoint allows you to delete a specified Bill from an accounting platform.   ### Process  1. Pass the `{billId}` to the _Delete Bills_ endpoint and store the `pushOperationKey` returned. 2. Check the status of the delete operation by checking the status of push operation either via     1. [Push operation webhook](/introduction/webhooks/core-rules-types#push-operation-status-has-changed) (advised),     2. [Push operation status endpoint](https://docs.codat.io/codat-api#/operations/get-push-operation).     A `Success` status indicates that the Bill object was deleted from the accounting platform. 3. (Optional) Check that the Bill was deleted from the accounting platform.  ### Effect on related objects  Be aware that deleting a Bill from an accounting platform might cause related objects to be modified. For example, if you delete a paid Bill in QuickBooks Online, the bill is deleted but the bill payment against that bill is not. The bill payment is converted to a payment on account.  ## Integration specifics Integrations that support soft delete do not permanently delete the object in the accounting platform.  | Integration | Soft Delete | Details                                                                                                      |   |-------------|-------------|--------------------------------------------------------------------------------------------------------------| | QuickBooks Online | No          | -                                                                                                            | | Oracle NetSuite   | No          | When deleting a Bill that's already linked to a Bill payment, you must delete the linked Bill payment first. |  > **Supported Integrations** >  > This functionality is currently only supported for our QuickBooks Online abd Oracle NetSuite integrations. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.

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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))

try:
    # Delete bill
    api_response = api_instance.delete_bill()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->delete_bill: %s\n" % e)
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

# **download_bill_attachment**
> object download_bill_attachment(attachment_id)

Download bill attachment

﻿Download bill attachment.

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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))
attachment_id = NULL # object | Unique identifier for an attachment

try:
    # Download bill attachment
    api_response = api_instance.download_bill_attachment(attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->download_bill_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | [**object**](.md)| Unique identifier for an attachment | 

### Return type

**object**

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bill**
> Bill get_bill()

Get bill

﻿Get a bill.

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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))

try:
    # Get bill
    api_response = api_instance.get_bill()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->get_bill: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Bill**](Bill.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bill_attachment**
> Attachment get_bill_attachment(attachment_id)

Get bill attachment

﻿Get bill attachment.

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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))
attachment_id = NULL # object | Unique identifier for an attachment

try:
    # Get bill attachment
    api_response = api_instance.get_bill_attachment(attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->get_bill_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | [**object**](.md)| Unique identifier for an attachment | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_create_update_bills_model**
> PushOption get_create_update_bills_model()

Get create/update bill model

﻿Get create/update bill model.  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support creating and updating a bill.

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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))

try:
    # Get create/update bill model
    api_response = api_instance.get_create_update_bills_model()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->get_create_update_bills_model: %s\n" % e)
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

# **list_bill_attachments**
> AttachmentsDataset list_bill_attachments()

List bill attachments

﻿List bill attachments.

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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))

try:
    # List bill attachments
    api_response = api_instance.list_bill_attachments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->list_bill_attachments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AttachmentsDataset**](AttachmentsDataset.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bills**
> Bills list_bills(page=page, page_size=page_size, query=query, order_by=order_by)

List bills

﻿Gets the latest bills for a company, with pagination.

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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List bills
    api_response = api_instance.list_bills(page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->list_bills: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**Bills**](Bills.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bill**
> UpdateBillResponse update_bill(body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)

Update bill

﻿Posts an updated bill to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call [Get create/update bill model](https://docs.codat.io/accounting-api#/operations/get-create-update-bills-model).  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support updating a bill.

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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)
force_update = false # object | When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting platform, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check. (optional) (default to false)

try:
    # Update bill
    api_response = api_instance.update_bill(body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->update_bill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 
 **force_update** | [**object**](.md)| When updating data in the destination platform Codat checks the &#x60;sourceModifiedDate&#x60; against the &#x60;lastupdated&#x60; date from the accounting platform, if they&#x27;re different Codat will return an error suggesting you should initiate another pull of the data. If this is set to &#x60;true&#x60; then the update will override this check. | [optional] [default to false]

### Return type

[**UpdateBillResponse**](UpdateBillResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_bill_attachment**
> upload_bill_attachment()

Upload bill attachment

﻿Upload bill attachment.

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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))

try:
    # Upload bill attachment
    api_instance.upload_bill_attachment()
except ApiException as e:
    print("Exception when calling BillsApi->upload_bill_attachment: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

