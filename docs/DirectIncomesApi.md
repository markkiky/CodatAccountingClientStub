# swagger_client.DirectIncomesApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_direct_income**](DirectIncomesApi.md#create_direct_income) | **POST** /companies/{companyId}/connections/{connectionId}/push/directIncomes | Create direct income
[**download_direct_income_attachment**](DirectIncomesApi.md#download_direct_income_attachment) | **GET** /companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId}/attachments/{attachmentId}/download | Download direct income attachment
[**get_create_direct_incomes_model**](DirectIncomesApi.md#get_create_direct_incomes_model) | **GET** /companies/{companyId}/connections/{connectionId}/options/directIncomes | Get create direct income model
[**get_direct_income**](DirectIncomesApi.md#get_direct_income) | **GET** /companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId} | Get direct income
[**get_direct_income_attachment**](DirectIncomesApi.md#get_direct_income_attachment) | **GET** /companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId}/attachments/{attachmentId} | Get direct income attachment
[**list_direct_income_attachments**](DirectIncomesApi.md#list_direct_income_attachments) | **GET** /companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId}/attachments | List direct income attachments
[**list_direct_incomes**](DirectIncomesApi.md#list_direct_incomes) | **GET** /companies/{companyId}/connections/{connectionId}/data/directIncomes | List direct incomes
[**upload_direct_income_attachment**](DirectIncomesApi.md#upload_direct_income_attachment) | **POST** /companies/{companyId}/connections/{connectionId}/push/directIncomes/{directIncomeId}/attachment | Create direct income attachment

# **create_direct_income**
> CreateDirectIncomeResponse create_direct_income(body=body, timeout_in_minutes=timeout_in_minutes)

Create direct income

Posts a new direct income to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call [Get create direct income model](https://docs.codat.io/accounting-api#/operations/get-create-directIncomes-model).  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) to see which integrations support this endpoint.

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
api_instance = swagger_client.DirectIncomesApi(swagger_client.ApiClient(configuration))
body = {
  "value" : {
    "note" : "test note",
    "contactRef" : {
      "id" : "80000002-1674552702",
      "dataType" : "string"
    },
    "issueDate" : "2023-02-01T16:27:40.023Z",
    "currency" : "USD",
    "lineItems" : [ {
      "description" : "line description 1",
      "unitAmount" : 9100,
      "quantity" : 68,
      "discountAmount" : 0,
      "discountPercentage" : 0,
      "subTotal" : 5320,
      "taxAmount" : 37,
      "totalAmount" : 12,
      "accountRef" : {
        "id" : "80000007-1671793811"
      },
      "trackingCategoryRefs" : [ {
        "id" : "80000002-1674553271",
        "name" : "string"
      } ]
    } ],
    "paymentAllocations" : [ {
      "payment" : {
        "id" : "3594002235",
        "note" : "payment allocations note",
        "reference" : "230202 1217",
        "accountRef" : {
          "id" : "80000028-1671794219"
        },
        "currency" : "USD",
        "currencyRate" : 1,
        "paidOnDate" : "2023-02-01T16:27:40.023Z",
        "totalAmount" : 560
      },
      "allocation" : {
        "currency" : "USD",
        "currencyRate" : 1,
        "allocatedOnDate" : "2023-02-01T16:27:40.023Z",
        "totalAmount" : 560
      }
    } ],
    "subTotal" : 0,
    "taxAmount" : 9999,
    "totalAmount" : 9999,
    "metadata" : {
      "isDeleted" : true
    }
  }
} # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)

try:
    # Create direct income
    api_response = api_instance.create_direct_income(body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectIncomesApi->create_direct_income: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 

### Return type

[**CreateDirectIncomeResponse**](CreateDirectIncomeResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_direct_income_attachment**
> object download_direct_income_attachment(attachment_id)

Download direct income attachment

Downloads an attachment for the specified direct income for a given company.

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
api_instance = swagger_client.DirectIncomesApi(swagger_client.ApiClient(configuration))
attachment_id = NULL # object | Unique identifier for an attachment

try:
    # Download direct income attachment
    api_response = api_instance.download_direct_income_attachment(attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectIncomesApi->download_direct_income_attachment: %s\n" % e)
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

# **get_create_direct_incomes_model**
> PushOption get_create_direct_incomes_model()

Get create direct income model

Get create direct income model. Returns the expected data for the request payload.  See the examples for integration-specific indicative models.  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support creating direct incomes.

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
api_instance = swagger_client.DirectIncomesApi(swagger_client.ApiClient(configuration))

try:
    # Get create direct income model
    api_response = api_instance.get_create_direct_incomes_model()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectIncomesApi->get_create_direct_incomes_model: %s\n" % e)
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

# **get_direct_income**
> DirectIncome get_direct_income(direct_income_id, company_id, connection_id)

Get direct income

Gets the specified direct income for a given company and connection.

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
api_instance = swagger_client.DirectIncomesApi(swagger_client.ApiClient(configuration))
direct_income_id = NULL # object | 
company_id = NULL # object | 
connection_id = NULL # object | 

try:
    # Get direct income
    api_response = api_instance.get_direct_income(direct_income_id, company_id, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectIncomesApi->get_direct_income: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direct_income_id** | [**object**](.md)|  | 
 **company_id** | [**object**](.md)|  | 
 **connection_id** | [**object**](.md)|  | 

### Return type

[**DirectIncome**](DirectIncome.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_direct_income_attachment**
> Attachment get_direct_income_attachment(timeout_in_minutes=timeout_in_minutes)

Get direct income attachment

Gets the specified direct income attachment for a given company.

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
api_instance = swagger_client.DirectIncomesApi(swagger_client.ApiClient(configuration))
timeout_in_minutes = NULL # object |  (optional)

try:
    # Get direct income attachment
    api_response = api_instance.get_direct_income_attachment(timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectIncomesApi->get_direct_income_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_direct_income_attachments**
> AttachmentsDataset list_direct_income_attachments()

List direct income attachments

Gets all attachments for the specified direct income for a given company.

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
api_instance = swagger_client.DirectIncomesApi(swagger_client.ApiClient(configuration))

try:
    # List direct income attachments
    api_response = api_instance.list_direct_income_attachments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectIncomesApi->list_direct_income_attachments: %s\n" % e)
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

# **list_direct_incomes**
> DirectIncomes list_direct_incomes(page=page, page_size=page_size, query=query, order_by=order_by)

List direct incomes

Lists the direct incomes for a given company.

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
api_instance = swagger_client.DirectIncomesApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List direct incomes
    api_response = api_instance.list_direct_incomes(page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectIncomesApi->list_direct_incomes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**DirectIncomes**](DirectIncomes.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_direct_income_attachment**
> upload_direct_income_attachment(direct_income_id, company_id, connection_id)

Create direct income attachment

Posts a new direct income attachment for a given company.

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
api_instance = swagger_client.DirectIncomesApi(swagger_client.ApiClient(configuration))
direct_income_id = NULL # object | 
company_id = NULL # object | 
connection_id = NULL # object | 

try:
    # Create direct income attachment
    api_instance.upload_direct_income_attachment(direct_income_id, company_id, connection_id)
except ApiException as e:
    print("Exception when calling DirectIncomesApi->upload_direct_income_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direct_income_id** | [**object**](.md)|  | 
 **company_id** | [**object**](.md)|  | 
 **connection_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

