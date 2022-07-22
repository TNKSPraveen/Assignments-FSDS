#Assignment: 10
#1. Write a Python program to find sum of elements in list?
#2. Write a Python program to Multiply all numbers in the list?
#3. Write a Python program to find smallest number in a list?
#4. Write a Python program to find largest number in a list?
#5. Write a Python program to find second largest number in a list?
#6. Write a Python program to find N largest elements from a list?
#7. Write a Python program to print even numbers in a list?
#8. Write a Python program to print odd numbers in a List?
#9. Write a Python program to Remove empty List from List?
#10. Write a Python program to Cloning or Copying a list?
#11. Write a Python program to Count occurrences of an element in a list?

l1 = [2, 4, 5, 6, 89, 54, 32, 1, 1, 2, 3, 87, 34, 4, 4]
l2 = [2,3,4, [1,3,6,7], [], [2,5,7,9]]
l3 = l1 + l2

#Question 1:#1. Write a Python program to find sum of elements in list?

def sum_list(l):
    sum = 0
    for i in l:
        if type(i)==int:
            sum = sum + i

        if type(i)==list:
            for j in i:
                if type(j)==int:
                    sum = sum+j
    return sum

print("The sume of digits in list is:", sum_list(l3))

#Question #2. Write a Python program to Multiply all numbers in the list?

def mul_list(l):
    mul = 1
    for i in l:
        if type(i)==int:
            mul = mul*i

        if type(i)==list:
            for j in i:
                if type(j)==int:
                    mul = mul*j

    return mul

print("THe product of all numebrs is: ",mul_list(l1))

#Question #3. Write a Python program to find smallest number in a list?

def small_list(l):
    l_out = sorted(l)
    return l_out[0]

print("The smallest numeber in given list is:", small_list(l1))

#Question #4. Write a Python program to find largest number in a list?

def nth_largest_list(l,n):
    l_out = sorted(l, reverse=True)
    return l_out[n-1]
print("The largest number in the given list is: ", nth_largest_list(l1,1))

#Question #5. Write a Python program to find second largest number in a list?

print("The 2nd largest number in the given list is: ",nth_largest_list(l1,2))

#Question #6. Write a Python program to find N largest elements from a list?

def list_n_largest(l,n):
    l_out1 = sorted(l, reverse=True)
    return l_out1[0:5]

print("The {} largest numbers are: {}".format(5, list_n_largest(l1,5)))

#Question #7. Write a Python program to print even numbers in a list?

def even_list(l):
    l_even=[]
    for i in l:
        if i%2==0:
            l_even.append(i)
    return l_even

print("The even numbers in the given list are: ", even_list(l1))

#Question #8. Write a Python program to print odd numbers in a List?

def odd_list(l):
    l_odd=[]
    for i in l:
        if i%2!=0:
            l_odd.append(i)
    return l_odd

print("The odd numbers in the given list are: ", odd_list(l1))

#Question #9. Write a Python program to Remove empty List from List?

def empty_list(l):
    l_out=l
    for i in l_out:
        if type(i) == list:
            if len(i) == 0:
                l_out.remove(i)
                return l_out

print("The list after removing empty list is: ", empty_list(l2))

#Question #10. Write a Python program to Cloning or Copying a list?

def clone_list(l):
    l_out = []
    for i in l:
        l_out.append(i)
    return l_out

print("The list after cloning the given list is: ", clone_list(l3))


#Question #11. Write a Python program to Count occurrences of an element in a list?

def count_repeat_list(l):
    for i in l:
        print("The occurance of {} : {} times".format(i,l.count(i)))

print(count_repeat_list(l1))