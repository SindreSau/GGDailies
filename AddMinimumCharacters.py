class Solution:
    def addMinChar(self, s):
        if s == s[::-1]:
            return 0
        i = 0
        j = len(s) - 1
        ans = j
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                ans -= 1
                i = 0
                j = ans
        return len(s) - (ans + 1)


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
