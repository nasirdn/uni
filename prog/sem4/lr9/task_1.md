1. �������� �������

��������:
������ ������������ ��� �������� ��������-��������������� ������ ����������������. ��� ������������ ����� �������, ����������� �������� � ������ �������� ������������� ����. �������� ������ � Python �������������� � �������������� ��������� ����� "class".
������:
```python
class Car():  
   
  def __init__(self, brand, model, years):  
      self.brand = brand  
      self.model = model  
      self.years = years  
   
  def get_full_name(self):  
      name = f"���������� {self.brand} {self.model} {self.years}"  
      return name.title()
```

---

2. �������� ��������

��������:
������ � ��� ���������� ������. ��� �������� �������� � ����� ���������� ����� � ������� ��������� ����� "class".
������: 
```python
car_1 = Car('Audi', 'R8', 2023)
```

---

3. ����������� �����

��������:
����������� ����� ������������ ����� �����, ������� �� ������� �������� ������� ��� ������� � ��� ��������� � �������. �� ������ ������������ ��� ����������� ��������� ������� ��� ������ ������ ������.
������:
```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y
```

---

4. ����������� �����

����a���:
����������� ����� �������� �������, ������� �������� � ������, � �� � ���������� ����� ������. �� �� ����� ������� � ��������� ���������� � ������������ ��� ���������� ��������, �� ��������� ������� � ��������� �������.
������:
```python
class StringUtils:
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]
```
����� �������, �������� �������� ����� ����������� ������� � ����������� ������� ����������� � ���, ��� ����������� ����� ������������ ��� ����������� ��������� ������� ��� ������ ������ ������, ����� ��� ����������� ����� ������������ ��� ���������� ��������, �� ��������� ������� � ��������� �������.

---

5. ��������� (getter, setter, deleter)

����a���:
������ (����� ���������) � ��� ������, ������� ������������ � ��������-��������������� ���������������� (���) ��� ������� � ������� ��������� ������. Getter ������ ����������� � �������������� ���������� @property � ������������ ������ � �������� �������, ��� � ������� ����������, �� ��� ���� ��������� ��������� �������������� �������� �� ��� ����� �������� ��������.
������ (����� ���������) � ��� �����, ������� ������������ ��� ��������� �������� ��������. Setter ����������� � ������� ���������� @<property_name>.setter � ��������� �������������� ������� ��������� �������� ��������, ��������, ��������� ��� �� ������������ ��� �������� ������ �������� �������.
������� (����� ��������) - ��� �����, ������� ������������ ��� �������� ������������� �������� �������. Deleter ����������� � ������� ���������� @<property_name>.deleter � ��������� ��������� �������������� �������� ��� �������� ��������, ��������, ���������� ������� ��� ��������� ������ ��������.
������:
Getter
```python
class MyClass:
    def __init__(self):
        self._my_variable = 0

    @property
    def my_variable(self):
        return self._my_variable

obj = MyClass()
print(obj.my_variable)  # ����� getter ��� �������� my_variable
```
Setter
```python
class MyClass:
    def __init__(self):
        self._my_variable = 0
    
    @property
    def my_variable(self):
        return self._my_variable
    
    @my_variable.setter
    def my_variable(self, value):
        if value > 0:
            self._my_variable = value

obj = MyClass()
obj.my_variable = 10  # ����� setter ��� �������� my_variable
```
Deleter
```python
class MyClass:
    def __init__(self):
        self._my_variable = 0
    
    @property
    def my_variable(self):
        return self._my_variable
    
    @my_variable.deleter
    def my_variable(self):
        del self._my_variable

obj = MyClass()
del obj.my_variable  # ����� deleter ��� �������� my_variable
```

---

6. ������������

����a���:
��� ��������� �������� ������ ���, ��� ������� ��� ����� ������ ������ � �������� ���������. ��������� �������� ����� ���� ������, ����� ��������� ����������. ��� ����������� ���� �������� private, protected � public ���������� � ������� ����������.  
- ��������� (public, ��� ������� ����������, publicBanana);  
- ���������� (protected, ���� ������ ������������� � ������ ��������, 
  _protectedBanana);  
- ��������� (private, ��� ������ ������������� � ������ ��������, __privateBanana).
������:
```python
class Phone:
    username = "Kate"                # public variable
    __serial_number = "11.22.33"     # private variable
    __how_many_times_turned_on = 0   # private variable

    def call(self):                  # public method
        print( "Ring-ring!" )

    def __turn_on(self):             # private method
        self.__how_many_times_turned_on += 1 
        print( "Times was turned on: ", self.__how_many_times_turned_on )
```

---

7. ������������

����a���:
��������� ��������� ����� ����� �� ������ ��� ������������� ������. ��������� ��������� ������������ �������� �������� � ����������. �������� ��������� �� ����������� ��� ��������� �������� � ������. ���������� ��� ���������� ������� (base class) ��� ������������ (parent class), � �������� - ����������� (derived class) ��� �������� (child class).
������:
```python
class Car():
    def __init__(self, brand, model, years):
        self.brand = brand
        self.model = model
        self.years = years
        self.mileage = 0

    def get_full_name(self):
        name = f"���������� {self.brand} {self.model} {self.years}"
        return name.title()
      
class ElectricCar(Car):
    def __init__(self, brand, model, years):
        # �������������� �������� ������ ��������
        super().__init__(brand, model, years)
        # ������� ������-�������
        self.battery_size = 100

    def battery_power(self):
        print(f"�������� ������������ {self.battery_size} ���?�")
```

---

8. �����������

����a���:
����������� � ������������� ������������ ��������(�����, �������� ��� ������) ��� ������������� ��������� ����� � ��������� ��������� �������������. ����������� ��������� � ����������� �������� ��������� ������� ���������� ������ ������ � ���� �� �����. ��� ��������� ������������ ����� ��������� ��� ���������� ��������, ���������� �� ���� �������.
������:
```python
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Dori", 2.5)
dog1 = Dog("Berry", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
```

---

9. ���������

����a���:
����� ������������ ����������� ������� ������ � Python ��� �������� �����������. ����������� ������� ������ ������������� ����������� ���������� ������, ������� ������ ���� ����������� � �������-�����������.
����� ������� ���������, ����� ������������ ������ `abc` (Abstract Base Classes), ������� ��������� ��������� ����������� ������� ������.
������:
```python
from abc import ABC, abstractmethod

class Shape(ABC):  # ��� ����������� ������� �����, ������� �������� �����������
    @abstractmethod
    def area(self):  # ����������� �����, ������� ������ ���� ���������� � �����������
        pass

    @abstractmethod
    def perimeter(self):  # ��� ���� ����������� �����
        pass

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length
```

---

10.  ������������� ������������

����a���:
�������� ����� ����� ����������� ���������������� �� ���������� �������, ��� ������������ �������� ��� �������������� � �������� �������. ������������� ������������ ��������� ������� �������� ������� � ���������� �������� ����������, ��� �������� � ����������� ���� � ��������� ������������� ����������������.
������:
```python
# ��� super()
class B:
    def b(self):
        print('b')
class C:
    def c(self):
        print('c')
class D(B, C):
    def d(self):
        print('d')
d = D()
d.b()
d.c()
d.d()
'''�������:
   b
   c
   d'''

# � super()
class Tokenizer:
    """Tokenize text"""
    def __init__(self, text):
        self.tokens = text.split()
      
class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self, text):
        super().__init__(text)
        self.word_count = len(self.tokens)
      
class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self, text):
        super().__init__(text)
        self.vocab = set(self.tokens)
      
class TextDescriber(WordCounter, Vocabulary):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        super().__init__(text)
      
td = TextDescriber('row row row your boat')
print(td.tokens)
print(td.vocab)
print(td.word_count)
```

---

11. ������� (mixin)

����a���:
����� �������������� ������������ � Python � ������ ����������, ������� ��������� ���������� ����������� ������������� ������������. ��� ������������ ����� ������� ������, ������� �������� ����� �������, ��������������� ��� ���������� � ������� ������, � ��������� ��������� ���������������� ������� ��� �������� �������� ������������.  
������������:
- ����� ������ �������� ������������ ��� ����� ����������� ��������, �� 
  ������������ �� ��������
- ����� ������ �������� ���������������� � ������������ ������� ��� ��������� �� ����.
������:
```python
''' ��� �������� ������� ���������� ���������� ����� � ������� ��������. �������� ������� � � ������� �� ������ ���� ������ __init__ ������, ��� ��� �� ����� ������������ __init__ ����� ������, � �������� ��� ����� ���������. '''
class LoggerMixin:
    def log(self, message):
        print(f'[LOG]: {message}')

''' ��� ������������� ������� ���������� �������� � � ������ ������������ ������� ���� ������, �������� ��������� ���������������� �������. '''
class MyClass(LoggerMixin):
    def do_something(self):
        self.log('����� ����������� ��������')
        # ��������� ��������
        self.log('����� ���������� ��������')

my_obj = MyClass()
my_obj.do_something()
```

---

12. ����������

����a���:
������������ ����� ����������� ���������� ��������� ��������� ��� ������� ��� ���������� � ����������� �� ����� �� ����������. ��� ��������, ��� ���� � �� �� ������� ��� �������� ����� ���� ������������ ��� ������ ����� ������, � �� ��������� ����� ��������������� ���� �����.
������:
```python
''' ������� ���������� �������: '''
def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + " " + b
    else:
        return None

print(add(3, 5))  # �����: 8
print(add("Hello", "World"))  # �����: Hello World

''' ������ ���������� ����������: '''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 =  Vector(3, 4)
print(v1 + v2)  # �����: Vector(4, 6)
print(v2 - v1)  # �����: Vector(2, 2)
```

---

13. ����������

����a���:
��������� ����������������, ������� �������� ������� ������ ����������, ������������ ������������� ������ ����������� ���������� � �������������� �����������. � Python �� ����� �������� ���������� ������ � ������� ����������� �������, � ����������� ������ ����� ���� ������� � ������� ������ abc (����������� ������� �����) � abstractmethod ������ abc.
������:
```python
import abc
class Shape(abc.ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    @abc.abstractmethod     
    def area (self): pass       # ���������� �����

    def print_point(self):          # ������������� �����
        print("X:", self.x, "\tY:", self.y)

# ����� �������������� 
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
    def area (self): return self.width * self.height


rect = Rectangle(10, 20, 100, 100)
rect.print_point()      # X: 10   Y: 20
```

---

14. ����������

����a���:
��� ���� �� ��������������� ��������� ��������-���������������� ����������������, ������� ��������� �������� ������ ����������������� ���� � ������. ���������� ����������� ����� �������� ��������� ������ �������, ������� ��������� �� ������ �������.
������:
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Author:
    def __init__(self, name):
        self.name = name

# ������� ���������� �������
author1 = Author("John Doe")
book1 = Book("Python Fundamentals", author1)

# ����������� �������
print(book1.author.name)  # ������� "John Doe"
```

---

15. ����������

����a���:
������������ ����� ������ �������� ������� �������� ����� ����������� ����� ������� ��������. � ���������� ���� ������ �������� ������ ������� � �������� ������, � ��� ����������� ��������� �������, ��� ��� ����� ����� ������������.
������:
```python
class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        print("Car started")
        self.engine.start()

    def stop(self):
        print("Car stopped")
        self.engine.stop()

my_car = Car()
my_car.start()
my_car.stop()
```

---

16. ���������

����a���:
��� ������� ����������� �������� ��������� ������� � ��������� �������� ��� ���������� ����� ������� �����. � ������� �� ������������, ��������� ��������� ��������� ��������� "��������" ����� ���������, ��� ������ �� ����� ���������� ���� �� �����.
������:
```python
class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Car:
    def __init__(self):
        self.engine = Engine()  # ��������� - ������ ������ Engine ���������� � ������� ������ Car

    def start(self):
        print("Starting the car")
        self.engine.start()

    def stop(self):
        print("Stopping the car")
        self.engine.stop()

my_car = Car()
my_car.start()  # �����: Starting the car
                #        Engine started
my_car.stop()   # �����: Stopping the car
                #        Engine stopped
```
�������� �������� ����� ����������� � ���������� ����������� � ���, ��� ������� �������: � ���������� ������� ������ ������� ���� � ������, � � ��������� ������� ����� ���� ������������.

---

17. ����������/�������������

����a���:
��������� ���������������� �������� ���������� ����������� ��������� ��� ���������� �� ������������ ����� ����������������. � ������ Python, ������������� ������������� ��������� ����, ������� ��������� ��������� ������ ��� ��������� ���������. ������������� � Python ����� ���� ������������ ��� �������� �������, �������, ���������� � ������ �������� ������, ������� ������ ���������� ������ ��� ��������� ������������ ����������.
������:
```python
''' ������������� ������: '''
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print("Engine started")

# ������������� ������������������� ������
my_car = Car("Toyota", "Corolla")
my_car.start_engine()

''' ������������� ���������: '''
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# ������������� ������������������� ���������
arr = [1, 3, 5, 7, 9]
target = 5
index = binary_search(arr, target)
print(f"Index of {target} is {index}")
```
---

18. �����������

����a���:
��������, ��� ���� ������ ��� ������ ���������� ���������������� ��� ������ �� ������� ������� ��� ������. ��� ��������� ��������� ��������� � ����������������� ���������, ��� ������ ����� ����� ������ � ������������ �����������. ����������� � Python ����� ���� ����������� ��� � �������������� ���������� �������, ��� � � ������� ��������� ���������. ������� ������������ � Python �������� ���������� ��� ������ � ������ ������, ������������ ������������, ��������������� ������������ � ������� ������� ���������.
������:
```python
import requests
```