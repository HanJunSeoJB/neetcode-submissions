class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i <= j:
            t = numbers[i] + numbers[j]
            # mid = (i + j) // 2
            print(numbers[i], numbers[j])
            if t == target:
                return [i+1, j+1]

            elif t > target:
                j -= 1

            elif t < target:
                i += 1
        return []