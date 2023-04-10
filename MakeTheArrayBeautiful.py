from typing import List


class Solution:
    def isBeautiful(self, arr: List[int]) -> bool:
        for i in range(1, len(arr)):
            if arr[i - 1] >= 0 > arr[i] or arr[i - 1] < 0 <= arr[i]:
                return False
        return True

    def makeBeautiful(self, arr: List[int]) -> List[int]:
        # code here
        is_beautiful = self.isBeautiful(arr)
        # print("isBeautiful: ", is_beautiful)
        # print("arr:", arr)
        if not is_beautiful:
            for i in range(1, len(arr)):
                if arr[i - 1] >= 0 > arr[i] or arr[i - 1] < 0 <= arr[i]:
                    # print("Deleting ", arr[i - 1], arr[i])
                    arr.pop(i - 1)
                    arr.pop(i - 1)
                    break
            self.makeBeautiful(arr)
        return arr


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
"""
