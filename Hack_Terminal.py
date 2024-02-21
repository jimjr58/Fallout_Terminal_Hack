#Hack Terminal
import re
inputString = input('Please enter the potential passwords sperated by a space:')
word_list = inputString.split()
# word_list = ['walk', 'guns', 'rude', 'free','foes', 'make'] # words for test
def find_word_with_most_common_letters(words):  #Find word to guess using the one with the most common letters
  word_length = len(words[0])
  max_common_letters = 0
  word_with_most_common_letters = ""

  for word in words:
    common_letters = 0
    compared_words = list(filter(lambda x: x != word, words))
    for i in range(word_length):
      if any(word[i] == w[i] for w in compared_words):
        common_letters += 1

    if common_letters > max_common_letters:
      max_common_letters = common_letters
      word_with_most_common_letters = word

  return word_with_most_common_letters

def find_words_with_likeness(word, word_list, target_likeness):  # If first guess is incorrect find the next possible guess by likeness
  word_length = len(word)
  words_with_target_likeness = []
  for item in word_list:
    likeness = 0
    for i in range(word_length):
      if item[i] == word[i]:
        likeness += 1
    if likeness == target_likeness:
      words_with_target_likeness.append(item)
  return words_with_target_likeness

def is_affirmative(response):
  # Define a regular expression pattern to match affirmative responses
  affirmative_pattern = re.compile(r'\b(?:y|yes|yeah|yep|yup|sure|ok|okay|true|1)\b', re.IGNORECASE)

  # Use the search method to find a match in the response
  match = re.search(affirmative_pattern, response)

  # If a match is found, return True (response is affirmative), otherwise return False
  return bool(match)

# Example usage

result = find_word_with_most_common_letters(word_list)
print(result)
word = result

success = (input('Was that the correct password? '))
if is_affirmative(success):
  print ('Great!')
else:
  likeness = int(input('What was the likeness?'))
  # Remove guessed word from list and use likeness to determine the next best possible guesses
  word_list.remove(word)
  likeness_list = find_words_with_likeness(word, word_list, likeness)
  print(likeness_list)
