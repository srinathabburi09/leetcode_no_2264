class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        largest = ""
        for i in range(n-2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                target = num[i] * 3
                if target > largest:
                    largest = target
        return largest


        
