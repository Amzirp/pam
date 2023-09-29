Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... numbers = [random.randint(1, 100) for _ in range(10)]
... print("Исходный список:", numbers)
... max_index = numbers.index(max(numbers))
... min_index = numbers.index(min(numbers))
... numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]
