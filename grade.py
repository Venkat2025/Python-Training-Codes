N=int(input("enter no of students"))
input2=input("grades:")
P=int(input("andrews grade:"))
grade=str(input2[N-1])
if (N-P)>1:
    start=N-P-1
else:
    start=0
if (N+P<=len(input2)):
    end=N+P
else:
    end=len(input2)
print(min(input2[start:end],key=lambda x:ord(x)),P)              