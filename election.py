'''n=int(input('enter no. of voters:'))
arr=list(map(int,input().split()))
d={}
if n==1:
    print(arr[0])
else:
    mx,mc=-1,-1
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    ans=-1
    vals=sorted(reverse=True,key=lambda s:s[1])
    if len(vals)==1:
        ans=vals[0][0]
    else:
        if vals[0][1]==svals[1][1]:
            ans=-1
        else:
            ans=vals[0][0]
print(ans)                                
'''
n = int(input('Enter the number of voters: '))
arr = list(map(int, input().split()))
d = {}

if n == 1:
    print(arr[0])
else:
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    vals = sorted(d.items(), reverse=True, key=lambda s: s[1])

    if len(vals) == 1:
        ans = vals[0][0]
    else:
        if vals[0][1] == vals[1][1]:
            ans = -1
        else:
            ans = vals[0][0]
    print(ans)
