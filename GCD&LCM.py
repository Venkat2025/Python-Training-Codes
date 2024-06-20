a,b=list(map(int,input().split()))
def gcd(a,b):
    while(b):
        a,b=b,a%b
    return a
def lcm(a,b):
    return a*b//gcd(a,b)
gcd,lcm=gcd(a,b),lcm(a,b) 
print(gcd,lcm)           