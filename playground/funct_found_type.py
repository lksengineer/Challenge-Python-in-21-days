"""
Function that takes a parameter called value.
Must and return the data type of the value parameter.
"""


def found_type(value):
  """
  Title: Function Found type
  Description: Found and return the value parameter
  parameter: Value
  """
  return type(value)


if __name__ == '__main__':
  value = 1.5
  print(found_type(value))  # <class 'float'>
