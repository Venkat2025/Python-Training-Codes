#finding higest element index of the array
ele=int(input("enter the number of elements"))
arr=list(map(int,input("enter number of elements one by one:").split()))
for i in len(arr):
    if ele>max(arr[i]):
        ele=arr[i]
        i=i+1
print(ele)
