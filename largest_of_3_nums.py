def larget_of_three_nums(a,b,c):
    if a>b:
        max_1 = a
    else:
        max_1 = b
    if max_1>c:
        return max_1
    else:
        return c


num1=int(input('Enter the first number: '))
num2=int(input('Enter the second number: '))
num3=int(input('Enter the third number: '))
result=larget_of_three_nums(num1, num2, num3)
print(result,'is the largest number')