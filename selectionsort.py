arr = [9,8,7,6,5]
c=0
def selection(nums):
    n = len(nums)
    global c
    for i in range(n-1):
        chhotu = i

        for j in range(i+1, n):
            c+=1
            if nums[chhotu] > nums[j]:
                chhotu = j

        if chhotu != i:
            t = nums[chhotu]
            nums[chhotu] = nums[i]
            nums[i] = t

    return nums

print(selection(arr))
print("total hits=",c)