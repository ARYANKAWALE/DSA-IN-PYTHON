from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = len(digits) - 1

        while last >=0:
            if(digits[last] < 9):
                digits[last] = digits[last] + 1
                return digits
            else:
                digits[last] = 0
                last -= 1
        digits.insert(0,1)
        return digits
obj = Solution()
print(obj.plusOne([4]))