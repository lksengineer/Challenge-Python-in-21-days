"""Higher order function:
Function que recibe como parametro otra function(recomendable lambda)
"""

# 1. 
# Higher order function with a Regular function
# Regular function
def increment(x):
  return x + 1

def high_ord_func(x, func):
  return x + func(x)

result = high_ord_func(2, increment)
print(result) # 2 + (2 + 1) = 5


# Higher order function With LAmbda Function
increment_v2 = lambda x: x +1

# Higher order function
high_ord_func_v2 = lambda x, func: x + func(x)

result = high_ord_func_v2(2, increment_v2)
print(result)

result = high_ord_func_v2(2, lambda x: x + 2)
print(result)

## change
result = high_ord_func_v2(2, lambda x: x * 5)
print(result)
