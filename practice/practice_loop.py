# Problem: Given a list of numbers, count how many are positive.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
for i in numbers:
    if i >= 0:
        print(f"positive number in numbers is : {i}")

# Problem: Calculate the sum of even numbers up to a given number n.
number = 18
sum = 0
for n in range(1, number + 1):
    if n % 2 == 0:
        sum += n
print(f"SUM OF EVEN NUMBERS TILL {number} is {sum}")

# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
number = 15
for i in range(1, 11):  # from 1 to 10
    if i == 5:          # skip 5th iteration
        continue
    print(f"{number} x {i} = {number * i}")

# Problem: Reverse a string using a loop.
string = "sanskriti"
rev_string = ""
for s in string:
    rev_string = s+rev_string
print(f"reversed string is {rev_string}")

# Problem: Given a string, find the first non-repeated character.
input_string = "teeter"
for ch in input_string:
    if input_string.count(ch) == 1:
        print(f"The first non-repeated character is {ch}")
        break

# Problem: Compute the factorial of a number using a while loop.
num = 5
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print(f"factorial of {num} is {fact}")

# Problem: Keep asking the user for input until they enter a number between 1 and 10.
while True:
    num = int(input("Enter a number between 1 and 10: "))
    if 1 <= num <= 10:
        print("Thank you! ✅")
        break
    else:
        print("Not in range, try again.")

# Problem: Check if a number is prime.
number = 13
is_prime = True

for i in range(2,number-1):
    if number % i == 0:
        is_prime = False
        break

if is_prime:
        print(f"{number} is a prime number")
else:
        print(f"{number} is not a prime number")

# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
items = ["apple", "banana", "orange", "apple", "mango"]
seen = set()

for item in items:
    if item in seen:
        print(f"The first duplicate is {item}")
        break
    seen.add(item)

# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.
import time
wait_time = 1
max_retry = 5
attempt = 0

while attempt < max_retry:
    print("Attempt",attempt +1,"-wait time",wait_time)
    time.sleep(wait_time)
    wait_time *=2
    attempt+=1

