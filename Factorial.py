''' FACTORIAL NUMBER
n=int(input("enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)'''


''' RECURSION FACTORIAL
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))
'''
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
t=int(input("enter the number"))
print(fact(t))