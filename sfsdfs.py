Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... my_list = []
... 
... for _ in range(10):
...     my_list.append(random.randint(1, 100))
... 
... print("Список случайных чисел:", my_list)
... 
... duplicates = []
... 
... for num in my_list:
...     if my_list.count(num) > 1 and num not in duplicates:
...         duplicates.append(num)
... 
... if duplicates:
...     print("Повторяющиеся элементы:", duplicates)
... else:
