def findMaxAverage(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
       
    maxSum=sum(nums[0:k])#/ç
    maxAvg=maxSum/(1.0*k)
    
    for i in xrange(1,len(nums)-k+1):
        maxSum=maxSum-nums[i-1]+nums[i+k-1]
        maxAvg=max(maxSum/(1.0*k),maxAvg)
    return maxAvg