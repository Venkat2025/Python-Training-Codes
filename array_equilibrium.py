n=int(input("enter the size of array:"))
A=list(map(int,input('enter the elements of array').split()))
flag=True
for i in range(len(A)):
    if sum(A[:i+1])==sum(A[i+1:]):
        flag=False
        print(i+1)
        break
        
if flag:
    print("not found")    