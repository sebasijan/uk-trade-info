import requests

baseUrl = 'https://api.uktradeinfo.com/'
resource = 'OTS'

filter = "filter(MonthId ge 202101 and CountryId eq 388 and FlowTypeId eq 3 and (Commodity/Hs2Code eq \'08\' or Commodity/Hs2Code eq \'07\'))"
aggregates = "aggregate(Value with sum as TotalValue, NetMass with sum as TotalNetMass)"
group_by = f"groupby((Commodity/Hs6Description, Commodity/Cn8LongDescription, Commodity/Cn8Code), {aggregates})"
apply = f"$apply={filter}/{group_by}"

params = f"?&{apply}"

response = requests.get(baseUrl + resource + params)

if not response.ok:
    raise Exception(response.text)

value = response.json()['value']

sortedValue = sorted(value, key=lambda x: x['TotalValue'], reverse=False)

for v in sortedValue:
    print(f"{v['Commodity']['Hs6Description']}")
    print(f"{v['Commodity']['Cn8LongDescription']}")
    print(f"\t{v['Commodity']['Cn8Code']}")
    print("\t£{:,.2f}".format(v['TotalValue']))
    print("\t{:,}".format(v['TotalNetMass']))