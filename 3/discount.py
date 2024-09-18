from datetime import date, datetime, timedelta

today = date.today()
print(today)
print(type(today))
# 2024-09-18
# <class 'datetime.date'>
time = datetime.now()
print("Aktualny czas:", time)  # Aktualny czas: 2024-09-18 15:36:20.038980

print(time.time())
print(today.day)
# 15:36:56.626787
# 18

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
#  days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2024-09-19

formatted_date = datetime.now().strftime("%d/%m/%Y")
print(formatted_date)  # 18/09/2024

formatted_time = datetime.now().strftime("%H:%M")
print(formatted_time)  # 15:43

formatted_time_s = datetime.now().strftime("%H:%M:%S")
print(formatted_time_s)  # 15:58:11

formatted_time_12h = datetime.now().strftime("%I:%M %p")
print(formatted_time_12h)  # 03:57 PM
# praca domowa wyswietlic godzine w formacie 12h

data_object = datetime.strptime("18/09/2024", "%d/%m/%Y")
print(data_object)
print(type(data_object))
# 2024-09-18 00:00:00
# <class 'datetime.datetime'>

products = [
    {'sku': 1, 'exp_date': today, 'price': 200},
    {'sku': 2, 'exp_date': today, 'price': 100},
    {'sku': 3, 'exp_date': tomorrow, 'price': 500},
    {'sku': 4, 'exp_date': today, 'price': 25.99},
]
print(products)  # {'sku': 2, 'exp_date': datetime.date(2024, 9, 18), 'price': 100},
for p in products:
    # print(p)
    # print(type(p))  # <class 'dict'>
    print(p['price'])
    if p['exp_date'] != today:
        continue  # wraca na początek pętli, bierze kolejny element
    p['price'] *= 0.8  # price = price * 0.8
    print(f"Nowa cena {p['sku']}, {p['price']}")
# 200
# Nowa cena 1, 160.0
# 100
# Nowa cena 2, 80.0
# 500
# 25.99
# Nowa cena 4, 20.792
