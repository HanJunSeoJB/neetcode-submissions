class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s1 = set(nums)
        result = 0
        def parse(arr, target):
            if target+1 in s1 and target+1 not in arr:
                arr.append(target+1)
                return parse(arr, target+1)
            if target-1 in s1 and target-1 not in arr:
                arr.append(target-1)
                return parse(arr, target-1)
            return arr
        for num in s1:
            answer = parse([num], num)
            result = max(result, len(answer))    
        
        return result
            
        