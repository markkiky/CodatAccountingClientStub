# swagger_client.DirectCostsApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_direct_cost**](DirectCostsApi.md#create_direct_cost) | **POST** /companies/{companyId}/connections/{connectionId}/push/directCosts | Create direct cost
[**download_direct_cost_attachment**](DirectCostsApi.md#download_direct_cost_attachment) | **GET** /companies/{companyId}/connections/{connectionId}/data/directCosts/{directCostId}/attachments/{attachmentId}/download | Download direct cost attachment
[**get_create_direct_costs_model**](DirectCostsApi.md#get_create_direct_costs_model) | **GET** /companies/{companyId}/connections/{connectionId}/options/directCosts | Get create direct cost model
[**get_direct_cost**](DirectCostsApi.md#get_direct_cost) | **GET** /companies/{companyId}/connections/{connectionId}/data/directCosts/{directCostId} | Get direct cost
[**get_direct_cost_attachment**](DirectCostsApi.md#get_direct_cost_attachment) | **GET** /companies/{companyId}/connections/{connectionId}/data/directCosts/{directCostId}/attachments/{attachmentId} | Get direct cost attachment
[**list_direct_cost_attachments**](DirectCostsApi.md#list_direct_cost_attachments) | **GET** /companies/{companyId}/connections/{connectionId}/data/directCosts/{directCostId}/attachments | List direct cost attachments
[**list_direct_costs**](DirectCostsApi.md#list_direct_costs) | **GET** /companies/{companyId}/connections/{connectionId}/data/directCosts | List direct costs
[**upload_direct_cost_attachment**](DirectCostsApi.md#upload_direct_cost_attachment) | **POST** /companies/{companyId}/connections/{connectionId}/push/directCosts/{directCostId}/attachment | Upload direct cost attachment

# **create_direct_cost**
> CreateDirectCostResponse create_direct_cost(body=body, timeout_in_minutes=timeout_in_minutes)

Create direct cost

Posts a new direct cost to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call [Get create direct cost model](https://docs.codat.io/accounting-api#/operations/get-create-directCosts-model).  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) to see which integrations support this endpoint.

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
api_instance = swagger_client.DirectCostsApi(swagger_client.ApiClient(configuration))
body = {
  "value" : {
    "reference" : "test ref",
    "note" : "directCost 21/03 09.20",
    "contactRef" : {
      "id" : "80000001-1671793885",
      "dataType" : "Test Vendor 1"
    },
    "issueDate" : "2023-03-21T10:19:52.223Z",
    "currency" : "USD",
    "lineItems" : [ {
      "description" : "test description line 1",
      "unitAmount" : 7,
      "quantity" : 1,
      "discountAmount" : 0,
      "discountPercentage" : 0,
      "subTotal" : 99,
      "taxAmount" : 360,
      "totalAmount" : 70,
      "accountRef" : {
        "id" : "8000000D-1671793811",
        "name" : "Purchases - Hardware for Resale"
      },
      "itemRef" : {
        "id" : "80000001-1674566705",
        "name" : "item test"
      },
      "trackingCategoryRefs" : [ {
        "id" : "80000001-1674553252",
        "name" : "Class 1"
      } ]
    } ],
    "paymentAllocations" : [ {
      "payment" : {
        "note" : "payment allocations note",
        "reference" : "payment allocations reference",
        "accountRef" : {
          "id" : "80000028-1671794219",
          "name" : "Bank Account 1"
        },
        "paidOnDate" : "2023-01-28T10:19:52.223Z",
        "totalAmount" : 54
      },
      "allocation" : {
        "currencyRate" : 0,
        "allocatedOnDate" : "2023-01-29T10:19:52.223Z",
        "totalAmount" : 88
      }
    } ],
    "subTotal" : 362,
    "taxAmount" : 4,
    "totalAmount" : 366
  }
} # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)

try:
    # Create direct cost
    api_response = api_instance.create_direct_cost(body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectCostsApi->create_direct_cost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 

### Return type

[**CreateDirectCostResponse**](CreateDirectCostResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_direct_cost_attachment**
> object download_direct_cost_attachment(attachment_id)

Download direct cost attachment

Downloads an attachment for the specified direct cost for a given company.

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
api_instance = swagger_client.DirectCostsApi(swagger_client.ApiClient(configuration))
attachment_id = NULL # object | Unique identifier for an attachment

try:
    # Download direct cost attachment
    api_response = api_instance.download_direct_cost_attachment(attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectCostsApi->download_direct_cost_attachment: %s\n" % e)
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

# **get_create_direct_costs_model**
> PushOption get_create_direct_costs_model()

Get create direct cost model

Get create direct cost model. Returns the expected data for the request payload.  See the examples for integration-specific indicative models.  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support creating direct costs.

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
api_instance = swagger_client.DirectCostsApi(swagger_client.ApiClient(configuration))

try:
    # Get create direct cost model
    api_response = api_instance.get_create_direct_costs_model()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectCostsApi->get_create_direct_costs_model: %s\n" % e)
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

# **get_direct_cost**
> DirectCost get_direct_cost()

Get direct cost

Gets the specified direct cost for a given company.

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
api_instance = swagger_client.DirectCostsApi(swagger_client.ApiClient(configuration))

try:
    # Get direct cost
    api_response = api_instance.get_direct_cost()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectCostsApi->get_direct_cost: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DirectCost**](DirectCost.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_direct_cost_attachment**
> Attachment get_direct_cost_attachment(attachment_id)

Get direct cost attachment

Gets the specified direct cost attachment for a given company.

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
api_instance = swagger_client.DirectCostsApi(swagger_client.ApiClient(configuration))
attachment_id = NULL # object | Unique identifier for an attachment

try:
    # Get direct cost attachment
    api_response = api_instance.get_direct_cost_attachment(attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectCostsApi->get_direct_cost_attachment: %s\n" % e)
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

# **list_direct_cost_attachments**
> AttachmentsDataset list_direct_cost_attachments()

List direct cost attachments

Gets all attachments for the specified direct cost for a given company.

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
api_instance = swagger_client.DirectCostsApi(swagger_client.ApiClient(configuration))

try:
    # List direct cost attachments
    api_response = api_instance.list_direct_cost_attachments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectCostsApi->list_direct_cost_attachments: %s\n" % e)
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

# **list_direct_costs**
> DirectCosts list_direct_costs(page=page, page_size=page_size, query=query, order_by=order_by)

List direct costs

Gets the direct costs for the company.

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
api_instance = swagger_client.DirectCostsApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List direct costs
    api_response = api_instance.list_direct_costs(page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectCostsApi->list_direct_costs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**DirectCosts**](DirectCosts.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_direct_cost_attachment**
> upload_direct_cost_attachment()

Upload direct cost attachment

Posts a new direct cost attachment for a given company.

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
api_instance = swagger_client.DirectCostsApi(swagger_client.ApiClient(configuration))

try:
    # Upload direct cost attachment
    api_instance.upload_direct_cost_attachment()
except ApiException as e:
    print("Exception when calling DirectCostsApi->upload_direct_cost_attachment: %s\n" % e)
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

