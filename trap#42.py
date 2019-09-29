
# time: O(N), space: O(1)

class Solution(object):
    def trap(self, arr):
        water=0
        left, right= 0, len(arr)-1
        leftwall, rightwall= 0, 0
        while left < right:
            if arr[left] < arr[right]:
                if leftwall < arr[left]:
                    leftwall= arr[left]

                else:
                    water+=leftwall-arr[left]
                    left+=1
            else:
                if rightwall < arr[right]:
                    rightwall= arr[left]
                else:
                    water+=rightwall-arr[right]
                    right-=1
        return water


arr=[0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(arr))
