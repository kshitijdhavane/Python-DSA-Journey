
# LeetCode 344: Reverse String
# Problem: https://leetcode.com/problems/reverse-string/
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1) extra space

class Solution:
    def reverseString(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1



if __name__ == "__main__":
    solution = Solution()

    s = ["h", "e", "l", "l", "o"]
    solution.reverseString(s)

    print("Reversed String:", s)
