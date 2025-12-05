# Problem: Write a function to calculate and return the square of a number.

def calculate_square(n):
    return n*n
square_n = calculate_square(8)
print(f"square of 8 is : {square_n}")


# Problem: Create a function that takes two numbers as parameters and returns their sum.
def s(num1,num2):
    return num1+num2

sum_of_num = s(8,10)
print(f"sum of numbers are : {sum_of_num}")

# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.
def mul(num1,num2):
    return num1*num2

multiple = mul(8,10)
print(f"multiple of numbers are : {multiple}")

multiple_string = mul("sanki  ",4)
print(f"multiple of numbers are : {multiple_string}")

# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math
def area(radius):
   a = math.pi*radius**2
   c = 2*math.pi*radius
   return a,c

a,c = area(5)
print(f"Area is {a} and circumference is {c}")

# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.
def greet(name = "SANKI "):
    return  name + "Welcome!"
msg = greet()
print(msg)
msg = greet("ABC ")
print(msg)

# Problem: Create a lambda function to compute the cube of a number.
cube = lambda x:x**3
print(cube(3))

# Problem: Write a function that takes variable number of arguments and returns their sum.
def func(*args):
    return sum(args)

print(func(1, 2))
print(func(1, 2, 3))
print(func(1, 2, 3, 4))
print(func(1, 2, 3, 4, 5))

def f(*args):
    for i in args:
        print(i*2)

print(f(1, 2, 3, 4, 5))


# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def normal_func(name, age):
    print("username:", name, "age:", age)


normal_func(name = "John", age = 30)
normal_func(age = 27, name = "Nick")
# normal_func(name = "Munna", age = 33, email = "munna33@gmoi.net")   # Output: TypeError: normal_func() got an unexpected keyword argument 'email'


# Handle with **kwargs
def kwargs_func(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
    print("\n")


kwargs_func(name = "John", age = 30)
kwargs_func(age = 27, name = "Nick")    # Output: age : 27 name : Nick
kwargs_func(name = "Munna", age = 33, email = "munna33@gmoi.net")

# Problem: Write a generator function that yields even numbers up to a specified limit.

def get_even(n):
    for i in range(2,n+1):
        if i%2==0:
            print(i)
get_even(15)


def get_even_another_way(n):
    for i in range(2,n+1,2):
        print(i)
get_even_another_way(115)


def even_generator(limit):
    for i in range(2, limit + 1, 2):
        return i
print(even_generator(10))    # Output: 2

# NOTE - With yield


# Inside python after memory definition, internally python manages 1st element memory reference address and maintain the yelded.

#  Internally python uses this memory reference address to determine the next element to be yelded and so on.

# Also internally if two different Iteration Tools are pointing to the same memory reference address then the yeald will not mismatch the value of the same memory reference address, like give 1st iterator tool 2 and 2nd iterator tool 3, then 1st iterator tool will give 2 and 2nd iterator tool will give 3 and so on. 

# Along with that yeald can also differentiate between the multiple Iteration Tools with same memory reference address.


def generator_function_with_yield(values):
    for i in range(1, values + 1,2):
        yield i

for num in generator_function_with_yield(10):
    print(num)
# Problem: Create a recursive function to calculate the factorial of a number.

n = 5

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
    

print(factorial(n))