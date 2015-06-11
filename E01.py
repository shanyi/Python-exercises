# '''
# Programming background in Python.
#
# The first exercise allows you to assess your ability to program in Python.
# As a data analyst, you will spend much of your time writing code and
# programs to work with data or to build mathematical, statistical, or
# machine learning models to find insights from data.
#
# Complete this function that modifies a list of integers.
#
# 1)  For numbers that are multiples of three replace the integer with the string "Fizz".
#
# 2)  For numbers that are multiples of five replace the integer with the string "Buzz".
#
# 3)  For numbers that are multiples of both three AND five replace the integer
#     with the string "FizzBuzz"
#
# Your function should take in a list of integers as input.
# Your function should not modify the input list.
# Your function should return an updated list with integers and strings.
# '''
#
#
# '''
# Your fizzbuzz function. The grader will run `fizzbuzz(intList)` to check if your
# function returns the correct output.
# intList: list containing integers
# Make sure you write the script so that your algorithm is part of the
# function; you do not need to call the function yourself.
#
# '''

def fizzbuzz(intList):
    for a in intList:
        result=[]
        if a % 3==0 and a % 5==0:
            result.append('FizzBuzz')
        elif a % 3==0:
            result.append('Fizz')
        elif a % 5==0:        
            result.append('Buzz')
        else:
            result.append(a)
    return intList

#OR

def fizzbuzz(intList):
    for i in range(len(intList)):
        if intList[i] % 3==0 and intList[i] % 5==0:
            intList[i]='FizzBuzz'
        elif intList[i] % 3==0:
            intList[i]='Fizz'
        elif intList[i] % 5==0:
            intList[i]='Buzz'
    return intList