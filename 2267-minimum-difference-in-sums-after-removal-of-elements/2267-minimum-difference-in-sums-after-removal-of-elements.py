class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        k=n//3
        leftmins=[0]*n
        rightmax=[0]*n
        maxleft=[]
        leftsum=0
        for i in range(k):
            heapq.heappush(maxleft, -nums[i])
            leftsum += nums[i]
        leftmins[k-1]=leftsum
        for i in range(k, n-k):
            if nums[i]< -maxleft[0]:
                leftsum += nums[i] + heapq.heappop(maxleft)
                heapq.heappush(maxleft, -nums[i])
            leftmins[i] = leftsum
        minright=[]
        rightsum=0
        for i in range(n-1, n-k-1, -1):
            heapq.heappush(minright,nums[i])
            rightsum += nums[i]
        rightmax[n-k]=rightsum
        for i in range(n-k-1, k-2,-1):
            if nums[i]>minright[0]:
                rightsum += nums[i] - heapq.heappop(minright)
                heapq.heappush(minright,nums[i])
            rightmax[i] = rightsum
        mindiff = float('inf')
        for i in range(k-1, n-k):
            mindiff=min(mindiff, leftmins[i]-rightmax[i+1])
        return mindiff
        