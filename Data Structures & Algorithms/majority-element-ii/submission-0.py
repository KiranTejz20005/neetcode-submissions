class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num,0)+1
        
        ans = []

        for key in count:
            if count[key]>len(nums)//3:
                ans.append(key)
        return ans
        