#!/usr/bin/env python3

def happy_new_year():

    i = 10

    while i >=  0:        
        
        if(i == 0):
            print("Happy New Year!")
            i= i - 1
        else:
            print(i)
            i = i - 1
    pass

def square_integers(int_list):
    int_list = [int * int for int in int_list]
    return int_list

def fizzbuzz():

    x = 1

    for x in range(1, 101):

        if(x % 3 == 0 and x % 5 == 0):
            print("FizzBuzz")
        elif(x % 3 ==  0):
            print("Fizz")
        elif(x % 5 == 0):
            print("Buzz")
        else:
            print(f"{x}")
    pass

happy_new_year()