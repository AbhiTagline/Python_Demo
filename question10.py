
# for the first pattern i have two different solutions 
# solution 1
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(rows-1-i):
        print("*",end=" ")
    for j in range(i*2+1):
        print(" ", end=" ")
    for j in range(rows-1-i):
        print("*",end=" ")
    print()
for i in range(rows-1,0,-1):
    for j in range(rows-i):
        print("*",end=" ")
    for j in range(i*2-1):
        print(" ", end=" ")
    for j in range(rows-i):
        print("*",end=" ")
    print()
# solution 2
rows = int(input("Enter number of rows: "))
for i in range(rows//2+1):
    print("* "*((rows-2)-i)+"  "*(i*2+1)+"* "*((rows-2)-i))
for j in range(rows//2,0,-1):
    print("* "*(rows-j-1)+"  "*(j*2-1)+"* "*(rows-j-1))
# kite Pattern 
rows = int(input("Enter number of rows: "))
for i in range(rows//2+1):
    print("  "*((rows-2)-i)+"* "*(i*2+1))
for j in range(rows//2,0,-1):
    print("  "*(rows-j-1)+"* "*(j*2-1))
# hollow triangle pattern 
rows = int(input("Enter number of rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        if j==1 or i==j or i==rows:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# hollow rectangle pattern
rows = int(input("Enter the number of rows: "))
for i in range(rows+1):
    for j in range(rows+1):
        if j==0 or j==rows or i == 0 or i==rows:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# number pattern
k = 1
for i in range(1,6):
    for j in range(i):
        print(k, end=" ")
        k += 1
    print()