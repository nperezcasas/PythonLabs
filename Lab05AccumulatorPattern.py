# Nuria Perez Casas
# Lab 5
# The Accumulator Pattern


#########################################################################
# Introduction
#########################################################################

# This lab introduces the accumulator pattern.
#
# Basic pattern:
# 1. Create an accumulator variable and set it to a default value
# 2. Increment the accumulator variable as necessary during a loop
# 3. Retrieve the value of the accumulator variable after the loop
#
# ===General Tips===
#
# =Style conventions=
# Follow the official guide located here:
#       http://www.python.org/dev/peps/pep-0008/
#
# =Tips=
# Function and variable names should be lowercase, with
# word breaks denoted by underscores. Be brief but
# make them meaningful. Examples:
#       number
#       score
#       score_list
#       human_guess
#       opponent_score
#       get_total_value()
#       calculate_average()
#
# A legal identifier for a variable or function name must
# follow a certain pattern.  The first character should be an uppercase
# or lowercase letter, or an underscore ('_'). Later characters can
# include uppercase or lowercase letters, underscores, and numbers.
#
# Give the accumulator variable a good name.  If it is the
# only accumulator in a simple function, you can use 'acc', but
# if you have more than one accumulator, use more specific names.
#
# Remember that the range() function creates a list of numbers.
# So when you see range(5), that is the same as saying [0,1,2,3,4].
#
# =Loops=
# We recently learned the structure of a for loop:
#       for _loopVariable_ in _list_:
# During the loop, the loop variable takes on the first value
# of the list, and the code within the loop runs. After the
# loop has finished one iteration, the loop variable takes on
# the next value in the list.  This continues until all items
# in the list have been used.
#
# If the loop is just counting over a range of numbers, the standard
# name you should give the loop variable is i.  If you need
# another loop variable, call it j, and so on.
#
# If the loop is over a specific list, you should use a fitting name.
# For example, if you are looping over a list called scores, you might
# use:
#       for score in scores:
#
# =Syntax note=
# In many of the loops below, you will see the operator +=.
# This operator is a shorthand operator common in many programming
# languages.  The assignment:
#       x += 1
# is exactly the same as saying:
#       x = x + 1
# but is simply shorter to type and easier to read. There are a
# handful of other shorthand assignment operators like this,
# including -=, *=, /=, **=, and //=.
#
# =How to use this file=
# Each example in this file is defined as a separate function.
# To use the file, open it in IDLE and select Run Module. In
# the shell prompt that appears, type the name of the function
# to run it. For example, to run the function simple_counter() I would
# write the following into my shell (the '>>>' is already there):
#       >>> simple_counter()
#       5
#
# To use a function like counter(number), you must supply a parameter.
# Here is an example usage:
#       >>> counter(9)
#       9
#
# You will often use a variable to call this type of function:
#       >>> number = 7
#       >>> counter(number)
#       7

#########################################################################
# Examples
#########################################################################

# This is our first example of an accumulator in action.
# First, we set acc = 0, because we want to start counting
# from 0 on up.  Then we loop over a list with 5 numbers, adding 1 to
# the accumulator each time. Finally, we print the result.
# Try it out by running this module and typing simple_counter()
# into the shell.
# We will call this type of accumulator a counting accumulator.
def simple_counter():
    acc = 0
    for i in [5, 9, 22, 18, 25, 8]:
        acc = acc + 1
    print(acc)


# There are two differences between simple_counter() and
# simple_summation(). The first difference is on the
# line declaring the for loop. Instead of using
# a specific list, this uses the range() function.  This is the
# equivalent of saying [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].  Remember that
# range() is only shorthand for a list.  The second
# difference is on the line where acc is incremented.
# Previously we incremented by 1 each time.  This time
# we add i. Since i is the loop variable, it takes on the
# value of each item in the list.  The result is that acc
# holds the sum of the numbers in the list.
# We will call this type of accumulator a summing accumulator.
def simple_summation():
    acc = 0
    for i in range(10):
        acc = acc + i
    print(acc)


# Now that you know how to use a counting accumulator and a summing
# accumulator, we combine them in this function to calculate the average
# of a list of numbers. Notice that both total and count are accumulator
# variables.  The variable total is a summing accumulator and count is
# a counting accumulator.  Again notice the third different way to
# use a for loop here.  This time the list is assigned to a variable
# and that variable representing the list is used in the 'for' line.
def simple_average():
    total = 0
    count = 0
    number_list = [5, 10, 19, 65, 74, 13, 9, 8, 10]
    for number in number_list:
        total += number
        count += 1
    average = total / count
    print("The average of", count, "items is", average)


# All three of the above functions demonstrate the accumulator pattern
# very well, but they are not very useful.  They only do one specific
# task and would need to be rewritten to work for other numbers. Now
# we will introduce the use of a parameter to give the function more
# value.  A parameter is a way to send extra information to a function
# before it runs, so its behavior can vary each time it is used.  For now,
# we will only use simple parameters. Just remember that you need to
# send a value when a function requires a parameter.  You have already
# done this every time you use the range() function or the print() function.
#
# Learning to use parameters can be confusing. Whatever name you give
# the parameter inside the parentheses is the name you can use to
# access the passed-in value inside your function. In this case,
# we called the parameter 'number' and used the 'number' variable
# to set the range of the for loop.
#
# In counter(), we count up to the given number. The result will be
# the same number that was sent in to it. It's still not very useful but
# demonstrates the counting accumulator pattern.  There are two examples
# above showing how to test out this function.
def counter(number):
    acc = 0
    for i in range(number):
        acc += 1
    print(acc)


# In summation(), we can pass in any list of numbers and the summing
# accumulator will find the total sum of the numbers in the list. This
# is now somewhat useful.
#
# This time the parameter is 'number_list' and we again used it
# to tell the for loop what to loop over.  Before you can call this
# function, you need to set up a list of numbers.
# Example:  >>> number_list = [5, 10, 25, 99, 84, 73]
#           >>> summation(number_list)
#           296
def summation(number_list):
    acc = 0
    for number in number_list:
        acc += number
    print(acc)


# With average(), we calculate the average of a given list of numbers.
# Notice this is very similar to simple_average(), with the only change
# being the parameterization of the number_list variable.
def average(number_list):
    """Calculates the average of a given list of numbers"""
    acc = 0
    count = 0
    for number in number_list:
        acc += number
        count += 1
    average = acc / count
    print("The average of", count, "items is", average)


#########################################################################
# Part 1
#########################################################################

# Your first task is to create a function called 'factorial()' **with
# one parameter**. Add it right into this file below this comment section.
# The function should print the factorial of the given number (and
# nothing else). Recall that the factorial of an integer n is the product
# of all positive integers less than or equal to n. The symbol for
# factorial is !, so:
#       4! = 4 x 3 x 2 x 1 = 24
#       4! = 1 x 2 x 3 x 4 = 24
#       5! = 5 x 4 x 3 x 2 x 1 = 120
# and so on.  You will need to use a new type of accumulator variable to
# accomplish this -- a multiplicative accumulator.  The function should
# just print the result of the factorial, so factorial(5) should print
# 120, factorial(4) should print 24, and so on.

def factorial(n):
    """

    Calculate the factorial of a number

    Parameters:
    n - The number to take the factorial of

    Prints the factorial of n, no return
    """
# In the same way we have seen how it is done in the top, we create an
# accumulator variable using a for loop. This time however, instead of
# adding we will mulitply, and instead of creating a list we will use
# the range so that it automatically calculates the factorial. 
    acc = 1
    for fact in range(1, n + 1):
        acc *= fact
    print(n, "! = ", acc)
        


#########################################################################
# Part 2
#########################################################################

# Next, we will create a function to help us find numbers in the
# fibonacci sequence.  This sequence is defined by the following
# recurrence relation:
#       F_0 = 0
#       F_1 = 1
#       F_n = F_(n-1) + F_(n-2)
# The function below is a representation of this recurrence
# relation in python code.  It will print the first
# 21 numbers in the fibonacci sequence.
def print_fibonacci():
    fib_0 = 0
    fib_1 = 1
    fib_n_minus_2 = fib_0
    fib_n_minus_1 = fib_1
    print(fib_0)
    print(fib_1)
    for i in range(21):
        fib_n = fib_n_minus_1 + fib_n_minus_2
        fib_n_minus_2 = fib_n_minus_1
        fib_n_minus_1 = fib_n
        print(fib_n)

    #NOTES: you may use an if statement. But you can use it. 
# Your task is to create a function called 'fibonacci()' **with one
# parameter**. Add it right into this file below this comment section.
# When called with number N, the function should print the value of
# the Nth item in the fibonacci sequence. For example, calling fibonacci(3)
# should print the number 2, fibonacci(10) should print 55, and
# fibonacci(14) should print 377. Don't print anything else or
# ask for other input.  Use the print_fibonacci() function for guidance.
# Hint: Start by copying over the print_fibonacci() function's contents,
# then modify it.  You will likely need to use at least one 'if' statement to
# accomplish this. Test that your function works for numbers 0-10, 14, and 25.

def fibonacci(n):
    # As we were asked, the function we create has a parameter
    # that asks what nth value of the fibonacci sequence you want.
    fib_n_minus_2 = 0
    fib_n_minus_1 = 1
    # We copy this section from the function we are given because we can't
    # ommit this part. We only change the fib_0 and fib_1 for 0 and 1 to
    # ommit the first two lines of the print_fibonacci() function. 

    # Now we create a if/elif statement for values 0 and 1 because they won't
    # work with the accumulator and the for loop formula we have in the top.
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Finally we create the accumulative loop function for the rest of the numbers.
    else:
        for i in range(2, n + 1):
            fib_n = fib_n_minus_1 + fib_n_minus_2
            fib_n_minus_2 = fib_n_minus_1
            fib_n_minus_1 = fib_n
    print(fib_n)


