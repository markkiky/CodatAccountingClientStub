# swagger_client.CustomersApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer**](CustomersApi.md#create_customer) | **POST** /companies/{companyId}/connections/{connectionId}/push/customers | Create customer
[**download_customer_attachment**](CustomersApi.md#download_customer_attachment) | **GET** /companies/{companyId}/connections/{connectionId}/data/customers/{customerId}/attachments/{attachmentId}/download | Download customer attachment
[**get_create_update_customers_model**](CustomersApi.md#get_create_update_customers_model) | **GET** /companies/{companyId}/connections/{connectionId}/options/customers | Get create/update customer model
[**get_customer**](CustomersApi.md#get_customer) | **GET** /companies/{companyId}/data/customers/{customerId} | Get customer
[**get_customer_attachment**](CustomersApi.md#get_customer_attachment) | **GET** /companies/{companyId}/connections/{connectionId}/data/customers/{customerId}/attachments/{attachmentId} | Get customer attachment
[**list_customer_attachments**](CustomersApi.md#list_customer_attachments) | **GET** /companies/{companyId}/connections/{connectionId}/data/customers/{customerId}/attachments | List customer attachments
[**list_customers**](CustomersApi.md#list_customers) | **GET** /companies/{companyId}/data/customers | List customers
[**update_customer**](CustomersApi.md#update_customer) | **PUT** /companies/{companyId}/connections/{connectionId}/push/customers/{customerId} | Update customer

# **create_customer**
> CreateCustomerResponse create_customer(body=body, timeout_in_minutes=timeout_in_minutes)

Create customer

Posts an individual customer for a given company.  Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) to see which integrations support this endpoint. 

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)

try:
    # Create customer
    api_response = api_instance.create_customer(body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 

### Return type

[**CreateCustomerResponse**](CreateCustomerResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_customer_attachment**
> object download_customer_attachment()

Download customer attachment

﻿Download customer attachment.

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))

try:
    # Download customer attachment
    api_response = api_instance.download_customer_attachment()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->download_customer_attachment: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_create_update_customers_model**
> PushOption get_create_update_customers_model()

Get create/update customer model

﻿Get create/update customer model. Returns the expected data for the request payload.  See the examples for integration-specific indicative models.  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating and updating customers.

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))

try:
    # Get create/update customer model
    api_response = api_instance.get_create_update_customers_model()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_create_update_customers_model: %s\n" % e)
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

# **get_customer**
> Customer get_customer()

Get customer

﻿Gets a single customer corresponding to the given ID.

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))

try:
    # Get customer
    api_response = api_instance.get_customer()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Customer**](Customer.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_attachment**
> Attachment get_customer_attachment()

Get customer attachment

﻿Get  customer attachment.

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))

try:
    # Get customer attachment
    api_response = api_instance.get_customer_attachment()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_attachment: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Attachment**](Attachment.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_attachments**
> AttachmentsDataset list_customer_attachments()

List customer attachments

﻿List customer attachments

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))

try:
    # List customer attachments
    api_response = api_instance.list_customer_attachments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_customer_attachments: %s\n" % e)
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

# **list_customers**
> Customers list_customers(page=page, page_size=page_size, query=query, order_by=order_by)

List customers

﻿Gets the latest customers for a company, with pagination.

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List customers
    api_response = api_instance.list_customers(page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**Customers**](Customers.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer**
> UpdateCustomerResponse update_customer(customer_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)

Update customer

﻿Posts an updated customer for a given company.  Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).  > **Supported Integrations** >  > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support updating customers.

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = NULL # object | 
body = NULL # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)
force_update = false # object | When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting platform, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check. (optional) (default to false)

try:
    # Update customer
    api_response = api_instance.update_customer(customer_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 
 **force_update** | [**object**](.md)| When updating data in the destination platform Codat checks the &#x60;sourceModifiedDate&#x60; against the &#x60;lastupdated&#x60; date from the accounting platform, if they&#x27;re different Codat will return an error suggesting you should initiate another pull of the data. If this is set to &#x60;true&#x60; then the update will override this check. | [optional] [default to false]

### Return type

[**UpdateCustomerResponse**](UpdateCustomerResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

