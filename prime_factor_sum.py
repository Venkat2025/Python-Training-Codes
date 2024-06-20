def prime_factors(num):
    i=2
    factors={}
    while i*i<=num:
        while (num%i)==0:
            if i in factors:
                factors[i]+=1
            else:
                factors[i]=1
            num//=i    
        i=i+1
    if num>1:
        factors[num]=1
    return factors
def main():
    n=int(input().strip())
    if n==0:
        return -1
    arr=list(map(int,input().split()))
    num=int(input().strip())
    factors= prime_factors(num)
    result=0    

    for factor,power in factors.items:
        index=factor
        if index<n:
            result=result+power*arr[index]
print(result)
main()
print(prime_factors(12))            