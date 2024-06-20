array=list(map(int,input().split()))
n=len(array)
count=0
for i in range(n):
    if sum(array[:i+1])==0:
        count+=1
print(count)       