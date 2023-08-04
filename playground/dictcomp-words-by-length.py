def count_words_by_length(words):
  """Function to count words by length"""
  # Declaro a Dict
  words_by_length = {}

  if not words:
    return words_by_length
    
  # Itero the words list for create the dict with dict comprehension
  # for word in words:
  #   # Calculate len of the word
  #   len_word = len(word)
  #   if len_word not in words_by_length:
  #     words_by_length[len_word] = 1
  #   else:
  #     words_by_length[len_word] += 1
  # return words_by_length

  # Dictionary comprehension
  words_by_length = {
    len(word): sum(1 for word_in in words if len(word_in) == len(word))
    for word in words
  }
  return words_by_length


if __name__ == '__main__':
  words = ["apple", "banana", "orange", "grapefruit", "pear", "kiwi"]
  words2 = []

  response = count_words_by_length(words)
  print(response)
