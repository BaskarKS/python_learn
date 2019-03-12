import copy
l1 = [10,20,[30,40],50]
l2 = copy.deepcopy(l1)

print("l1 Address : ",id(l1))
print("l2 Address : ",id(l2))

print(l1[2])
print(l2[2])

#l1[0] = 111
print("l1[0] : ",id(l1[0]))
print("l2[0] : ",id(l2[0]))

#l1[1] = 222
print("l1[1] : ",id(l1[1]))
print("l2[1] : ",id(l2[1]))

l1[2][0] = 333
print("l1[2][0] : ",id(l1[2]))
print("l2[2][0] : ",id(l2[2]))

#l1[3] = 555
print("l1[3] : ",id(l1[3]))
print("l2[3] : ",id(l2[3]))

print("l1 : ",l1)
print("l2 : ",l2)