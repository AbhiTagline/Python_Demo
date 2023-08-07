from collections import Counter

sentences = ["My name is Ram", "He is a good person", "You should be careful while coding", "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen"]

words = [word for sentence in sentences for word in sentence.split()]
print(words)

word_count = Counter(words)
print(word_count)