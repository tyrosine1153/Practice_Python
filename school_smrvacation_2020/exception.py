class AnyError(Exception):
    def __str__(self):
        print("집에 갈래요우")

try:
    if True:
        raise AnyError
except NameError as err:
    print(err)
    print(type(err))
except ValueError as err:
    print(err)
    print(type(err))
except AnyError as err:
    print(err)
    print(type(err))