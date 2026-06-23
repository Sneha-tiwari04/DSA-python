# onlineshorting 
arr = [1,2,3,4,5]
c=0

def insertionSort(nums):
    global c 
    n = len(nums)
    for i in range(1, n):
        j = i
        while j > 0 and nums[j] < nums[j-1]:
            c=+1
            t = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = t
            j = j - 1

    return nums

print(insertionSort(arr))
print("total hits=",c)