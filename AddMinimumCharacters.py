# User function Template for python3
# AAAAAB -> BAAAAAB -> 1
# AAB -> BAAB -> 1
# AABCD -> DCBAABCD -> 3
# ABCDEFGHIJKJIHGFEDCBA -> 0
# UMUB -> BUMUB -> 1
# AABBAACBD


class Solution:
    lenStartingPalindrome = 1

    def isPalindrome(self, str1):
        if len(str1) > 1:
            strRev = str1[::-1]
            if len(str1) % 2 == 0:
                firstHalf = str1[:len(str1) // 2]
                secondHalf = strRev[:len(str1) // 2]
                return bool(firstHalf == secondHalf)
            else:
                firstHalf2 = str1[:len(str1) // 2 + 1]
                secondHalf2 = strRev[:len(str1) // 2 + 1]
                return bool(firstHalf2 == secondHalf2)
        else:
            return False

    def hasPalindrome(self, str1):
        newStr = str1[:1]
        for i in range(len(str1)):
            if self.isPalindrome(newStr):
                return True
            else:
                if i + 1 < len(str1):
                    newStr += str1[i + 1]
                    self.lenStartingPalindrome += 1
        return False

    def addMinChar(self, str1):
        if self.isPalindrome(str1):
            print("is palindrome")
            return 0
        elif self.hasPalindrome(str1):
            print("has palindrome")
            return len(str1) - self.lenStartingPalindrome
        else:
            print("is or has no palindrome")
            # count = 0
            # firstLetter = str1[0]
            # for i in range(len(str1)):
            #     if str1[i] == firstLetter:
            #         count += 1
            #     else:
            #         break
            # if count > 1:
            #     return len(str1) - count
            # else:
            return len(str1) - 1


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
