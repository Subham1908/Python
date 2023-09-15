# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:54:06 2023

@author: YG168VL
"""
#2

def is_prime(number): 

    if number == 1: 

        return False 

    for i in range(2, number): # Changed the range to start from 2 instead of 1

        if number % i == 0: # Changed '/' to '%' for checking divisibility

            return False 

    return True 

 

def find_prime_numbers(start, end): 

    prime_numbers = [] 

    for num in range(start, end + 1): 

        if is_prime(num): 

            prime_numbers.append(num) 

    return prime_numbers 

 

# Test the function 

start_range = 1 

end_range = 50 

expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47] 

result = find_prime_numbers(start_range, end_range) 

 

if result == expected_primes: 
    print("Congratulations! The function is correct.") 

else: 

    	print("Too bad! There's a bug in the function.") 