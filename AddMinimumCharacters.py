class Solution:
    @staticmethod
    def isPalindrome(s):
        if s == s[::-1]:
            return True
        return False

    def addMinChar(self, s):
        lenRemoved = 0
        while not self.isPalindrome(s):
            lenRemoved += 1
            s = s[:-1]
        return lenRemoved


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str1 = input()

        ob = Solution()
        print(ob.addMinChar(str1))

# } Driver Code Ends
