1. СОЗДАНИЕ КЛАССОВ

Описание:
Классы используются для создания объектно-ориентированной модели программирования. Они представляют собой шаблоны, описывающие атрибуты и методы объектов определенного типа. Создание класса в Python осуществляется с использованием ключевого слова "class".
Пример:
```python
class Car():  
   
  def __init__(self, brand, model, years):  
      self.brand = brand  
      self.model = model  
      self.years = years  
   
  def get_full_name(self):  
      name = f"Автомобиль {self.brand} {self.model} {self.years}"  
      return name.title()
```

---

2. СОЗДАНИЕ ОБЪЕКТОВ

Описание:
Объект — это воплощение класса. Для создания объектов в нужно определить класс с помощью ключевого слова "class".
Пример: 
```python
car_1 = Car('Audi', 'R8', 2023)
```

---

3. СТАТИЧЕСКИЙ КЛАСС

Описание:
Статический класс представляет собой класс, который не требует создания объекта для доступа к его свойствам и методам. Он обычно используется для организации связанных функций или данных внутри класса.
Пример:
```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y
```

---

4. СТАТИЧЕСКИЙ МЕТОД

Описaние:
Статический метод является методом, который привязан к классу, а не к экземпляру этого класса. Он не имеет доступа к атрибутам экземпляра и используется для выполнения операций, не требующих доступа к состоянию объекта.
Пример:
```python
class StringUtils:
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]
```
Таким образом, основное различие между статическим классом и статическим методом заключается в том, что статический класс используется для организации связанных функций или данных внутри класса, тогда как статический метод используется для выполнения операций, не требующих доступа к состоянию объекта.

---

5. АКСЕССОРЫ (getter, setter, deleter)

Описaние:
Геттер (метод получения) – это методы, которые используются в объектно-ориентированном программировании (ООП) для доступа к частным атрибутам класса. Getter обычно реализуется с использованием декоратора @property и обеспечивает доступ к атрибуту объекта, как к обычной переменной, но при этом позволяет выполнить дополнительные операции до или после возврата значения.
Сеттер (метод установки) – это метод, который используется для установки значения свойства. Setter реализуется с помощью декоратора @<property_name>.setter и позволяет контролировать процесс установки значения атрибута, например, проверять его на допустимость или изменять другие атрибуты объекта.
Делетер (метод удаления) - это метод, который используется для удаления определенного атрибута объекта. Deleter реализуется с помощью декоратора @<property_name>.deleter и позволяет выполнить дополнительные действия при удалении атрибута, например, освободить ресурсы или выполнить другие операции.
Пример:
Getter
```python
class MyClass:
    def __init__(self):
        self._my_variable = 0

    @property
    def my_variable(self):
        return self._my_variable

obj = MyClass()
print(obj.my_variable)  # Вызов getter для атрибута my_variable
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
obj.my_variable = 10  # Вызов setter для атрибута my_variable
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
del obj.my_variable  # Вызов deleter для атрибута my_variable
```

---

6. ИНКАПСУЛЯЦИЯ

Описaние:
Это концепция упаковки данных так, что внешний мир имеет доступ только к открытым свойствам. Некоторые свойства могут быть скрыты, чтобы уменьшить уязвимость. Это реализуется путём создания private, protected и public переменных и методов экземпляра.  
- публичный (public, нет особого синтаксиса, publicBanana);  
- защищенный (protected, одно нижнее подчеркивание в начале названия, 
  _protectedBanana);  
- приватный (private, два нижних подчеркивания в начала названия, __privateBanana).
Пример:
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

7. НАСЛЕДОВАНИЕ

Описaние:
Позволяет создавать новый класс на основе уже существующего класса. Ключевыми понятиями наследования являются подкласс и суперкласс. Подкласс наследует от суперкласса все публичные атрибуты и методы. Суперкласс еще называется базовым (base class) или родительским (parent class), а подкласс - производным (derived class) или дочерним (child class).
Пример:
```python
class Car():
    def __init__(self, brand, model, years):
        self.brand = brand
        self.model = model
        self.years = years
        self.mileage = 0

    def get_full_name(self):
        name = f"Автомобиль {self.brand} {self.model} {self.years}"
        return name.title()
      
class ElectricCar(Car):
    def __init__(self, brand, model, years):
        # инициализирует атрибуты класса родителя
        super().__init__(brand, model, years)
        # атрибут класса-потомка
        self.battery_size = 100

    def battery_power(self):
        print(f"Мощность аккумулятора {self.battery_size} кВт?ч")
```

---

8. ПОЛИМОРФИЗМ

Описaние:
Заключается в использовании единственной сущности(метод, оператор или объект) для представления различных типов в различных сценариях использования. Полиморфизм относится к возможности объектов различных классов ответвлять методы одного и того же имени. Это позволяет использовать общий интерфейс для выполнения действий, независимо от типа объекта.
Пример:
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

9. ИНТЕРФЕЙС

Описaние:
Можно использовать абстрактные базовые классы в Python для создания интерфейсов. Абстрактные базовые классы предоставляют возможность определить методы, которые должны быть реализованы в классах-наследниках.
Чтобы создать интерфейс, можно использовать модуль `abc` (Abstract Base Classes), который позволяет создавать абстрактные базовые классы.
Пример:
```python
from abc import ABC, abstractmethod

class Shape(ABC):  # Это абстрактный базовый класс, который является интерфейсом
    @abstractmethod
    def area(self):  # Абстрактный метод, который должен быть реализован в наследниках
        pass

    @abstractmethod
    def perimeter(self):  # Еще один абстрактный метод
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

10.  МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ

Описaние:
Дочерний класс может наследовать функциональность от нескольких классов, что обеспечивает гибкость при проектировании и создании классов. Множественное наследование позволяет создать иерархию классов с различными уровнями абстракции, что помогает в организации кода и повторном использовании функциональности.
Пример:
```python
# без super()
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
'''Получим:
   b
   c
   d'''

# с super()
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

11. ПРИМЕСЬ (mixin)

Описaние:
Форма множественного наследования в Python и мощный инструмент, который позволяет преодолеть ограничения единственного наследования. Они представляют собой простые классы, которые включают набор методов, предназначенных для добавления к другому классу, и позволяют расширять функциональность классов без глубокой иерархии наследования.  
Используется:
- Когда хотите повторно использовать код между несколькими классами, но 
  наследование не подходит
- Когда хотите добавить функциональность к существующим классам без изменения их кода.
Пример:
```python
''' Для создания примеси достаточно определить класс с нужными методами. Основное условие – у примеси не должно быть своего __init__ метода, так как он может перезаписать __init__ метод класса, к которому она будет добавлена. '''
class LoggerMixin:
    def log(self, message):
        print(f'[LOG]: {message}')

''' Для использования примеси достаточно добавить её в список родительских классов того класса, которому требуется функциональность примеси. '''
class MyClass(LoggerMixin):
    def do_something(self):
        self.log('Перед выполнением действия')
        # выполняем действие
        self.log('После выполнения действия')

my_obj = MyClass()
my_obj.do_something()
```

---

12. ПЕРЕГРУЗКА

Описaние:
Представляет собой возможность определять различное поведение для функций или операторов в зависимости от типов их аргументов. Это означает, что одна и та же функция или оператор может быть использована для разных типов данных, и их поведение будет соответствовать этим типам.
Пример:
```python
''' Примеры перегрузки функций: '''
def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + " " + b
    else:
        return None

print(add(3, 5))  # Вывод: 8
print(add("Hello", "World"))  # Вывод: Hello World

''' Пример перегрузки операторов: '''
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
print(v1 + v2)  # Вывод: Vector(4, 6)
print(v2 - v1)  # Вывод: Vector(2, 2)
```

---

13. АБСТРАКЦИЯ

Описaние:
Концепция программирования, которая скрывает сложные детали реализации, предоставляя пользователям только необходимую информацию и функциональные возможности. В Python мы можем добиться абстракции данных с помощью абстрактных классов, а абстрактные классы могут быть созданы с помощью модуля abc (абстрактный базовый класс) и abstractmethod модуля abc.
Пример:
```python
import abc
class Shape(abc.ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    @abc.abstractmethod     
    def area (self): pass       # абстрактны метод

    def print_point(self):          # неабстрактный метод
        print("X:", self.x, "\tY:", self.y)

# класс прямоугольника 
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

14. АССОЦИАЦИЯ

Описaние:
Это один из фундаментальных принципов объектно-ориентированного программирования, который позволяет объектам класса взаимодействовать друг с другом. Ассоциация реализуется путем создания атрибутов одного объекта, которые ссылаются на другие объекты.
Пример:
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Author:
    def __init__(self, name):
        self.name = name

# Создаем экземпляры классов
author1 = Author("John Doe")
book1 = Book("Python Fundamentals", author1)

# Ассоциируем объекты
print(book1.author.name)  # Выведет "John Doe"
```

---

15. КОМПОЗИЦИЯ

Описaние:
Представляет собой способ создания сложных объектов путем объединения более простых объектов. В композиции один объект содержит другие объекты в качестве частей, и при уничтожении основного объекта, все его части также уничтожаются.
Пример:
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

16. АГРЕГАЦИЯ

Описaние:
Это процесс объединения объектов различных классов в составных объектах для выполнения более сложных задач. В отличие от наследования, агрегация позволяет создавать отношения "содержит" между объектами, что делает их менее зависимыми друг от друга.
Пример:
```python
class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Car:
    def __init__(self):
        self.engine = Engine()  # Агрегация - объект класса Engine содержится в объекте класса Car

    def start(self):
        print("Starting the car")
        self.engine.start()

    def stop(self):
        print("Stopping the car")
        self.engine.stop()

my_car = Car()
my_car.start()  # Вывод: Starting the car
                #        Engine started
my_car.stop()   # Вывод: Stopping the car
                #        Engine stopped
```
Ключевое различие между композицией и агрегацией заключается в том, как объекты связаны: в композиции объекты жестко связаны друг с другом, а в агрегации объекты могут быть независимыми.

---

17. РЕАЛИЗАЦИЯ/ИМПЛЕМЕНТАЦИЯ

Описaние:
Контексте программирования означает реализацию конкретного алгоритма или интерфейса на определенном языке программирования. В случае Python, имплементация подразумевает написание кода, который конкретно выполняет задачу или реализует интерфейс. Имплементация в Python может быть использована для создания классов, функций, алгоритмов и других структур данных, которые решают конкретные задачи или реализуют определенный функционал.
Пример:
```python
''' Имплементация класса: '''
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print("Engine started")

# Использование имплементированного класса
my_car = Car("Toyota", "Corolla")
my_car.start_engine()

''' Имплементация алгоритма: '''
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

# Использование имплементированного алгоритма
arr = [1, 3, 5, 7, 9]
target = 5
index = binary_search(arr, target)
print(f"Index of {target} is {index}")
```
---

18. ЗАВИСИМОСТЬ

Описaние:
Означает, что один объект или модуль использует функциональность или данные из другого объекта или модуля. Это позволяет создавать модульные и многокомпонентные программы, где каждая часть имеет чёткие и ограниченные обязанности. Зависимости в Python могут быть установлены как с использованием встроенных модулей, так и с помощью сторонних библиотек. Примеры зависимостей в Python включают библиотеки для работы с базами данных, графическими интерфейсами, математическими вычислениями и многими другими областями.
Пример:
```python
import requests
```