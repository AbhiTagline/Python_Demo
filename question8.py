numbers = [2, 5, 6, 1, 3, 8, 9, 10]

for i in range(len(numbers)-1):
    for j in range(len(numbers)-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
print(numbers)