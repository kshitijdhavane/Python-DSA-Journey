
# LeetCode 1903: Largest Odd Number in String
# Problem: https://leetcode.com/problems/largest-odd-number-in-string/
# Approach: Greedy / Two Pointers (scan from right)
# Time Complexity: O(n)
# Space Complexity: O(1) extra space, excluding the returned substring

class Solution(object):
    def largestOddNumber(self, num):
        right = len(num) - 1

        while right >= 0:
            if int(num[right]) % 2 != 0:
                return num[:right + 1]

            right -= 1

        return ""



if __name__ == "__main__":
    solution = Solution()

    num = "35427"
    result = solution.largestOddNumber(num)

    print("Input:", num)
    print("Largest odd number:", result)
