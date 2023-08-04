# def find_largest_palindrome(words):
#   """Function Find Largest Palindrome"""
#   max_word = max([len(word) for word in words])
#   aux = 0
  
#   for word in words:
#     word = word.replace(" ", "").lower()
#     if word == word[::-1] and len(word) == max_word:
#       aux += 1
#       return (word)
#   if aux == 0:
#     return None
      
# if __name__ == '__main__':
#   words = ["oso", "racecar", "lLevel", "o  soi", "world", "hello"]
#   words2 = ["Platzi", "Python", "django", "flask"]

#   response = find_largest_palindrome(words)
#   print(response)

def find_largest_palindrome(words):
  """Function Find Largest Palindrome"""
  # max_word = max([len(word) for word in words])
  max_word = 0
  palindrome = ""
  
  for word in words:
    word = word.replace(" ", "").lower()
    if word == word[::-1] and len(word) > max_word:
      max_word = len(word)
      palindrome = word
  return palindrome if palindrome else None


if __name__ == '__main__':
  words = ["oso", "racecar", "lLevel", "o  soi", "world", "hello"]
  words2 = ["Platzi", "Python", "django", "flask"]

  response = find_largest_palindrome(words2)
  print(response)