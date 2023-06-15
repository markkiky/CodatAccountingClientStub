# swagger_client.SalesOrdersApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sales_order**](SalesOrdersApi.md#get_sales_order) | **GET** /companies/{companyId}/data/salesOrders/{salesOrderId} | Get sales order
[**list_sales_orders**](SalesOrdersApi.md#list_sales_orders) | **GET** /companies/{companyId}/data/salesOrders | List sales orders

# **get_sales_order**
> SalesOrder get_sales_order(sales_order_id, company_id)

Get sales order

Get sales order

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
api_instance = swagger_client.SalesOrdersApi(swagger_client.ApiClient(configuration))
sales_order_id = NULL # object | 
company_id = NULL # object | 

try:
    # Get sales order
    api_response = api_instance.get_sales_order(sales_order_id, company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesOrdersApi->get_sales_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_order_id** | [**object**](.md)|  | 
 **company_id** | [**object**](.md)|  | 

### Return type

[**SalesOrder**](SalesOrder.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sales_orders**
> SalesOrders list_sales_orders(page=page, page_size=page_size, query=query, order_by=order_by)

List sales orders

Get sales orders

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
api_instance = swagger_client.SalesOrdersApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List sales orders
    api_response = api_instance.list_sales_orders(page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesOrdersApi->list_sales_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**SalesOrders**](SalesOrders.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

