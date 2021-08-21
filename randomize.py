import random
test = list(range(15))
print(test)
#O(n) algorithm for randomizing an array 
for elem in range(0,len(test)-1):
    num = random.randint(1,len(test)-1)
    temp = test[elem]
    test[elem] = test[num]
    test[num] = temp

print(test)


