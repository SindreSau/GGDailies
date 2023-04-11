from typing import List


class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        stack = []
        for i in range(len(arr)):
            if len(stack) == 0:
                stack.append(arr[i])
            elif stack[len(stack) - 1] >= 0 > arr[i] or stack[len(stack) - 1] < 0 <= arr[i]:
                stack.pop(len(stack) - 1)
            else:
                stack.append(arr[i])
        return stack


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())

        arr = list(map(int, input().split()))

        obj = Solution()
        res = obj.makeBeautiful(arr)
        print(*res)
# } Driver Code Ends

"""
1
8
2 1 -4 3 -5 2 6 -3

1
7
-3 -1 -19 0 6 -13 12

1
28
186 156 -145 148 52 160 128 -133 86 -199 54 -29 62 116 -37 -137 168 -69 -103 -127 80 58 -161 124 -115 -21 0 -37

1
41
-145 -69 56 -123 84 76 -49 -169 -141 -173 -79 -71 82 -87 162 182 -73 -151 -95 -195 10 42 24 -171 184 44 54 -141 110 58 186 -39 -47 -69 -87 148 -111 32 -189 92 32
"""
