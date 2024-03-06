# list
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# Access list1 items
print(list1[1])
print(list1[-2])
print(list1[1:3])
print(list1[:4])
print(list1[2:])
print(list1[-3:-1])
if "kiwi" in list1:
  print("Yes, 'kiwi' is in the fruits list")

# Change list1 items
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
list1[3] = "watermelon"
print(list1)
list1[1:3] = ["strawberry", "watermelon"]
print(list1)
list1[1:3] = ["watermelon"]
print(list1)

# Insert list1 items
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
list1.insert(2, "watermelon")
print(list1)

# Add list1 items
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# use append() method
list1.append("orange")
print(list1)

# Extend list1 items
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
tuple1 = ("kiwi", "orange")
list1.extend(tuple1)
print(list1)

# Remove list1 items
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
list1.remove("banana")
print(list1)
list1.pop(3)
print(list1)
list1.pop()
print(list1)

# Delete entire list
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
del list1
# Clear list1 using clear() method
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
list1.clear()
print(list1)

# loops through list
# for loop
list1 = ["apple", "banana", "cherry"]
for x in list1:
  print(x)
for i in range(len(list1)):
  print(list1[i])
# while loop by using len() funtion
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Sort list1 items by using sort() function
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
list1.sort()
print(list1)
list1.sort(reverse = True)
print(list1)
# Case insensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Copy list1 items by using copy() function
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Join 2 lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# joining and extending list items work same



