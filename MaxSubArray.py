'''def max(list1):
    sum=0
    for i in range(len(list1)):
        sum+=list1[i]
    return sum
list1=[-2,0,2,4] 
print(max(list1))'''   

def max_sum_subarray(array, number):
    narray = len(array)
    if number > narray:
        return "subarray of size greater than the array is not possible"
    
    current_sum = sum(array[:number])
    #max_sum = current_sum
    max_sum=float('-inf')
    for i in range(1, narray - number + 1):
        current_sum = current_sum - array[i - 1] + array[i + number - 1]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

array1 = [4, 3, 2, 7, 1, 9]
number = 4
print(max_sum_subarray(array1, number))

