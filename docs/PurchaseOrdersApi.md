# swagger_client.PurchaseOrdersApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_purchase_order**](PurchaseOrdersApi.md#create_purchase_order) | **POST** /companies/{companyId}/connections/{connectionId}/push/purchaseOrders | Create purchase order
[**get_create_update_purchase_orders_model**](PurchaseOrdersApi.md#get_create_update_purchase_orders_model) | **GET** /companies/{companyId}/connections/{connectionId}/options/purchaseOrders | Get create/update purchase order model
[**get_purchase_order**](PurchaseOrdersApi.md#get_purchase_order) | **GET** /companies/{companyId}/data/purchaseOrders/{purchaseOrderId} | Get purchase order
[**list_purchase_orders**](PurchaseOrdersApi.md#list_purchase_orders) | **GET** /companies/{companyId}/data/purchaseOrders | List purchase orders
[**update_purchase_order**](PurchaseOrdersApi.md#update_purchase_order) | **PUT** /companies/{companyId}/connections/{connectionId}/push/purchaseOrders/{purchaseOrderId} | Update purchase order

# **create_purchase_order**
> CreatePurchaseOrderResponse create_purchase_order(body=body, timeout_in_minutes=timeout_in_minutes)

Create purchase order

Posts a new purchase order to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call [Get create/update purchase order model](https://docs.codat.io/accounting-api#/operations/get-create-update-purchaseOrders-model).  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) to see which integrations support this endpoint.

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
api_instance = swagger_client.PurchaseOrdersApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)

try:
    # Create purchase order
    api_response = api_instance.create_purchase_order(body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->create_purchase_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 

### Return type

[**CreatePurchaseOrderResponse**](CreatePurchaseOrderResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_create_update_purchase_orders_model**
> PushOption get_create_update_purchase_orders_model()

Get create/update purchase order model

Get create/update purchase order model. Returns the expected data for the request payload.  See the examples for integration-specific indicative models.  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support creating and updating purchase orders.

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
api_instance = swagger_client.PurchaseOrdersApi(swagger_client.ApiClient(configuration))

try:
    # Get create/update purchase order model
    api_response = api_instance.get_create_update_purchase_orders_model()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->get_create_update_purchase_orders_model: %s\n" % e)
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

# **get_purchase_order**
> PurchaseOrder get_purchase_order(purchase_order_id, company_id)

Get purchase order

Get purchase order

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
api_instance = swagger_client.PurchaseOrdersApi(swagger_client.ApiClient(configuration))
purchase_order_id = NULL # object | 
company_id = NULL # object | 

try:
    # Get purchase order
    api_response = api_instance.get_purchase_order(purchase_order_id, company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->get_purchase_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_order_id** | [**object**](.md)|  | 
 **company_id** | [**object**](.md)|  | 

### Return type

[**PurchaseOrder**](PurchaseOrder.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_purchase_orders**
> PurchaseOrders list_purchase_orders(page=page, page_size=page_size, query=query, order_by=order_by)

List purchase orders

Get purchase orders

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
api_instance = swagger_client.PurchaseOrdersApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List purchase orders
    api_response = api_instance.list_purchase_orders(page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->list_purchase_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_purchase_order**
> UpdatePurchaseOrderResponse update_purchase_order(purchase_order_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)

Update purchase order

Posts an updated purchase order to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call []().  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support updating purchase orders.

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
api_instance = swagger_client.PurchaseOrdersApi(swagger_client.ApiClient(configuration))
purchase_order_id = NULL # object | 
body = NULL # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)
force_update = false # object | When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting platform, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check. (optional) (default to false)

try:
    # Update purchase order
    api_response = api_instance.update_purchase_order(purchase_order_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->update_purchase_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_order_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 
 **force_update** | [**object**](.md)| When updating data in the destination platform Codat checks the &#x60;sourceModifiedDate&#x60; against the &#x60;lastupdated&#x60; date from the accounting platform, if they&#x27;re different Codat will return an error suggesting you should initiate another pull of the data. If this is set to &#x60;true&#x60; then the update will override this check. | [optional] [default to false]

### Return type

[**UpdatePurchaseOrderResponse**](UpdatePurchaseOrderResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

