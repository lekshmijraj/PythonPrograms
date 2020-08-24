list1 = ['physics', 'chemistry', 1997, 2000]

list2 = [1, 2, 3, 4, 5, 6, 7 ]
list3 = list(["a", "b", "c", "d"])

print(list1)

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

print ("Value available at index 2 : "+ str(list1[2]))


list1[2] = 2001

print(list1)
print( "New value available at index 2 : " + str(list1[2]))

del list1[2];
print ("After deleting value at index 2 : " +  str(list1))

x=list1.index("chemistry")
print("index of given element in list 1 is : " + str(x))

list2 = [1, 2, 3, 4, 5, 6, 7 ]

print(list2[1:6])
print(list2[-6:-1])
print(list2[-6:-1:])