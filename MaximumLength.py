# User function Template for python3

class Solution:
    def solve(self, a, b, c):
        # code here
        mx = max(a, b, c)
        thr = ((a + b + c - mx) * 2) + 2
        if mx > thr:
            s = -1
        else:
            s = a + b + c
        return s


# {
# Driver Code Starts
# Initial Template for Python 3

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    obj = Solution()
    res = obj.solve(a, b, c)

    print(res)
# } Driver Code Ends

"""
1
3 3 3
"""
