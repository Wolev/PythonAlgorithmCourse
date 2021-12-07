print("Hello World from PyCharm and Python")

array = [10, 3, 7, 5, 34, 14, 18]

# In Java you can't do this
array1 = [0.0, 1, 'me', 3]


print(array)
print(array[:])
print(array[0:])
print(array[0:2])
print(array[:-1]) # prints the array execept the last element
print(array1[2] + "\n")

# Linear search O(n)

max = array[0]
min = array[0]

for item in array:
    if item > max:
        max = item
    if item < min:
        min = item

print("The max number in the array is " + str(max) + ".")
print("The min number in the array is " + str(min) + ".")