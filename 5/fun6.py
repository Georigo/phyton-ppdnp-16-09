def connect(**opcje):
    print(opcje)  # {'a': 9}, {'a': 9, 'b': {'a': 67}}


connect(a=9, b={"a": 67})
connect(name="Radek")  # {'name': 'Radek'}


def all_args(*args, **kwargs):
    print(args, kwargs)


all_args()
all_args(1)
all_args(11, 2, 3)
all_args(11, 2, 3, a=9)
all_args(a=9)
all_args(a=9, name="Radek")
# all_args(a=9,name="Radek", 9)  # SyntaxError: positional argument follows keyword argument
# {'a': 9, 'b': {'a': 67}}
# {'name': 'Radek'}
# () {}
# (1,) {}
# (11, 2, 3) {}
# (11, 2, 3) {'a': 9}
# () {'a': 9}
# () {'a': 9, 'name': 'Radek'}
