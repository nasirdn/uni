from collections import UserDict

def userdict_example():

  class MyDict(UserDict):

    def __init__(self, data=None, **kwargs):
      super().__init__(**kwargs)
      self.data = data if data is not None else {}

  my_dict = MyDict({'one': 1, 'two': 2})
  print(my_dict['one'])
