class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x == self.reverse(x)

    def reverse(self, y):
        reversed = 0
        while y > 0:
            digit = y % 10
            reversed = reversed * 10 + digit
            y = y // 10

        return reversed