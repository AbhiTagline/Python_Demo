# Question1 

choice = input("A. Length of list\nB. Display first 3 numbers\nC. Display sum of odd numbers\nD. Number of duplicate numbers\nE. Display list without duplicate numbers\nEnter Your choice: ")
numbers = [2,4,5,2,12,44,5,1,2,3]
if choice.lower()=="a":
    print("Length of list: ",len(numbers))
elif choice.lower()=="b":
    print("First 3 numbers: ",numbers[:3])
elif choice.lower()=="c":
    print("Sum of odd numbers",sum([x for x in numbers if x%2!=0]))
elif choice.lower()=="d":
    unique_numbers = []
    repitative_numbers = []
    for i in numbers:
        if i not in unique_numbers:
            unique_numbers.append(i)
        else:
            repitative_numbers.append(i) 
    common_elements = set(repitative_numbers[::])
    print("Number of duplicate numbers: ",len(common_elements),tuple(common_elements),"repeats")
elif choice.lower()=="e":
    print("List without duplicate numbers: ",list(set(numbers)))
