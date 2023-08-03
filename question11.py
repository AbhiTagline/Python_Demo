AP = [1,5,8,11,14,17]

diff = 0
# to find out the difference
if AP[1]-AP[0] == AP[2] - AP[1]:
    diff = AP[1] - AP[0]
    print("Got the difference",diff)
elif AP[-1]-AP[-2] == AP[-3] - AP[-4]:  #if first two ap got wrong then will check from last
    diff = AP[-1] - AP[-2]

for i in range(len(AP)-1):
    if AP[i+1] == (AP[i] + diff):
        pass
    else:
        print('This number is wrong',AP[i+1])
        AP[i+1] = AP[i] + diff
print(AP)



GP = [3,9,27,81,244,729]

common_ratio = 0
# to find the common ratio
if GP[1]/GP[0] == GP[2]/GP[1]:
    common_ratio = int(GP[1]/GP[0])
elif GP[-1]/GP[-2] == GP[-2]/GP[-3]:
    common_ratio = int(GP[-1]/GP[-2])


for i in range(len(GP)-2):
    if GP[i+2] == (GP[i+1] * common_ratio):
        pass
    else:
        print('This number is wrong',GP[i+2])
        GP[i+2] = GP[i+1] * common_ratio
print(GP)