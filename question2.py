names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']
print("Names :", names)


length = [len(x) for x in names]
print("Name lengthd:",length)


nlst = list(set(length))
nlst.sort()
count = 0
for i in nlst[:3]:
    print(length.count(i),"names of length",i,[x for x in names if len(x) == nlst[count]])
    count += 1



print("The three least frequent name lengths are")
count = 0
for i in nlst[-3:]:
    print(length.count(i),"names of length",i,[x for x in names if len(x) == nlst[count]])
    count += 1
