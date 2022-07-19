##Python_Basic_Programming_Assigment_09

#Write a Python program to check if the given number is a Disarium Number?
#Write a Python program to print all disarium numbers between 1 to 100?
#Write a Python program to check if the given number is Happy Number?
#Write a Python program to print all happy numbers between 1 and 100?
#Write a Python program to determine whether the given number is a Harshad Number?
#Write a Python program to print all pronic numbers between 1 and 100?

#Question 1: Check Disarium Number
import logging

logging.basicConfig(filename="assignment09_log.log", level=logging.INFO, format= '%(levelname)s %(asctime)s %(name)s %(message)s')

def Disarium_num(a):

    try:
        temp = a
        sum = 0
        i = 0
        while i<len(str(a)):
            if temp!=0:
                n = temp%10
                sum = sum + n**(len(str(a))-i)
                temp = temp//10
                i=i+1

        if sum == a:
            logging.info("Entered number {} is Disarium number".format(a))
        else:
            logging.info("Entered number {} is not Disarium number".format(a))

    except Exception as e:
        logging.error("Error observed: ", e)

Disarium_num(175)


#Question 2: Check Disarium number in a range

def Range_Dis_num(n1, n2):
    """This program gives the list of Disarium numbers in the given range"""

    try:
        l=[]
        for j in range(n1,n2+1):
            temp = j
            sum = 0
            i = 0
            while i<len(str(j)):
                if temp!=0:
                    n = temp%10
                    sum = sum + n**(len(str(j))-i)
                    temp = temp//10
                    i=i+1

            if sum == j:
                l.append(j)

        logging.info("List of Disarium numbers in the range {} to {} are: %s".format(n1, n2), l)

    except Exception as e:
        logging.error("There is an error: ", e)

Range_Dis_num(1,520)


#Question 3: Check Happy number

def sum_digit(n):
    """This function returns sum of squares of the digits in the given number"""
    try:
        temp = n
        sq = 0
        for i in range(len(str(n))):
            temp1 = temp%10
            sq = sq + temp1**2
            temp = temp//10
        return sq
    except Exception as e:
        logging.error("There is an error:", e)

def happy_num(n):
    """This function checks if the given number is Happy number or not"""
    try:
        logging.info("The input value is: %s", n)
        if n>0:
            ans = sum_digit(n)
            while len(str(ans))!=1:
                ans = sum_digit(ans)
                continue
            if ans == 1:
                logging.info("Given number is Happy number")
            else:
                logging.info("Given number is not a Happy number")
        else:
            logging.error("Check the input")
    except Exception as e:
        logging.error("There is an error", e)

happy_num(234)

#Question 4: Happy numbers in given range

def range_happy_num(a,b):
    """This function returns Happy numbers in the given range"""
    try:
        logging.info("The entered range is: %s, %s", a, b)
        if a>0 and b>0:
            l = []
            for j in range(a,b+1):
                ans = sum_digit(j)
                while len(str(ans)) != 1:
                    ans = sum_digit(ans)
                    continue
                if ans == 1:
                    l.append(j)
                else:
                    continue
            logging.info("The list of Happy numbers in the given range: %s", l)
        else:
            logging.error("Check the input")

    except Exception as e:
        logging.error("There is an error", e)

range_happy_num(1,200)

#Question 5: Program to check Harshad number

def harshad_num(n):
    """This Program checks if the given number is Harshad number or not"""
    try:
        logging.info("The input number is: %s", n)
        if n>0:
            temp = n
            sum = 0
            for i in range(len(str(n))):
                temp1 = temp%10
                sum = sum + temp1
                temp = temp//10
            if n%sum == 0:
                logging.info("The given number is Harshad number")
            else:
                logging.info("The given number is not Harshad number")
        else:
            logging.error("Check the input number")
    except Exception as e:
        logging.error("There is an error: %s", e)

harshad_num(153)

#Question 6: Pronic numbers from 1 to 100

def pranic_num(n):
    """This function checks if the given number is pranic number or not"""
    try:
        logging.info("The input number is: %s", n)
        if n>0:
            count = 0
            for i in range(n):
                if i*(i+1)==n:
                    count = count+1
                    break

            if count==1:
                logging.info("The given number is Pranic Number")
            else:
                logging.info("The given number is not Pranic Number")

    except Exception as e:
        logging.error("There is an error:", e)

pranic_num(132)