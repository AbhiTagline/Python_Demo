AP = [1,5,8,11,14,17]

diff = 0
# to find out the difference
if AP[1]-AP[0] == AP[2] - AP[1]:
    diff = AP[1] - AP[0]
    print("Got the difference",diff)
elif AP[-1]-AP[-2] == AP[-3] - AP[-4]:  #if first two ap got wrong then will check from last
    diff = AP[-1] - AP[-2]

for i in range(len(AP)-1):
    print(AP[i+1] == (AP[i] + diff))
    if AP[i+1] == (AP[i] + diff):
        pass
    else:
        print('This number is wrong',AP[i+1])
        AP[i+1] = AP[i] + diff
        break
print(AP)