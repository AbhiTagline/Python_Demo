# Question1 

choice = input("A. Length of list\nB. Display first 3 numbers\nC. Display sum of odd numbers\nD. Number of duplicate numbers\nE. Display list without duplicate numbers\nEnter Your choice: ")
lst = [2,4,5,2,12,44,5,1,2,3]
if choice.lower()=="a":
    print("Length of list: ",len(lst))
if choice.lower()=="b":
    print("First 3 numbers: ",lst[:3])
if choice.lower()=="c":
    print("Sum of odd numbers",sum([x for x in lst if x%2!=0]))
if choice.lower()=="d":
    nlst = []
    result = []
    for i in lst:
        if i not in nlst:
            nlst.append(i)
        else:
            result.append(i) 
    print("Number of duplicate numbers: ",len(set(result)),tuple(set(result[::])),"repeats")
if choice.lower()=="e":
    print("List without duplicate numbers: ",list(set(lst)))
