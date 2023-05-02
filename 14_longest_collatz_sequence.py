# https://projecteuler.net/problem=14

# Longest Collatz sequence
# Problem 14

# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

import timeit

start_time = timeit.default_timer()

max_sequence_length = 0
max_number = 0
sequences = {}

for num in range(1, 10**7):
    temp = num
    sequence_length = 1
    # iterate until sequence reaches 1
    while temp != 1:
        # check if sequence length of temp is already in sequences dictionary
        if temp in sequences:
            sequence_length += sequences[temp] - 1
            break
        
        if temp % 2 == 0:
            temp = temp // 2 
        else:
            temp = 3 * temp + 1

        sequence_length += 1

    # add current number and sequence length to sequences dictionary
    sequences[num] = sequence_length
    
    # check if sequence length is greater than previous max
    if sequence_length > max_sequence_length:
        max_sequence_length = sequence_length
        max_number = num

print(f"Number produces longest chain {max_number}")
print(f"Length of sequence {max_sequence_length}")
execution_time = timeit.default_timer() - start_time
print(f"Execution time {execution_time} seconds")
