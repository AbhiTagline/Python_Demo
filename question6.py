string = "PQRQRQRQ"

substring = "QRQ"

count = 0
for i in range(len(string)-len(substring)+1):
    if substring in string[i:len(substring)+i]:
        count += 1

print(count)
