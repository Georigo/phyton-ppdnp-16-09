# funkcja wewnętrzna, zagnieżdzona
#  uzywane w dekoratorach

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # tu zwracamy adres funkcji (referencje)


fun1()
xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x0000016AA91A9EE0>
print(type(xFun))  # <class 'function'>
xFun()
# To jest fun1
# To jest fun1
# <function fun1.<locals>.fun2 at 0x000002095A549EE0>
# <class 'function'>
# To jest fun2
