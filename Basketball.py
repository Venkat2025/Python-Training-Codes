def maximum_score(A,K):
    N=len(A)
    max_score=float('-inf')

    for i in range(N-K+1):
        current_score=0
        for j in range(K):
            current_score+=(i+j)*A[i+j]
            max_score=max(current_score,max_score)
    return max_score

A= [4,3,2,7,1,9]
K=3
print(maximum_score(A,K))           