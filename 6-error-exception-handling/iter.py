# Iter() function is iterar a range manually

# Iter with for
for i in range(1, 10):
  print(i)

# Iter with iter()
my_iter = iter(range(1, 4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))