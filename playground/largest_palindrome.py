def find_largest_palindrome(words):
  """Function Find Largest Palindrome"""
  palindromes = [word for word in words if word == word[::-1]]
  print(palindromes)



if __name__ == '__main__':
  words = ["oso", "racecar", "lLevel", "o  soi", "world", "hello"]
  words2 = ["Platzi", "Python", "django", "flask"]

  response = find_largest_palindrome(words)
  print(response)