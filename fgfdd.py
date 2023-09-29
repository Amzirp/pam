Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  import random
... 
... my_list = []
... 
... for _ in range(10):
...     my_list.append(random.randint(1, 100))
... 
... x = int(input("Введите число: "))
... 
... if x in my_list:
...     index = my_list.index(x)
...     print("Номер числа в списке:", index)
... else:
