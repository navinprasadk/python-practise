# https://projecteuler.net/problem=145

# How many reversible numbers are there below one-billion?
# Problem 145

# Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

# There are 120 reversible numbers below one-thousand.

# How many reversible numbers are there below one-billion (109)?

import time

start_time = time.time()

# counter to count the reversible numbers
count = 0

for num in range(1, 1000000000):
    # skip numbers that end with 0
    if num % 10 == 0:
        continue  
    
    reverse_num = int(str(num)[::-1])
    sum = num + reverse_num
    
    is_sum_odd = True
    
    # check if all digits in the sum are odd
    for digit in str(sum):
        if int(digit) % 2 == 0:
            is_sum_odd = False
            break

    # if the sum consists entirely of odd digits, increment the counter            
    if is_sum_odd:
        count +=1

print(f"number of reversible numbers under 1 billion is  {count}")
end_time = time.time()
execution_time = end_time - start_time
print(f"execution time is {execution_time}")
