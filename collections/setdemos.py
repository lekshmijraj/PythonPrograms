thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset = set(("apple", "banana", "cherry"))

print("banana" in thisset)


thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)

thisset.pop()

print(thisset)