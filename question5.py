numbers = [9,4,8,10,2,4,8,3,14,4,8,5,6,7,3,4,5,23,1,2,3,4,5,6,7,8,9,00,0,00,0,00,0,00,000,0,00,6656,5,454,5,453,4,23,23,4,454,56,57,676,7,443,43,45,6567,67,64,545,456,5656,56756,765,4545,44,43,4,44,33345,5,6,677,77,7,77,7,77,5,544,5,45,45,6,677776754,34,23454,3453,454,645,4532,3,354564,56]

num = 12

pairs = []

for i in range(len(numbers)):
    for j in range(len(numbers)):
        sorted_pair = sorted([numbers[i],numbers[j]])
        if numbers[i]+numbers[j] == num and sorted_pair not in pairs:
            pairs.append(sorted_pair)
print(pairs)

