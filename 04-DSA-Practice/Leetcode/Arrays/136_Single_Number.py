
# LeetCode 136: Single Number
# Problem: https://leetcode.com/problems/single-number/
# Approach: Frequency Dictionary
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def singleNumber(self, nums):
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for num in nums:
            if frequency[num] == 1:
                return num

        return None



# Local testing in VS Code (not required on LeetCode)
if __name__ == "__main__":
    solution = Solution()

    nums = [4, 1, 2, 1, 2]
    result = solution.singleNumber(nums)

    print("Input:", nums)
    print("Single Number:", result)
