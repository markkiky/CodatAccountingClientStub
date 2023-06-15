# swagger_client.BillPaymentsApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bill_payment**](BillPaymentsApi.md#create_bill_payment) | **POST** /companies/{companyId}/connections/{connectionId}/push/billPayments | Create bill payments
[**delete_bill_payment**](BillPaymentsApi.md#delete_bill_payment) | **DELETE** /companies/{companyId}/connections/{connectionId}/push/billPayments/{billPaymentId} | Delete bill payment
[**get_bill_payments**](BillPaymentsApi.md#get_bill_payments) | **GET** /companies/{companyId}/data/billPayments/{billPaymentId} | Get bill payment
[**get_create_bill_payments_model**](BillPaymentsApi.md#get_create_bill_payments_model) | **GET** /companies/{companyId}/connections/{connectionId}/options/billPayments | Get create bill payment model
[**list_bill_payments**](BillPaymentsApi.md#list_bill_payments) | **GET** /companies/{companyId}/data/billPayments | List bill payments

# **create_bill_payment**
> CreateBillPaymentResponse create_bill_payment(body=body, timeout_in_minutes=timeout_in_minutes)

Create bill payments

Posts a new bill payment to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call [Get create bill payment model](https://docs.codat.io/accounting-api#/operations/get-create-billPayments-model).  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) to see which integrations support this endpoint. 

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
api_instance = swagger_client.BillPaymentsApi(swagger_client.ApiClient(configuration))
body = {
  "value" : {
    "supplierRef" : {
      "id" : "SUPP1",
      "supplierName" : "string"
    },
    "accountRef" : {
      "id" : "1200",
      "name" : "string"
    },
    "totalAmount" : 15.38,
    "currency" : "GBP",
    "currencyRate" : 1,
    "date" : "2023-01-05T12:33:25.339Z",
    "note" : "note - billpayment on 20230220 of 15.38",
    "paymentMethodRef" : {
      "id" : "string",
      "name" : "string"
    },
    "lines" : [ {
      "amount" : 15.38,
      "links" : [ {
        "type" : "Bill",
        "id" : "3",
        "amount" : -15.38,
        "currencyRate" : 1
      } ],
      "allocatedOnDate" : "2023-01-05T12:33:25.339Z"
    } ],
    "modifiedDate" : "2023-01-05T12:33:25.339Z",
    "sourceModifiedDate" : "2023-01-05T12:33:25.339Z",
    "reference" : "reference 20230220 15.38",
    "metadata" : {
      "isDeleted" : true
    }
  }
} # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)

try:
    # Create bill payments
    api_response = api_instance.create_bill_payment(body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillPaymentsApi->create_bill_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 

### Return type

[**CreateBillPaymentResponse**](CreateBillPaymentResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bill_payment**
> PushOperationSummary delete_bill_payment()

Delete bill payment

﻿The _Delete Bill Payments_ endpoint allows you to delete a specified Bill Payment from an accounting platform.  ### Process 1. Pass the `{billPaymentId}` to the _Delete Bill Payments_ endpoint and store the `pushOperationKey` returned. 2. Check the status of the delete operation by checking the status of push operation either via     1. [Push operation webhook](/introduction/webhooks/core-rules-types#push-operation-status-has-changed) (advised),     2. [Push operation status endpoint](https://docs.codat.io/codat-api#/operations/get-push-operation).     A `Success` status indicates that the Bill Payment object was deleted from the accounting platform. 3. (Optional) Check that the Bill Payment was deleted from the accounting platform.  ### Effect on related objects Be aware that deleting a Bill Payment from an accounting platform might cause related objects to be modified.  ## Integration specifics Integrations that support soft delete do not permanently delete the object in the accounting platform.  | Integration | Soft Delete | Details                                                                                             |   |-------------|-------------|-----------------------------------------------------------------------------------------------------| | Oracle NetSuite   | No          | See [here](/integrations/accounting/netsuite/how-deleting-bill-payments-works) to learn more. |  > **Supported Integrations** > > This functionality is currently only supported for our QuickBooks Online abd Oracle NetSuite integrations. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.

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
api_instance = swagger_client.BillPaymentsApi(swagger_client.ApiClient(configuration))

try:
    # Delete bill payment
    api_response = api_instance.delete_bill_payment()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillPaymentsApi->delete_bill_payment: %s\n" % e)
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

# **get_bill_payments**
> BillPayment get_bill_payments()

Get bill payment

﻿Get a bill payment.

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
api_instance = swagger_client.BillPaymentsApi(swagger_client.ApiClient(configuration))

try:
    # Get bill payment
    api_response = api_instance.get_bill_payments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillPaymentsApi->get_bill_payments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BillPayment**](BillPayment.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_create_bill_payments_model**
> PushOption get_create_bill_payments_model()

Get create bill payment model

﻿Get create bill payment model.  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support creating and deleting bill payments.

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
api_instance = swagger_client.BillPaymentsApi(swagger_client.ApiClient(configuration))

try:
    # Get create bill payment model
    api_response = api_instance.get_create_bill_payments_model()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillPaymentsApi->get_create_bill_payments_model: %s\n" % e)
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

# **list_bill_payments**
> BillPayments list_bill_payments(page=page, page_size=page_size, query=query, order_by=order_by)

List bill payments

﻿Gets the latest billPayments for a company, with pagination.

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
api_instance = swagger_client.BillPaymentsApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List bill payments
    api_response = api_instance.list_bill_payments(page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillPaymentsApi->list_bill_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**BillPayments**](BillPayments.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

