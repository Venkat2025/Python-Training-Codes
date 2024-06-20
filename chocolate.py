chocolate=list(map(int,input("enter number of chocolate in each jar:").split()))
N=len(chocolate)
count=0
for i in chocolate:
    if i==0:
        continue
    if i==1:
        count+=1
    else:
        if i%3==0:
            count+=(i//3)
        else:
            count+=(i//3)+1
print(count)                

