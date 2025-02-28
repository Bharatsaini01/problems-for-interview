
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