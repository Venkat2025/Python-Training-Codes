n=int(input('enter the size of array:'))
arr=list(map(int,input("enter array elements:").split()))
arr.sort()
res=[]
start=0
end=-1
while len(arr)>=1:
    res.append(abs(arr[end]-arr[start]))
    arr.pop(end)
    arr.pop(start)
print(sum(res))   