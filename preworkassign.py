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
def max_num_in_list(a_list):
    a_list = [1,2,3,4,5,6,7,8,9,10]
    max_num= max(a_list)
    return(max_num)
    
print(max_num_in_list)


