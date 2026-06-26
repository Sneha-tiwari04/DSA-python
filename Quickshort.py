arr = [9,8,7,6,5]
def part (nums,l,r):
    k=nums[r]
    start=l
    for i in range (l, r+1):
        if nums[i]<k:
            t=nums[i]
            nums[i]=nums[start]
            nums[start]=t
            start=start+ 1
    return start-1
