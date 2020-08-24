dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])



dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print(dict.get("School"))
print(dict)

dict['rollNo'] =53


print(dict)
print(dict.pop("rollNo"))

dict['rollNo'] =67

print(dict.popitem())

dict.update({"School":"new School"})

print(dict)
print((dict.keys()))

print(dict.values())

print(dict.items())
