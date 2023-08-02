sentences = ["My name is Ram", "He is a good person", "You should be careful while coding", "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen"]

word_tree = [z for x in [y.split(" ") for y in sentences] for z in x]
print(word_tree)

dict = {x:word_tree.count(x) for x in word_tree }
print(dict)