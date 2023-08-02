numbers = [9,4,8,10,2,4,8,3,14,4,8]

num = 12

pairs = []

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i]+numbers[j]== num and sorted([numbers[i],numbers[j]]) not in pairs:
            pairs.append(sorted([numbers[i],numbers[j]]))
print(pairs)