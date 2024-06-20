''' sir logic
n=int(input())
arr=list(map(int,input().split()))
pro=0
dlist=[]
k=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]+arr[j]==18:
            if arr[i]>arr[j]:
                k=arr[i]*arr[j]
            if k>pro:
                pro=k
                dlist.append(arr[i])
                dlist.append(arr[j])
print(dlist)                        
'''

''' bull logic'''
def max_prod_sum(n,arr):
    max_prod=0
    cur_prod=0
    #d=[]
    for i in range(len(arr)-1):
        for j in range(len(arr)):
            if arr[i]+arr[j]==18 and arr[i]>arr[j]:
                cur_prod=arr[i]+arr[j]
                if cur_prod>=max_prod:
                    max_prod=cur_prod
                    #d.append(arr[i])
                    #d.append(arr[j])
                    #return d
                    return arr[i],arr[j]

n=int(input())
arr=list(map(int,input().split()))
print(max_prod_sum(n,arr))
