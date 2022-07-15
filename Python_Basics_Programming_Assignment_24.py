###Python_Basic_Programming_Assigment_24

##Question1
##Create a function that takes an integer and returns a list from 1 to the given number, where:
##1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
##2. If the number cannot be divided evenly by 4, simply return the number.


import logging

logging.basicConfig(filename="assignment24_log.log", level=logging.INFO, format= '%(levelname)s %(asctime)s %(name)s %(message)s')


def int_to_list(n):
    """This function is used to take an integer and returns a list from 1 to the given number, where:
        1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
        2. If the number cannot be divided evenly by 4, simply return the number"""
    try:
        logging.info("We are into the try block, and input number is %s ", n)
        l=[]
        if (n>0):
            for i in range(1,n+1):
                if i%4!=0:
                    l.append(i)
                else:
                    l.append(i*10)
        else:  
            logging.info("The entered number is not valid")

        logging.info(str(("The output is: ", l)))

    except Exception as e:
        logging.exception("There is error encountered: ", e)
        logging.error(e)


int_to_list(-8)

##Question2
##Create a function that takes a list of numbers and return the number that's unique.


def return_unique_n(l):
    """This function can be used to return the unique number in list of given numbers"""
    try:
        logging.info("We are into the try block and the entered input is: %s ", l)
        l1 = set(l)

        for i in l1:
            if l.count(i)==1:
                logging.info("The unique number in the list is: %s ", i)

    except Exception as e:
        logging.exception("There is an error", e)
        logging.error(e)

a = [2,2,2,2,23,2,2,2,2,2]
return_unique_n(a)

#Question3
#Your task is to create a Circle constructor that creates a circle with a radius provided by an argument.
#The circles constructed must have two getters getArea() (PIr^2) and getPerimeter() (2PI*r)
#which give both respective areas and perimeter (circumference).


class circle_val():
    """This function gives area of circle and perimeter of circle, given radius"""
    try:
        def circle_area(r):
            logging.info("The given radius is: %s", r)
            logging.info("Finding the area of circle")
            area_of_circle = 3.14*r**2
            logging.info("The area of circle with given radius is: %s", area_of_circle)

        def circle_perimeter(r):
            logging.info("Finding perimeter of circle")
            perimeter_of_circle = 2*3.14*r
            logging.info("The perimeter of circle with given radius is: %s", perimeter_of_circle)

    except Exception as e:
        logging.exception("There is error to be checked: ", e)


circle_val.circle_perimeter(20)
circle_val.circle_area(20)

##Question 4:
##Create a function that takes a list of strings and return a list, sorted from shortest to longest.

def sort_list(l):
    logging.info("The input list for sorting is %s", l)
    try:
        l2 = sorted(l,key=len)
        logging.info("The sorted list is %s", l2)

    except Exception as e:
        logging.info("There is an error", e)

ad = ["are", "is", "a", "four", "eight", "wonderfully", "attribute"]
sort_list(ad)

##Question 5:
##Create a function that validates whether three given integers form a Pythagorean triplet. The
##sum of the squares of the two smallest integers must equal the square of the largest number to be validated.

def pyth_triplet(a,b,c):
    """This program checks whether 3 given integers form a Pythagorean Triplet"""
    logging.info("The given numbers are: %s, %s, %s", a,b,c)

    try:
        l = [a,b,c]
        [a1, b1, c1] = sorted(l,key=int)
        if (a1**2) + (b1**2) == (c1**2):
            logging.info("The given set of numbers form Pythagorean triplet")

        else:
            logging.info("The given set doesn't form Pythagorean triplet")

    except Exception as e:
        logging.error("There is an error: %s", e)


pyth_triplet(13,12,5)