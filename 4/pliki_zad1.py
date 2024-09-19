# działania z plikami
# context manager
# with - context manager
# open() - praca z plikami
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with  open('test.log', 'w', encoding='utf-8') as fh:
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("kolejne\n")

# x - sprawdza czy plik istnieje
# with open('test.log', "x", encoding='utf-8') as f:
#     f.write("Cokolwiek")
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\ppdnp-16-09\4\pliki_zad1.py", line 21, in <module>
#     with open('test.log', "x") as f:
#          ^^^^^^^^^^^^^^^^^^^^^
# FileExistsError: [Errno 17] File exists: 'test.log'

# tworzy nowy plik, kasuje jesli istniał!!!
with open('test.log', "w", encoding='utf-8') as f:
    f.write("Nadpisane\n")

with open('test.log', "a", encoding='utf-8') as f:
    f.write("Dopisane\n")
    f.write("Dopisane\n")
    f.write("Dopisane\n")
    f.write("Dopisane\n")
    f.write("Dopisane\n")
    f.write("Dopisane\n")
    f.write("Dośdane\n")

with open('test.log', "r", encoding='utf-8') as f:
    lines = f.read()

print(lines)
# encoding='utf-8' - ustawienie kodowania
