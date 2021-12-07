# The problem is that we want to reverse a T[] array in O(N) linear time complexity and we want the algorithm
# to be in-place as well - so no additional memory can be used!

def reverse(array):

    startPoint = 0
    endPoint = len(array) - 1

    while startPoint < endPoint:
        array[startPoint], array[endPoint] = array[endPoint], array[startPoint]
        startPoint += 1
        endPoint -= 1
        print(array)

if __name__ == '__main__':
    array = [0, 1, 2, 3, 4, 5, 6]
    reverse(array)
    print("\nFinal array is: " + str(array))

'''
for item in range(0, num - 1):
    while startPoint < endPoint:
        array[startPoint], array[endPoint] = array[endPoint], array[startPoint]
        startPoint += 1
        endPoint -= 1
        print(array)
    if startPoint == endPoint:
        break
'''

