import requests as re

url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"

response = re.get(url)
print(response)  # <Response [200]>
# 200 ok
# 3xx - 304 - przekierowania
# 4xx - 404 - brak strony, 400 Bad Request bład w parametrach, 401 wymaga autoryzacji
# 5xx - 500 Internal Server Error - błedy po stronie serwera

print(response.text)
print(type(response.text))  # <class 'str'>

data = response.json()
print(data)
print(type(data))  # <class 'dict'>
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
#  'rates': [{'no': '184/A/NBP/2024', 'effectiveDate': '2024-09-20', 'mid': 3.8317}]}

print(data['currency'], data['rates'][0]['mid'])  # dolar amerykański 3.8317, euro 4.2779
