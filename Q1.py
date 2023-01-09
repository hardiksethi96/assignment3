string = input("Enter a string: ")
string = string.lower()
if len(string.split()) == 1:
  char_count = {}
  for char in string:
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1
  print("Character Count:", char_count)
else:
  word_count = {}
  for word in string.split():
    if word in word_count:
      word_count[word] += 1
    else:
      word_count[word] = 1
  print("Word Count:", word_count)
