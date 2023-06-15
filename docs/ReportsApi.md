# swagger_client.ReportsApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aged_creditors_report**](ReportsApi.md#get_aged_creditors_report) | **GET** /companies/{companyId}/reports/agedCreditor | Aged creditors report
[**get_aged_debtors_report**](ReportsApi.md#get_aged_debtors_report) | **GET** /companies/{companyId}/reports/agedDebtor | Aged debtors report
[**get_balance_sheet**](ReportsApi.md#get_balance_sheet) | **GET** /companies/{companyId}/data/financials/balanceSheet | Get balance sheet
[**get_cash_flow_statement**](ReportsApi.md#get_cash_flow_statement) | **GET** /companies/{companyId}/data/financials/cashFlowStatement | Get cash flow statement
[**get_profit_and_loss**](ReportsApi.md#get_profit_and_loss) | **GET** /companies/{companyId}/data/financials/profitAndLoss | Get profit and loss
[**is_aged_creditors_report_available**](ReportsApi.md#is_aged_creditors_report_available) | **GET** /companies/{companyId}/reports/agedCreditor/available | Aged creditors report available
[**is_aged_debtor_report_available**](ReportsApi.md#is_aged_debtor_report_available) | **GET** /companies/{companyId}/reports/agedDebtor/available | Aged debtors report available

# **get_aged_creditors_report**
> AgedCreditorReport get_aged_creditors_report(report_date=report_date, number_of_periods=number_of_periods, period_length_days=period_length_days)

Aged creditors report

Returns aged creditors report for company that shows the total balance owed by a business to its suppliers over time.

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
report_date = NULL # object | Date the report is generated up to. (optional)
number_of_periods = NULL # object | Number of periods to include in the report. (optional)
period_length_days = NULL # object | The length of period in days. (optional)

try:
    # Aged creditors report
    api_response = api_instance.get_aged_creditors_report(report_date=report_date, number_of_periods=number_of_periods, period_length_days=period_length_days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_aged_creditors_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_date** | [**object**](.md)| Date the report is generated up to. | [optional] 
 **number_of_periods** | [**object**](.md)| Number of periods to include in the report. | [optional] 
 **period_length_days** | [**object**](.md)| The length of period in days. | [optional] 

### Return type

[**AgedCreditorReport**](AgedCreditorReport.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aged_debtors_report**
> AgedDebtorReport get_aged_debtors_report(report_date=report_date, number_of_periods=number_of_periods, period_length_days=period_length_days)

Aged debtors report

Returns aged debtors report for company that shows the total outstanding balance due from customers to the business over time.

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
report_date = NULL # object | Date the report is generated up to. (optional)
number_of_periods = NULL # object | Number of periods to include in the report. (optional)
period_length_days = NULL # object | The length of period in days. (optional)

try:
    # Aged debtors report
    api_response = api_instance.get_aged_debtors_report(report_date=report_date, number_of_periods=number_of_periods, period_length_days=period_length_days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_aged_debtors_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_date** | [**object**](.md)| Date the report is generated up to. | [optional] 
 **number_of_periods** | [**object**](.md)| Number of periods to include in the report. | [optional] 
 **period_length_days** | [**object**](.md)| The length of period in days. | [optional] 

### Return type

[**AgedDebtorReport**](AgedDebtorReport.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_sheet**
> BalanceSheet get_balance_sheet(period_length, periods_to_compare, start_month=start_month)

Get balance sheet

Gets the latest balance sheet for a company.

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
period_length = NULL # object | Number of months defining the period of interest.
periods_to_compare = NULL # object | Number of periods with `periodLength` to compare.
start_month = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    # Get balance sheet
    api_response = api_instance.get_balance_sheet(period_length, periods_to_compare, start_month=start_month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_balance_sheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period_length** | [**object**](.md)| Number of months defining the period of interest. | 
 **periods_to_compare** | [**object**](.md)| Number of periods with &#x60;periodLength&#x60; to compare. | 
 **start_month** | [**datetime**](.md)|  | [optional] 

### Return type

[**BalanceSheet**](BalanceSheet.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cash_flow_statement**
> CashFlowStatement get_cash_flow_statement(period_length, periods_to_compare, start_month=start_month)

Get cash flow statement

Gets the latest cash flow statement for a company.

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
period_length = NULL # object | Number of months defining the period of interest.
periods_to_compare = NULL # object | Number of periods with `periodLength` to compare.
start_month = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    # Get cash flow statement
    api_response = api_instance.get_cash_flow_statement(period_length, periods_to_compare, start_month=start_month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_cash_flow_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period_length** | [**object**](.md)| Number of months defining the period of interest. | 
 **periods_to_compare** | [**object**](.md)| Number of periods with &#x60;periodLength&#x60; to compare. | 
 **start_month** | [**datetime**](.md)|  | [optional] 

### Return type

[**CashFlowStatement**](CashFlowStatement.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profit_and_loss**
> ProfitAndLossReport get_profit_and_loss(period_length, periods_to_compare, start_month=start_month)

Get profit and loss

Gets the latest profit and loss for a company.

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
period_length = NULL # object | Number of months defining the period of interest.
periods_to_compare = NULL # object | Number of periods with `periodLength` to compare.
start_month = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    # Get profit and loss
    api_response = api_instance.get_profit_and_loss(period_length, periods_to_compare, start_month=start_month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_profit_and_loss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period_length** | [**object**](.md)| Number of months defining the period of interest. | 
 **periods_to_compare** | [**object**](.md)| Number of periods with &#x60;periodLength&#x60; to compare. | 
 **start_month** | [**datetime**](.md)|  | [optional] 

### Return type

[**ProfitAndLossReport**](ProfitAndLossReport.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_aged_creditors_report_available**
> object is_aged_creditors_report_available()

Aged creditors report available

Indicates whether the aged creditor report is available for the company.

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))

try:
    # Aged creditors report available
    api_response = api_instance.is_aged_creditors_report_available()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->is_aged_creditors_report_available: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_aged_debtor_report_available**
> object is_aged_debtor_report_available()

Aged debtors report available

Indicates whether the aged debtor report is available for the company.

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))

try:
    # Aged debtors report available
    api_response = api_instance.is_aged_debtor_report_available()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->is_aged_debtor_report_available: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

