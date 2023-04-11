# {
# Driver Code Starts
# Initial Template for Python 3

class Shop:
    chocolates = []
    countOfCalls = 0

    def __init__(self):
        self.chocolates = []
        self.countOfCalls = 0

    def addChocolate(self, price):
        self.chocolates.append(price)

    def get(self, i):
        self.countOfCalls += 1
        if self.countOfCalls > 50 or i >= len(self.chocolates) or i < 0:
            print("countOfCalls = ", self.countOfCalls)
            return -1

        return self.chocolates[i]


# } Driver Code Ends
# User function Template for python3

"""
Instructions - 

    1. 'shop' is object of class Shop.
    2. User 'shop.get(int i)' to enquire about the price
            of the i^th chocolate.
    3. Every chocolate in shop is arranged in increasing order
            i.e. shop.get(i) <= shop.get(i + 1) for all 0 <= i < n - 1
"""


class Solution:
    shop = Shop()

    def __init__(self, shop):
        self.shop = shop

    def find(self, n, k):
        afford = 0
        while k > 0:
            for i in reversed(range(len(self.shop.chocolates))):
                # print("k = ", k, " i = ", i)
                if k >= self.shop.get(i):
                    # print("buying ", self.shop.get(i))
                    k -= self.shop.get(i)
                    afford += 1
                    break
        return afford


"""
4 9
1 2 3 4
"""

# {
# Driver Code Starts.

if __name__ == '__main__':
    tc = 1
    while tc > 0:
        shop = Shop()
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        for choco in arr:
            shop.addChocolate(choco)
        ob = Solution(shop)
        ans = ob.find(n, k)
        print("ret = ", ans)
        tc -= 1

# } Driver Code Ends
