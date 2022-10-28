#Question One
#Write a function to print "hello_USERNAME!" 
#USERNAME is the input of the function.

def hello_name(username):
    """Display a simple greeting."""
    print("hello_" + username + "!")
hello_name("USERNAME")

#Question Two
#Write a python function, first_odds that prints 
#the odd numbers from 1-100 and returns nothing
def first_odds():
    odd_numbers = list(range(1,100,2))
    print(odd_numbers)
first_odds()

#Question 3
#Please write a Python function, 
#max_num_in_list to return the max number
#of a given list. 
a_list = [1,2,3,4,5,6,7,8,9,10]
def max_num_in_list(a_list):
    
    max_num= max(a_list)
    return(max_num)
    
print(max_num_in_list(a_list))


#Question 4
#Write a function to return if the given year 
#is a leap year. A leap year is divisible by 4,
#but not divisible by 100, unless it is also divisible by 400. 
#The return should be boolean.

def is_leap_year(a_year):
    if a_year % 4 ==0:
        if a_year % 100 != 0:
        
            if a_year % 400 == 0:
                print("This is a leap year.")
            else: 
                print ("This is not a leap year.")
        else:
            print("This is a leap year.")
    else:
        print("This is not a leap year.")
is_leap_year(2024)

#Question 5
#Write a function to check to see if all 
#numbers in list are consecutive numbers. 
#For example, [2,3,4,5,6,7] are consecutive numbers, 
#but [1,2,4,5] are not consecutive numbers. 
#The return should be boolean Type.

a_list=[1,2,3,5]
def is_consecutive(a_list):
    my_pointer=a_list[0]
    for num in a_list:
        print(num)
        if num != my_pointer:
            return "This is not a consecutive number."
        my_pointer += 1
    return "This is a consecutive number."
print(is_consecutive(a_list))

