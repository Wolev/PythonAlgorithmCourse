# Interview Question #5
# The problem is that we want to find duplicates in a one-dimensional array of integers in O(N) running time where the
# integer values are smaller than the length of the array!

def find_duplicates(nums):

    # We can achieve O(n) linear running time when N=len(nums)
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = - nums[abs(num)]
        else:
            print("Repetition found: %s" % str(abs(num)))

if __name__ == "__main__":
    # This method cannot handle values < 0
    # the maximum item is smaller than the size of the list
    n = [2, 6, 5, 1, 4, 3, 2]
    find_duplicates(n)