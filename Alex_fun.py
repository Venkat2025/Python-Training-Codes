def f(n):
    if n==0 or n==1:
        return 1
    return (f(n-1)*f(n-1)+(n-2)*(n-2))%47
n=int(input())
print(f(n))