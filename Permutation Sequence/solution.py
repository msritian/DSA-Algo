class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums=[]
        fact=1
        for i in range(1,n):
            fact=fact*i
            nums.append(i)
        nums.append(n)
        k=k-1
        ans= ""
        while(True):
            ans=ans+str(nums[int(k/fact)])
            nums.pop(int(k/fact))
            if len(nums)==0:
                break
            k=k%fact
            fact=fact/len(nums)
        return ans