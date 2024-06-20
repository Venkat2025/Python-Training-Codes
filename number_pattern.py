row=int(input())
for i in range(row,0,-1):
    a=[]
    for j in range(row,0,-1):
        a=[j]*i
        print(*a,sep=' ',end=' ')
    print()