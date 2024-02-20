sentence = input()
# 🚨 Don't change code above 👆
# Write your code below 👇
def sentence_to_list(sentence):
  words = sentence.split()
  return words
words = sentence_to_list(sentence)

result ={word:len(word) for word in words}

print(result)