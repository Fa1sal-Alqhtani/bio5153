#! /usr/bin/env python3

# import modules
import argparse


# function to accept command-line arguments
def get_args():
        
    #create an ArgumentParser object
    parser = argparse.ArgumentParser(description="This script returns the Fibonacci number at a specified locationin the sequence")

    # add positional (required) arguments
    parser.add_argument("num", help="The Fibonacci number you wish to calculate", type=int)

    # add optional arguments
    # the default for 'store_true' is . . . "False"
    parser.add_argument("-v", "--verbose", help="Print verbose output", action= 'store_true')

    # parse the actual arguments
    # access argument values via 'args' variable
    args = parser.parse_args()
    
    return args

# function to calculate the Fibonacci number/sequence
def fib(n):
    a,b = 0,1

    for i in range(n):
        a,b = b,a+b

    return a

# define the 'main' function
def main():

    fib_number = fib(x.num)

    # print the answer
    if x.verbose:
        print('The Fibonacci number for', x.num, 'is:', fib_number)
    else:
        print(fib_number)

# get the command-line arguments

x = get_args()
# print the answer
#print('The Fibonacci number for', args.num, 'is:' fib_number)



# set the environment for this script
# is this main, or is this a module called by another script?
if __name__== '__main__':
    main()