# swagger_client.CompanyInfoApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_info**](CompanyInfoApi.md#get_company_info) | **GET** /companies/{companyId}/data/info | Get company info
[**refresh_company_info**](CompanyInfoApi.md#refresh_company_info) | **POST** /companies/{companyId}/data/info | Refresh company info

# **get_company_info**
> CompanyDataset get_company_info()

Get company info

Gets the latest basic info for a company.

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
api_instance = swagger_client.CompanyInfoApi(swagger_client.ApiClient(configuration))

try:
    # Get company info
    api_response = api_instance.get_company_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyInfoApi->get_company_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CompanyDataset**](CompanyDataset.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_company_info**
> Dataset refresh_company_info()

Refresh company info

Initiates the process of synchronising basic info for a company

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
api_instance = swagger_client.CompanyInfoApi(swagger_client.ApiClient(configuration))

try:
    # Refresh company info
    api_response = api_instance.refresh_company_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyInfoApi->refresh_company_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dataset**](Dataset.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

