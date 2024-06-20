'''
def number(X,Y):
    T=X-Y
    while True:
        if Y==0:
            return X
        else:
            if T==X-Y:
                X=Y
                Y=T
                return Y
print(number(48,18))
'''

X=int(input())
Y=int(input())
while (Y>0):
    if Y>X:
        X,Y=Y,X
    else:
        X,Y=Y,X-Y
print(X)        