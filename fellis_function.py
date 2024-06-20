def f(n):
    if n==0 or n==1:
        return 1
    return (f(n-1)+7*f(n-2)+(n//4)%(10^9+7))
n=int(input())
print(f(n))