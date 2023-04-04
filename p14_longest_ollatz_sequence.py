# https://projecteuler.net/problem=14
# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

import time

start_time = time.time()

max_sequence_length = 0
max_number = 0

for num in range(1, 1000000):
    temp = num
    sequence_length = 1
    while temp != 1:
        if temp % 2 == 0:
            temp = temp // 2 
        else:
            temp = 3 * temp + 1
        sequence_length += 1
    if sequence_length > max_sequence_length:
        max_sequence_length = sequence_length
        max_number = num

print(f"Number produces longest chain {max_number}")
print(f"Length of sequence {max_sequence_length}")
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time {execution_time} seconds")
