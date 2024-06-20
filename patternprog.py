

''' printing triangle 
rows=5
max_width=len(' *'*rows)
for i in range(1,rows+1):
    stars=' '.join('*'*i)
    leading_spaces=(max_width-len(stars))//2
    print(' '*leading_spaces+stars)

    OR
for i in range(5):
    x=' *'
    x=x*i
    print(f'{x:^10}')
    '''

'''
for i in range(6):
    x=' *'
    x=x*i
    print(f'{x:<10}')
'''
t1=(1,2,3,2,4,1)
t2=set(t1) 
print(t2) 
t2=sorted(t1)
print(t2) 
