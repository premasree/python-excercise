def is_it_a_prime_number(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


try:
    start = int(input('Enter the starting number: '))
    end = int(input('Enter the ending number: '))
except:
    print("please enter whole number")
    exit()

if start <= 1:
    print('Start Value should be greater than 1')
    print('Since 1 is neither Prime nor Composite')
    exit()
if start > end:
    print('Start Value cannot be greater than the End Value')
    exit()
for i in range(start, end + 1):
    result = is_it_a_prime_number(i)
    if result is False:
        print(i, 'is a not Prime Number')
    else:
        print(i, 'is a Prime Number')
