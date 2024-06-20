#LEET CODE QUESTION
'''
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j'''


arr=list(map(int,input("enter the elements:").split()))
target=int(input("enter the target sum:"))
for i in range(len(arr)):
    for j in range(1,len(arr)):
        if arr[i]+arr[j]==target:
            print(i,j)

