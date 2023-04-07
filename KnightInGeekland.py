# User function Template for python3

class Solution:
    def knightInGeekland(self, arr, start):
        arr.


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        n, m = map(int, input().split())
        starting_x, starting_y = map(int, input().split())
        orignal_array = []

        for i in range(n):
            l = list(map(int, input().split()))
            orignal_array.append(l)

        res = Solution().knightInGeekland(orignal_array, [starting_x, starting_y])
        print(res)
# } Driver Code Ends
