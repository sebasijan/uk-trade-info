import requests

baseUrl = 'https://api.uktradeinfo.com/'
resource = 'OTS'

params = '?&$apply=filter(MonthId eq 202201 and CountryId eq 388 and FlowTypeId eq 3)/groupby((Commodity/Hs6Description, Commodity/Cn8LongDescription, Commodity/Cn8Code),aggregate(Value with sum as TotalValue, NetMass with sum as TotalNetMass))'

response = requests.get(baseUrl + resource + params)

if not response.ok:
    raise Exception(response.text)

value = response.json()['value']

sortedValue = sorted(value, key=lambda x: x['TotalValue'], reverse=False)

for v in sortedValue:
    print(f"{v['Commodity']['Cn8LongDescription']}")
    print(f"\t{v['Commodity']['Cn8Code']}")
    print("\t£{:,.2f}".format(v['TotalValue']))
    print(f"\t{v['TotalNetMass']}")