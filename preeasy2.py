array=input("enter the elements in the array:").split(',')
array=[int(num) for num in array]
sum_odd=0
sum_even=0
for i in range(len(array)):
    if array[i] % 2==0:
        sum_even+=array[i]*array[i]
    else:
        sum_odd+=array[i]*array[i]
print("sum of square of even numbers in a array:",sum_even)
print("sum of square of odd numbers in a array:",sum_odd)
        