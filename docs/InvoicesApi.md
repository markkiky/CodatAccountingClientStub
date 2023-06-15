# swagger_client.InvoicesApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invoice**](InvoicesApi.md#create_invoice) | **POST** /companies/{companyId}/connections/{connectionId}/push/invoices | Create invoice
[**delete_invoice**](InvoicesApi.md#delete_invoice) | **DELETE** /companies/{companyId}/connections/{connectionId}/push/invoices/{invoiceId} | Delete invoice
[**download_invoice_pdf**](InvoicesApi.md#download_invoice_pdf) | **GET** /companies/{companyId}/data/invoices/{invoiceId}/pdf | Get invoice as PDF
[**download_invoices_attachment**](InvoicesApi.md#download_invoices_attachment) | **GET** /companies/{companyId}/connections/{connectionId}/data/invoices/{invoiceId}/attachments/{attachmentId}/download | Download invoice attachment
[**get_create_update_invoices_model**](InvoicesApi.md#get_create_update_invoices_model) | **GET** /companies/{companyId}/connections/{connectionId}/options/invoices | Get create/update invoice model
[**get_invoice**](InvoicesApi.md#get_invoice) | **GET** /companies/{companyId}/data/invoices/{invoiceId} | Get invoice
[**get_invoice_attachment**](InvoicesApi.md#get_invoice_attachment) | **GET** /companies/{companyId}/connections/{connectionId}/data/invoices/{invoiceId}/attachments/{attachmentId} | Get invoice attachment
[**list_invoice_attachments**](InvoicesApi.md#list_invoice_attachments) | **GET** /companies/{companyId}/connections/{connectionId}/data/invoices/{invoiceId}/attachments | List invoice attachments
[**list_invoices**](InvoicesApi.md#list_invoices) | **GET** /companies/{companyId}/data/invoices | List invoices
[**update_invoice**](InvoicesApi.md#update_invoice) | **PUT** /companies/{companyId}/connections/{connectionId}/push/invoices/{invoiceId} | Update invoice
[**upload_invoice_attachment**](InvoicesApi.md#upload_invoice_attachment) | **POST** /companies/{companyId}/connections/{connectionId}/push/invoices/{invoiceId}/attachment | Push invoice attachment

# **create_invoice**
> CreateInvoiceResponse create_invoice(body=body, timeout_in_minutes=timeout_in_minutes)

Create invoice

Posts a new invoice to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call [Get create/update invoice model](https://docs.codat.io/accounting-api#/operations/get-create-update-invoices-model).  Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) to see which integrations support this endpoint. 

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
body = {
  "value" : {
    "invoiceNumber" : "18/04 15.26",
    "note" : "invoice push 20230418 15.26",
    "customerRef" : {
      "id" : "80000002-1674552702",
      "companyName" : "Test Customer 1"
    },
    "salesOrderRefs" : [ {
      "id" : "string",
      "dataType" : "string"
    } ],
    "issueDate" : "2023-04-18T11:09:01.438Z",
    "dueDate" : "2023-05-24T11:09:01.438Z",
    "modifiedDate" : "2023-02-14T11:09:01.438Z",
    "sourceModifiedDate" : "2023-02-14T11:09:01.438Z",
    "paidOnDate" : "2023-02-10T11:09:01.438Z",
    "currency" : "USD",
    "currencyRate" : 1,
    "lineItems" : [ {
      "description" : "lineItems.description 1",
      "unitAmount" : 15,
      "quantity" : 2,
      "discountAmount" : 0,
      "subTotal" : 30,
      "taxAmount" : 0,
      "totalAmount" : 30,
      "accountRef" : {
        "id" : "80000006-1671793811",
        "name" : "Consulting Income"
      },
      "discountPercentage" : 0,
      "taxRateRef" : {
        "id" : "80000002-1671793802",
        "name" : "Non (TAX CODE)",
        "effectiveTaxRate" : 0
      },
      "itemRef" : {
        "id" : "80000004-1675280003",
        "name" : "test income item 1"
      },
      "trackingCategoryRefs" : [ {
        "id" : "80000004-1674554660",
        "name" : "Class 3"
      } ]
    } ],
    "paymentAllocations" : [ {
      "payment" : {
        "id" : "80000004-1789341990",
        "note" : "string",
        "reference" : "string",
        "accountRef" : {
          "id" : "string",
          "name" : "string"
        },
        "currency" : "USD",
        "currencyRate" : 1,
        "paidOnDate" : "2023-02-14T11:09:01.438Z",
        "totalAmount" : 725
      },
      "allocation" : {
        "currency" : "USD",
        "currencyRate" : 1,
        "allocatedOnDate" : "2023-02-14T11:09:01.438Z",
        "totalAmount" : 725
      }
    } ],
    "withholdingTax" : [ {
      "name" : "string",
      "amount" : 0
    } ],
    "totalDiscount" : 0,
    "subTotal" : 30,
    "additionalTaxAmount" : 0,
    "additionalTaxPercentage" : 0,
    "totalTaxAmount" : 0,
    "totalAmount" : 30,
    "amountDue" : 87326532,
    "discountPercentage" : 0,
    "status" : "Submitted"
  }
} # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)

try:
    # Create invoice
    api_response = api_instance.create_invoice(body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->create_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 

### Return type

[**CreateInvoiceResponse**](CreateInvoiceResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, examples

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice**
> PushOperationSummary delete_invoice(invoice_id, company_id, connection_id)

Delete invoice

﻿The _Delete Invoices_ endpoint allows you to delete a specified Invoice from an accounting platform.  ### Process 1. Pass the `{invoiceId}` to the _Delete Invoices_ endpoint and store the `pushOperationKey` returned. 2. Check the status of the delete operation by checking the status of push operation either via     1. [Push operation webhook](/introduction/webhooks/core-rules-types#push-operation-status-has-changed) (advised),     2. [Push operation status endpoint](https://docs.codat.io/codat-api#/operations/get-push-operation).     A `Success` status indicates that the Invoice object was deleted from the accounting platform. 3. (Optional) Check that the Invoice was deleted from the accounting platform.  ### Effect on related objects  Be aware that deleting an Invoice from an accounting platform might cause related objects to be modified. For example, if you delete a paid invoice from QuickBooks Online, the invoice is deleted but the payment against that invoice is not. The payment is converted to a payment on account.  ## Integration specifics Integrations that support soft delete do not permanently delete the object in the accounting platform.  | Integration | Soft Deleted |  |-------------|--------------| | QuickBooks Online | Yes    |       > **Supported Integrations** >  > This functionality is currently only supported for our QuickBooks Online integration. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features. > We're increasing support for object deletion across various accounting platforms and data types. You can check our [Accounting API Public Product Roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) for the latest status.

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
invoice_id = NULL # object | Unique identifier for an invoice
company_id = NULL # object | 
connection_id = NULL # object | 

try:
    # Delete invoice
    api_response = api_instance.delete_invoice(invoice_id, company_id, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->delete_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**object**](.md)| Unique identifier for an invoice | 
 **company_id** | [**object**](.md)|  | 
 **connection_id** | [**object**](.md)|  | 

### Return type

[**PushOperationSummary**](PushOperationSummary.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_invoice_pdf**
> object download_invoice_pdf(invoice_id)

Get invoice as PDF

﻿Download invoice as a pdf.

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
invoice_id = NULL # object | Unique identifier for an invoice

try:
    # Get invoice as PDF
    api_response = api_instance.download_invoice_pdf(invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->download_invoice_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**object**](.md)| Unique identifier for an invoice | 

### Return type

**object**

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_invoices_attachment**
> object download_invoices_attachment(invoice_id, attachment_id)

Download invoice attachment

﻿Download invoice attachment.

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
invoice_id = NULL # object | Unique identifier for an invoice
attachment_id = NULL # object | Unique identifier for an attachment

try:
    # Download invoice attachment
    api_response = api_instance.download_invoices_attachment(invoice_id, attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->download_invoices_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**object**](.md)| Unique identifier for an invoice | 
 **attachment_id** | [**object**](.md)| Unique identifier for an attachment | 

### Return type

**object**

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_create_update_invoices_model**
> PushOption get_create_update_invoices_model()

Get create/update invoice model

﻿Get create/update invoice model. Returns the expected data for the request payload.  See the examples for integration-specific indicative models.  > **Supported Integrations** >  > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support creating and updating invoices.

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))

try:
    # Get create/update invoice model
    api_response = api_instance.get_create_update_invoices_model()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_create_update_invoices_model: %s\n" % e)
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

# **get_invoice**
> Invoice get_invoice(invoice_id)

Get invoice

﻿Get an invoice.

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
invoice_id = NULL # object | Unique identifier for an invoice

try:
    # Get invoice
    api_response = api_instance.get_invoice(invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**object**](.md)| Unique identifier for an invoice | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_attachment**
> Attachment get_invoice_attachment(invoice_id, attachment_id)

Get invoice attachment

﻿Get invoice attachment.

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
invoice_id = NULL # object | Unique identifier for an invoice
attachment_id = NULL # object | Unique identifier for an attachment

try:
    # Get invoice attachment
    api_response = api_instance.get_invoice_attachment(invoice_id, attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**object**](.md)| Unique identifier for an invoice | 
 **attachment_id** | [**object**](.md)| Unique identifier for an attachment | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoice_attachments**
> AttachmentsDataset list_invoice_attachments(invoice_id)

List invoice attachments

﻿List invoice attachments

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
invoice_id = NULL # object | Unique identifier for an invoice

try:
    # List invoice attachments
    api_response = api_instance.list_invoice_attachments(invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->list_invoice_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**object**](.md)| Unique identifier for an invoice | 

### Return type

[**AttachmentsDataset**](AttachmentsDataset.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoices**
> Invoices list_invoices(page=page, page_size=page_size, query=query, order_by=order_by)

List invoices

﻿Gets the latest invoices for a company, with pagination.

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 1)
page_size = 100 # object | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). (optional) (default to 100)
query = NULL # object | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). (optional)
order_by = NULL # object | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). (optional)

try:
    # List invoices
    api_response = api_instance.list_invoices(page=page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->list_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 1]
 **page_size** | [**object**](.md)| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | [**object**](.md)| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **order_by** | [**object**](.md)| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**Invoices**](Invoices.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice**
> UpdateInvoiceResponse update_invoice(invoice_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)

Update invoice

﻿Posts an updated invoice to the accounting package for a given company.  Required data may vary by integration. To see what data to post, first call [Get create/update invoice model](https://docs.codat.io/accounting-api#/operations/get-create-update-invoices-model).  > **Supported Integrations** >  > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support updating invoices. operationId: update-invoice

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
invoice_id = NULL # object | Unique identifier for an invoice
body = NULL # object |  (optional)
timeout_in_minutes = NULL # object |  (optional)
force_update = false # object | When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting platform, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check. (optional) (default to false)

try:
    # Update invoice
    api_response = api_instance.update_invoice(invoice_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->update_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**object**](.md)| Unique identifier for an invoice | 
 **body** | [**object**](object.md)|  | [optional] 
 **timeout_in_minutes** | [**object**](.md)|  | [optional] 
 **force_update** | [**object**](.md)| When updating data in the destination platform Codat checks the &#x60;sourceModifiedDate&#x60; against the &#x60;lastupdated&#x60; date from the accounting platform, if they&#x27;re different Codat will return an error suggesting you should initiate another pull of the data. If this is set to &#x60;true&#x60; then the update will override this check. | [optional] [default to false]

### Return type

[**UpdateInvoiceResponse**](UpdateInvoiceResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_invoice_attachment**
> upload_invoice_attachment(invoice_id)

Push invoice attachment

﻿Upload invoice attachment.

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
invoice_id = NULL # object | Unique identifier for an invoice

try:
    # Push invoice attachment
    api_instance.upload_invoice_attachment(invoice_id)
except ApiException as e:
    print("Exception when calling InvoicesApi->upload_invoice_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**object**](.md)| Unique identifier for an invoice | 

### Return type

void (empty response body)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

