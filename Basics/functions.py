# *args are any arguments, args is the variable name
# **kwards are any keyword arguments, kwards is the variable name
def my_function(*args, **kwargs) -> None:
  print(f"The args is a tuple: {args}")
  print(f"The kwargs is a dictionary: {kwargs}")


my_function("a", "b", "c", 1, 2, 3, one=1, two=2, three=3, four=4)

# lambda arguments : expresion
x = lambda a : a + 10 # takes a and adds 10, x is function name. result = x(a)
x = lambda a, b : a * b # multiplies 2 numbers together. result = x(a,b)
"""
    def myfunc(n):
    return lambda a : a * n

    mydoubler = myfunc(2)
    mytripler = myfunc(3)

    print(mydoubler(11))
    print(mytripler(11))
"""
