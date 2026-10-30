class Solution(object):
    def largestOddNumber(self, num):
        
        right = len(num) - 1

        while right >= 0:
            if int(num[right]) % 2 != 0:
                return num[:right + 1].lstrip("0")

            right -= 1

        return ""
