
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



