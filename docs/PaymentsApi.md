# swagger_client.PaymentsApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment**](PaymentsApi.md#create_payment) | **POST** /companies/{companyId}/connections/{connectionId}/push/payments | Create payment
[**get_create_payments_model**](PaymentsApi.md#get_create_payments_model) | **GET** /companies/{companyId}/connections/{connectionId}/options/payments | Get create payment model
[**get_payment**](PaymentsApi.md#get_payment) | **GET** /companies/{companyId}/data/payments/{paymentId} | Get payment
[**list_payments**](PaymentsApi.md#list_payments) | **GET** /companies/{companyId}/data/payments | List payments

# **create_payment**
> CreatePaymentResponse create_payment(body=body, timeout_in_minutes=timeout_in_minutes)

Create payment

Posts a new payment to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call [Get create payment model](https://docs.codat.io/accounting-api#/operations/get-create-payments-model).  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments) to see which integrations support this endpoint.

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
body = {
  "value" : {
    "customerRef" : {
      "id" : "80000002-1674552702",
      "companyName" : "string"
    },
    "accountRef" : {
      "id" : "8000002E-1675267199",
      "name" : "Undeposited Funds"
    },
    "paymentMethodRef" : {
      "id" : "string",
      "name" : "string"
    },
    "totalAmount" : 28,
    "currency" : "USD",
    "currencyRate" : 1,
    "date" : "2023-02-10T11:47:04.792Z",
    "note" : "note 14/02 1147",
    "lines" : [ {
      "amount" : 28,
      "links" : [ {
        "type" : "Invoice",
        "id" : "181-1676374586",
        "amount" : -28,
        "currencyRate" : 1
      } ],
      "allocatedOnDate" : "2023-02-11T11:47:04.792Z"
    } ],
    "reference" : "ref 14/02 1147"
  }
} # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)

try:
    # Create payment
    api_response = api_instance.create_payment(body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->create_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 

### Return type

[**CreatePaymentResponse**](CreatePaymentResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_create_payments_model**
> PushOption get_create_payments_model()

Get create payment model

Get create payment model. Returns the expected data for the request payload.  See the examples for integration-specific indicative models.  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments) for integrations that support creating payments.

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))

try:
    # Get create payment model
    api_response = api_instance.get_create_payments_model()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_create_payments_model: %s\n" % e)
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

# **get_payment**
> Payment get_payment(payment_id, company_id)

Get payment

Get payment

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
payment_id = NULL # object | 
company_id = NULL # object | 

try:
    # Get payment
    api_response = api_instance.get_payment(payment_id, company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**object**](.md)|  | 
 **company_id** | [**object**](.md)|  | 

### Return type

[**Payment**](Payment.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payments**
> Payments list_payments(page=page, page_size=page_size, query=query, order_by=order_by)

List payments

Gets the latest payments for a company, with pagination

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List payments
    api_response = api_instance.list_payments(page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->list_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**Payments**](Payments.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

