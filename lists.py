# lists are used to store multiple vales of different data types
# lists can be modified
# created by using []




# basic of list
names = ["Madan", "Mohan", "Harsha", "Modi", "Virat", "Kohli"]
#index      0        1         2......
#index     -6       -5        -4......
dates = [6,3,2,8,9,4]
print(names)


print("")
# to the list to another variable
copy = names.copy()

print("")
# list position
print(names[1])
print(names[5])
print(names[3])

print("")
# from to where positions
print(names[2:4])
print(names[::2])

print("")
# changing values
names[3] = "Kiran"
print(names)

print("")
# adding another list
names.extend(dates)
print(names)

print("")
# adding values to the list at last
names.append("Modi")
print(names)

print("")
# adding values at specific position
names.insert(3, "Narendra")
print(names)

print("")
# remove elements in list
names.remove("Narendra")
names.remove("Modi")
print(names)

print("")
# remove last element in the list
names.pop()
print(names)

print("")
# to know the index of the element
print(names.index("Kohli"))

print("")
# to count the frequency of the element
print(names.count("Virat"))

print("")
# to sort the number in the list in order
dates.sort()
print(dates)
copy.sort()
print(copy)