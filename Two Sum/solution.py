class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j])==target:
                    if nums[i] not in lis and nums[j] not in lis:
                        lis.append(i)
                        lis.append(j)
        return lis
                    
        