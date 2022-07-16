##Python Basics Programming Assignment: 23

#Question 1
#Create a function that takes a number as an argument and returns True or False depending on whether the number
#is symmetrical or not. A number is symmetrical when it is the same as its reverse.

import logging

logging.basicConfig(filename="assignment23_log.log", level=logging.INFO, format= '%(levelname)s %(asctime)s %(name)s %(message)s')

def check_symmetric(n):
    """This program checks if the given number is symmetric or not"""

    try:
        logging.info("The entered number is: %s", n)
        temp = n
        fin = 0
        for i in range(len(str(n))):
            num1 = temp%10
            fin = fin*10+num1
            temp = temp//10
        if n == fin:
            logging.info("The given number, %s is symmetric number", n)
        else:
            logging.info("The given number, %s is not symmetric number", n)

    except Exception as e:
        logging.error("There is an error: %s", e)

check_symmetric(1223221)

#Question 2
#Given a string of numbers separated by a comma and space, return the product of the numbers.

def str_num_product(str1):
    """This function is to return product of the numbers separated by comma and space"""

    try:
        logging.info("The entered number string is: %s", str1)
        l = str1.split(', ')
        prod = 1
        for i in l:
            prod = int(i)*prod

        logging.info("The value of the entered string is: %s", prod)

    except Exception as e:
        logging.error("There is an error: ", e)

str_num_product("34, 5, 6, 2, 10")

#Question 3
#Create a function that squares every digit of a number.

def squ_digit(n):
    """This Function returns square of every digit in the given number and gives complete number"""

    try:
        logging.info("The given number is: %s", n)
        temp = n
        sq = 0
        pow = 0
        for i in range(len(str(n))):
            num = temp % 10
            pow = pow + len(str(num ** 2))
            sq = (sq + num ** 2) / (10 ** len(str(num ** 2)))
            temp = temp // 10
        op = sq * (10 ** pow)
        logging.info("The output value of the function is: %s", round(op))
    except Exception as e:
        logging.error("There is an error: %s", e)

squ_digit(3456)

#Question 4
#Create a function that sorts a list and removes all duplicate items from it.

def sort_list(l):
    """This fucntion sorts the given list and removes duplicates"""
    try:
        logging.info("The input list is: %s", l)
        l2 = sorted(list(set(l)), key=float)
        logging.info("The sorted list of given list is: %s", l2)

    except Exception as e:
        logging.error("There is an error: %s", e)

sort_list([23, 23, 45, 5,45,5, 3,3,3,2,27,7,89,87,345,90, 00.1])


#Question 5
#Create a function that returns the mean of all digits.

def mean_digits(n):
    """This function returns the mean of the given digits as integer"""
    try:
        logging.info("The given number is: %s", n)
        temp = n
        mean1 = 0
        for i in range(len(str(n))):
            num = temp%10
            mean1 = mean1 + num
            temp = temp//10
        logging.info("The mean of the given digit is: %s", int(mean1/len(str(n))))

    except Exception as e:
        logging.error("There is an error: %s", e)

mean_digits(15827)