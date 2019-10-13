class Solution(object):
    def threeSum(self, arr, targetSum):
        arr= sorted(arr)

        triplets=[]
        for i in range(len(arr)-1):
            left=i+1
            right= len(arr)-1
            while left < right:
                currentSum= arr[i] + arr[left]+ arr[right]
                if currentSum==targetSum:
                    triplets.append((arr[i], arr[left], arr[right]))
                    left+=1
                    right-=1
                elif currentSum< targetSum:
                    left+=1
                elif currentSum > targetSum:
                    right-=1
        return triplets 




print(Solution().threeSum([1,2,3,4,5,6], 9))


