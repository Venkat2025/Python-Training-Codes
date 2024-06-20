array=list(map(int,input().split()))
n=len(array)
array.sort()
max1,max2=array[-1],array[-2]
avg=(max1+max2)/2
sum=0
for i in range(len(array)):
    if array[i]>=avg:
        sum=sum+array[i]
    else:
        pass
print(sum)