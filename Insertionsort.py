# onlineshorting 
arr = [4,5,6,7,1,2,3]

def insertionSort(nums):
    n = len(nums)

    for i in range(1, n):
        j = i
        while j > 0 and nums[j] < nums[j-1]:
            t = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = t
            j = j - 1

    return nums

print(insertionSort(arr))