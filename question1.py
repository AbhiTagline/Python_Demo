# Question1
from collections import Counter
choice = input("A. Length of list\nB. Display first 3 numbers\nC. Display sum of odd numbers\nD. Number of duplicate numbers\nE. Display list without duplicate numbers\nEnter Your choice: ")
numbers  = [2,4,5,2,12,44,5,1,2,3,]
if choice.lower()=="a":
    print("Length of list: ",len(numbers))
elif choice.lower()=="b":
    print("First 3 numbers: ",numbers[:3])
elif choice.lower()=="c":
    print("Sum of odd numbers",sum([x for x in numbers if x%2!=0]))
elif choice.lower()=="d":
    duplicate_numbers = Counter(numbers)
    duplicate_numbers_lists = [x for x,y in duplicate_numbers.items() if y>=2]
    print(duplicate_numbers_lists)
    print("Number of duplicate numbers: ",len(duplicate_numbers_lists),duplicate_numbers_lists,"repeats")
elif choice.lower()=="e":
    print("List without duplicate numbers: ",list(set(numbers)))
