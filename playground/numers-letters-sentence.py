def count_letters(phrase):
  """Function to count the numbers of letters in a phrase"""
  total_letters = {}

  # Bucle for iterar the letter in phrase
  for letter in phrase:

    # Conditional for count the numbers of letters in the phrase
    if letter not in total_letters:
      total_letters[letter] = 1
    else:
      total_letters[letter] += 1
  return total_letters

if __name__ == '__main__':
  phrase = "Hola mundo"
  response = count_letters(phrase)
  print(response)
