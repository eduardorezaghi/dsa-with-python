class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets: list[list[int]] = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            lo = i + 1
            hi = len(nums) - 1
            
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if total == 0:
                    triplets.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif total < 0:
                    lo += 1
                else:
                    hi -= 1
                    
        return triplets


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
    print(s.threeSum([])) # []
    print(s.threeSum([0])) # []
    print(s.threeSum([0,0,0])) # [[0,0,0]]