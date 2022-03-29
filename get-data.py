import requests
import locale

baseUrl = 'https://api.uktradeinfo.com/'
resource = 'OTS'

# Jan 2022, HS2Code = 07, Country = South Africa, FlowType = non-EU import, grouped by commodity, aggregate sum value as TotalValue
params = '?&$apply=filter(MonthId eq 202201 and CountryId eq 388 and FlowTypeId eq 3)/groupby((Commodity/Cn8LongDescription),aggregate(Value with sum as TotalValue))'

response = requests.get(baseUrl + resource + params)

value = response.json()['value']

sortedValue = sorted(value, key=lambda x: x['TotalValue'], reverse=False)

for v in sortedValue:
    print(v['Commodity']['Cn8LongDescription'])
    print("£{:,.2f}".format(v['TotalValue']))