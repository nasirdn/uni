from collections import UserList

def userlist_example():

  class MyList(UserList):

    def __init__(self, data=None):
      super().__init__(data)

  my_list = MyList([1, 2, 3, 4])
  my_list.append(5)
  print(my_list)
