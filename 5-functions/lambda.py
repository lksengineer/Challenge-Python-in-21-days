# Function anonymous: Lambda

# Function Normal
def increment(x):
  return x + 1


result = increment(10)
print(result)


# Lambda Function
increment_v2 = lambda x: x + 1

result = increment_v2(10)
print(result)

result = increment_v2(20)
print(result)


# Lambda Function 2
full_name = lambda name, last_name: f'Full name: {name.title()} {last_name.title()}'

text = full_name('nicolas', 'perez casas')
print(text)