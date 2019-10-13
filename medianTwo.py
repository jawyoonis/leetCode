class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1+nums2
        nums.sort()
        median = 0.00
        l = len(nums)
        if l%2==0:
            n= int(l/2)
            
            median= (nums[n-1]+nums[n])/2
        else:
            n= int(l/2)
            median= nums[n]
        return median
arr=[1,2,3,4]
arr1=[1,2,3,7]


print(Solution().findMedianSortedArrays(arr, arr1))
