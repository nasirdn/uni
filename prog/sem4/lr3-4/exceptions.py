class BinaryTreeException(Exception):
  """Basic class for binary tree exception"""

class HeightException(BinaryTreeException):
  """Class for height exceptions"""

class HeightBelowZeroException(HeightException):
  """Class for height below zero exceptions"""

class HeightIsNotAnIntegerException(HeightException):
  """Class for height is not an integer exceptions"""

class RootIsNotANumberException(BinaryTreeException):
  """Class for root is not a number exceptions"""