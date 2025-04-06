class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map = {}
        for i in range(len(list1)):
            map[list1[i]] = i
        min = float('inf')
        for j in range(len(list2)):
            if list2[j] in map:
                sum = j + map[list2[j]]
                if sum < min :
                    min = sum
                    res = []
                    res.append(list2[j])
                elif sum == min :
                    res.append(list2[j])  
        return res
                           