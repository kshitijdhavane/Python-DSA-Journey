
# LeetCode 217: Contains Duplicate
# Problem: https://leetcode.com/problems/contains-duplicate/
# Approach: Frequency Dictionary
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for num in nums:
            if frequency[num] >= 2:
                return True

        return False
