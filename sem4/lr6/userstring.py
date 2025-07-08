from collections import UserString

def userstring_example():

  class MyString(UserString):

    def __init__(self, data=None):
      super().__init__(data)

  my_string = MyString('Laboratory work 6')
  print(my_string.upper())
