# CompanyDataset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **object** | Name of the linked company. | [optional] 
**accounting_platform_ref** | **object** | Identifier or reference for the company in the accounting platform. | [optional] 
**company_legal_name** | **object** | Registered legal name of the linked company. | [optional] 
**addresses** | **object** | An array of Addresses. | [optional] 
**phone_numbers** | **object** | An array of phone numbers. | [optional] 
**web_links** | **object** | An array of weblinks. | [optional] 
**ledger_lock_date** | **datetime** | If set in the accounting platform, the date (in the ISO 8601 date/time format) after which accounting transactions cannot be edited. Commonly used when books are closed at year-end. | [optional] 
**registration_number** | **object** | Registration number given to the linked company by the companies authority in the country of origin. In the UK this is Companies House. | [optional] 
**tax_number** | **object** | Company tax number. | [optional] 
**financial_year_start_date** | **datetime** | Start date of the financial year for the company. | [optional] 
**base_currency** | **object** | Currency set in the accounting platform of the linked company. Used by the currency rate. | [optional] 
**source_urls** | **object** | URL addresses for the accounting source.  For example, for Xero integrations two URLs are returned. These have many potential use cases, such as [deep linking](https://developer.xero.com/documentation/api-guides/deep-link-xero). | [optional] 
**created_date** | **datetime** | Date the linked company was created in the accounting platform. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

