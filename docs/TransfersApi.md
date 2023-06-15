# swagger_client.TransfersApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transfer**](TransfersApi.md#create_transfer) | **POST** /companies/{companyId}/connections/{connectionId}/push/transfers | Create transfer
[**get_create_transfers_model**](TransfersApi.md#get_create_transfers_model) | **GET** /companies/{companyId}/connections/{connectionId}/options/transfers | Get create transfer model
[**get_transfer**](TransfersApi.md#get_transfer) | **GET** /companies/{companyId}/connections/{connectionId}/data/transfers/{transferId} | Get transfer
[**list_transfers**](TransfersApi.md#list_transfers) | **GET** /companies/{companyId}/connections/{connectionId}/data/transfers | List transfers

# **create_transfer**
> CreateTransferResponse create_transfer(body=body)

Create transfer

Posts a new transfer to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call [Get create transfer model](https://docs.codat.io/accounting-api#/operations/get-create-transfers-model).  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=transfers) to see which integrations support this endpoint.

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
api_instance = swagger_client.TransfersApi(swagger_client.ApiClient(configuration))
body = {
  "value" : {
    "description" : "test transfers push 20230126 12.08",
    "contactRef" : {
      "id" : "string",
      "dataType" : "string"
    },
    "date" : "2023-01-26T11:51:18.104Z",
    "from" : {
      "accountRef" : {
        "id" : "80000028-1671794219",
        "dataType" : "bankAccounts"
      },
      "amount" : 12
    },
    "to" : {
      "accountRef" : {
        "id" : "80000004-1671793811",
        "dataType" : "bankAccounts"
      },
      "amount" : 12
    },
    "trackingCategoryRefs" : [ {
      "id" : "80000001-1674553252",
      "name" : "Class 1"
    } ],
    "metadata" : {
      "isDeleted" : true
    }
  }
} # object |  (optional)

try:
    # Create transfer
    api_response = api_instance.create_transfer(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->create_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**CreateTransferResponse**](CreateTransferResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_create_transfers_model**
> PushOption get_create_transfers_model()

Get create transfer model

Get create transfer model. Returns the expected data for the request payload.  See the examples for integration-specific indicative models.  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=transfers) for integrations that support creating transfers.

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
api_instance = swagger_client.TransfersApi(swagger_client.ApiClient(configuration))

try:
    # Get create transfer model
    api_response = api_instance.get_create_transfers_model()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->get_create_transfers_model: %s\n" % e)
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

# **get_transfer**
> Transfer get_transfer()

Get transfer

Gets the specified transfer for a given company.

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
api_instance = swagger_client.TransfersApi(swagger_client.ApiClient(configuration))

try:
    # Get transfer
    api_response = api_instance.get_transfer()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->get_transfer: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Transfer**](Transfer.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transfers**
> Transfers list_transfers(page=page, page_size=page_size, query=query, order_by=order_by)

List transfers

Gets the transfers for a given company.

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
api_instance = swagger_client.TransfersApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List transfers
    api_response = api_instance.list_transfers(page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->list_transfers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**Transfers**](Transfers.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

