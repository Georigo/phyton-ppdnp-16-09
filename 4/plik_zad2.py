import chardet

# pip install chardet

with open('test.log', "r") as f:
    raw_data = f.read()

print(raw_data)
# Nadpisane
# Dopisane
# Dopisane
# Dopisane
# Dopisane
# Dopisane
# Dopisane
# DoĹ›dane

# rb - odczyt bajtowy
with open('test.log', 'rb') as file:
    raw_data = file.read()

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'MacRoman', 'confidence': 0.6497802197802197, 'language': ''}
# po zwiększuni próbki (ilości polskich liter) odczytał poprawnie
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
encoding = result['encoding']
confidence = result['confidence']
if confidence < 0.8:
    print("Uwaga")
print(raw_data.decode(encoding=encoding))
# Dopisane
# Dopisane
# Dopisane
# Dopisane
# Dopisane
# Dośdane
# Dośćąźdane
