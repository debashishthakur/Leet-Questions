def twoSum(self, nums, target):
    hm = {}
    for i,n in enumerate nums:
    diff = target - n
    if diff in hm:
        return hm[diff],i
    else:
        hm[n] = i
