# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1, 2, 5, 2, 5, 1, 3, 7, 9]
# Expected Result : [2, 4, 6, 8]

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newLi = []
c = 0

for num in li:
 
    if num % 2 == 0:
    	newLi.append(num)
print(newLi)