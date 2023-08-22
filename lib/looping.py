#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count >= 1:
        print(count)
        count = count - 1

    print("Happy New Year!")

def square_integers(int_list):
    squared_integers =[item**2 for item in int_list]
    return squared_integers
    


def fizzbuzz():
    for i in range(1, 101):
        if (i %3 == 0) and (i %5 == 0):
            print("FizzBuzz")
        elif i %3 == 0:
            print("Fizz")
        elif i%5 ==0:
            print("Buzz")
        else:
            print(i)
 