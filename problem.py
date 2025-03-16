
# You are given a Bank account having N amount and you are asked to perform 
# ADD(credit) or SUBTRACT(debit) operation of an amount X.
# After the operation print the amount left in the Bank account. 
# If the debit amount is greater than current balance print 
# "Insufficient Funds"(without quotes) and the operation is skipped.

def bank_account(balance):
    a = "Enter amount :"
    b = "your balance :"
    print("enter 1 for credit \
           enter 2 for debit \
           enter any other key to exit")
    choice = int(input("Enter your choice :"))

    if choice ==1:
        amount = int(input("Enter amount for Credit:"))
        if amount >= 1:
            balance += amount
            print(b,balance)
            bank_account(balance);
        else:
            print("Invalid amount!")

    elif choice == 2:
        amount = int(input("Enter amount for Debit:"))
        if amount >= 1:
            if balance >= amount:
                balance -= amount
                print(b,balance)
                bank_account(balance);
            else:
                print("Insufficient Funds!")
                bank_account(balance);
# bank_account(0);

# Write a program to input an integer from user and 
# print 1 if it is odd otherwise print 0.

def check_odd():
    num = int(input("enter a number :"))
    if num%2==0 :
        print(0)
    else:
        print(1)

# check_odd()

# Write a program to input two numbers(A & B) from user and 
# print the minimum element among A & B in each line.

def min_value():
    a = int(input("Enter first number  : "))
    b = int(input("Enter second number : "))
    min = 0
    if a < b :
        min = a
    else:
        min = b
    
    print("{} is minimum".format(min))

# min_value();

# Write a program to input three numbers(A, B & C) 
# from user and print the minimum element among A, B & C.

def minimum_value():
    a = int(input("Enter first number  : "))
    b = int(input("Enter second number : "))
    c = int(input("Enter third number  : "))
    min = 0
    if a < b :
        min = a
    else:
        min = b
    if min < c:
        min = min
    else:
        min = c
    
    print("{} is minimum".format(min))

# minimum_value();

# Take an integer A as input, you have to tell whether it is a prime number or not.
# A prime number is a natural number greater than 1which is divisible only 
# by 1 and itself.

def check_prime_number():
    num = int(input("enter a number :"))
    check = 0
    if num == 1 or num == 2:
        check = 1
    else:
        for i in range(2,num):
            if num%i==0:
                check = 0
                break
            else:
                check = 1
    if check == 0:
        print("{} is not prime number.".format(num))
    else:
        print("{} is prime number.".format(num))


# check_prime_number();

# Given an integer N, print the corresponding pattern for N.
# For example if N = 4 then pattern will be like:
# A
# B B
# C C C
# D D D D

def make_pattern():
    N = int(input("enter a number :"))
    alfabat = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(N):
        print("")
        for j in range(i+1):
            print(alfabat[i], end=" ")

# make_pattern();

# Take an integer N as input, print the corresponding pattern for N. 
# For example if N = 4 then pattern will be like:


# 1
# 1 2
# 1 2 3
# 1 2 3 4


def make_pattern_num():
    N = int(input("enter a number :"))
    for i in range(1,N+1):
        print("")
        for j in range(i):
            print(i, end=" ")

# make_pattern_num();

# Take an integer N as input, print the corresponding stair pattern for N.
# For example if N = 4 then stair pattern will be like:
# *
# **
# ***
# ****


def make_pattern_star():
    N = int(input("enter a number :"))
    for i in range(N):
        print("")
        for j in range(i+1):
            print("*", end="")

# make_pattern_star();

# You take a number of test cases, denoted by T as input.For each test case, 
# you should take integers Nas input. 
# Your task is to calculate and print the sum of the digits of the given number N.


def sum_of_digits():
    T = int(input("enter no of values :"))
    data = []
    for i in range(T):
        N = input("enter number :")
        sum = 0
        for j in N:
            sum += int(j)
        data.append(sum)
    for i in data:
        print(i)

# sum_of_digits();

# You are given an integer A, you need to find and return the 
# sum of all the even numbers between 1and A.
# Even numbers are those numbers that are divisible by 2.


def sum_of_even():
    N = int(input("enter a number"))
    sum = 0
    for i in range(1,N+1):
        if i%2==0:
            sum+=i
    
    print("sum is :",sum)

# sum_of_even();
"""
1111
123%10 = 3
0*10

"""
def reverse_num():
    num = int(input("enter a number"))
    reverse_num = 0
    while num > 0 :
        digit = num%10
        num = num//10
        reverse_num =  reverse_num*10 + digit
    print(reverse_num)

# reverse_num()

def palindrom_check():
    word = input("enter a word: ")
    reverse_word = word[::-1]
    print("palindrom") if word == reverse_word else print("not palindrom")

# palindrom_check()

#  Write a program to print the multiplication table of the number entered by the user, N.

# The table for input N = 5 should get displayed in the following form:


def multiplication_table():
    num = int(input("enter a num"))
    for i in range(1,11):
        value = num*i
        print(value)

# multiplication_table()

# ake an integer N as input, print the corresponding Numeric Inverted Half Pyramid pattern for N.

# For example if N = 4 then pattern will be like:

# 1 2 3 4
# 1 2 3
# 1 2
# 1

def show_descending_number_triangle():
    N = int(input("Enter a number: "))
    for i in range(N,0,-1):
        for j in range(1,i+1):
            print(j ,end=" ")
        print("")

# show_descending_number_triangle()

# Problem Description

# Given an integer N as input, print the corresponding Full Numeric Pyramid pattern for N.

# For example if N = 5 then pattern will be like:

# 0 0 0 0 1 0 0 0 0 
# 0 0 0 2 3 2 0 0 0 
# 0 0 3 4 5 4 3 0 0
# 0 4 5 6 7 6 5 4 0
# 5 6 7 8 9 8 7 6 5 

def full_numeric_pyramid():
    N = int(input("Enter a Number: "))
    num = 0
    for i in range(N,0,-1):
        for j in range(1,N*2):
            if j == i :
                num += 1
                print(num,end=" ")
            elif j <= N and j > i:
                num += 1
                print(num,end=" ")
            elif j > N and j <= N*2-i:
                num -= 1
                print(num,end=" ")
            else:
                print(0,end=" ")
        print("")

            

        
        

        

# full_numeric_pyramid()


# You are given an integer A, you need to find and return the sum of all the even numbers between 1 and A.

# Even numbers are those numbers that are divisible by 2.


def sum_of_even_numbers(A):
    sum = 0
    for i in range(1,A):
        if i%2 ==0:
            sum += i
    return sum

# A = 5
# sum = sum_of_even_numbers(A)
# print(sum)


# Count Even and Odd Digits in a Number
# Problem: Given a number N, count how many digits are even and how many are odd.
# Example:

# Input:  482351  
# Output: Even: 3, Odd: 3  

def count_even_odd_numbers(N):
    even = 0
    odd = 0
    for i in range(1,N+1):
        if i%2 == 0:
            even +=1
        else:
            odd += 1
    print("Even : {} Odd : {}".format(even,odd))

# N = 5
# count_even_odd_numbers(N)

# convert a number to binary without using built-in functions
# input = 10
# output = 1010

def convert_number_to_binary(N):
    binary_number = ""
    while N > 0:
        binary_number = str(N % 2) + binary_number
        N = N//2
    return binary_number if binary_number else 0

# N = 7
# binary_value = convert_number_to_binary(N)
# print(binary_value)

# find the largest and smallest digit in a number
# input 38576
# output  largest =8, smallest=3

def find_largest_and_smallest_digit(N):
    max_digit = N%10
    min_digit = max_digit
    while N > 0:
        N = N//10 
        next_digit = N%10
        print(next_digit)
        if max_digit < next_digit:
            max_digit = next_digit
        elif min_digit > next_digit and N != 0:
            min_digit = next_digit
    print("Largest: {} and Smallest: {}".format(max_digit,min_digit))

# N = 385762
# find_largest_and_smallest_digit(N)

# Remove a Specific Digit from a Number
# Problem: Given a number N and a digit D, remove all occurrences of D from N.
# Example:

# Input:  N = 10501, D = 0  
# Output: 151  

def remove_digit_in_number(N,D):
    result = 0
    while N > 0:
        digit = N%10
        N = N//10
        if digit == D:
            continue
        else:
            result = digit*10 + result
        
    return result

# N,D = 10501,2
# result = remove_digit_in_number(N,D) 
# print(result)


# convert a number to decimal to binary without using built-in functions 
# input= 1010
# output = 10


def convert_binary_to_decimal(N):
    decimal_number = 0
    i=0
    while N > 0:
        digit = N%10
        N = N//10
        decimal_number =+ digit * 2**i + decimal_number
        i += 1
    print(decimal_number)

# N = 111
# convert_binary_to_decimal(N)


# Problem:
# Use division by 2 to check if a number is even or odd.

# Example:
# Input: n = 27
# Output: Odd


def check_even_and_odd(N):
    if N%2 == 0:
        print("Even")
    else:
        print("Odd")

# N=27
# check_even_and_odd(N)


# Write a function to count the number of 1s in a binary representation of a number using division by 2.

# Example:
# Input: n = 13 (Binary: 1101)
# Output: 3

def count_no_of_once_in_binary(N):
    count = 0
    while N > 0:
        digit = N %2
        N = N//2
        if digit ==1:
            count +=1
    print(count)
        
# N=13
# count_no_of_once_in_binary(N)



# The parity of a number is even if it has an even number of 1s in its binary representation and odd otherwise.

# Write a function to find the parity of a number using division by 2.

# Example:
# Input: n = 9 (Binary: 1001, has 2 ones)
# Output: Even Parity


def check_even_odd_parity(N):
    parity = 0
    while N > 0 :
        digit = N%2
        N = N//2
        if digit == 1:
            parity += 1

    print("Even parity") if parity%2 == 0 else print("Odd parity")

# N= 9
# check_even_odd_parity(N)

# Problem:
# Write a function to reverse the binary representation of a number using division by 2.

# Example:
# Input: n = 6 (Binary: 110)
# Output: 011 (Binary of 3)

def reverse_binary(N):
    reverse_binary = ""
    while N>0:
        reverse_binary = reverse_binary + str(N%2)
        N = N//2
    
    print(reverse_binary) if reverse_binary else 0

N=6
# reverse_binary(N)