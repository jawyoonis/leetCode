class Solution:
    def anagrams(self, strs):
        hashtable={}
        result=[]
        for i in strs:
            sortedwords= " ".join(sorted(i))
            print(sortedwords)
            if sortedwords not in hashtable:
                hashtable[sortedwords]= [i]
            else:
                hashtable[sortedwords].append(i)
        for item in hashtable.values():
            result.append(item)
        return result 





print(Solution().anagrams(["eat","tea","tan","ate","nat","bat"]))





