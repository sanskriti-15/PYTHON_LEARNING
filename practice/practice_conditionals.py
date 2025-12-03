# Classify a person's age group: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+)

age = int(input("ENTER THE AGE: "))

if age < 13:
    print("The person is a Child")

elif age >= 13 and age <= 19:
    print("The person is a Teenager")

elif age >= 20 and age <= 59:
    print("The person is an Adult")

else:
    print("The person is a Senior")


# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("ENTER THE AGE: "))
day = input("WHAT DAY IS TODAY : ")

if age >= 18 and day == "wednesday":
    print("Price is $10")
elif age>=18 and day != "wednesday":
     print("Price is $12")
elif age < 18 and day != "wednesday":
     print("Price is $8")
else :
     print("Price is $6")

# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

marks = int(input("ENTER THE MARKS : "))
if(marks >100) :
      print("INVALID !!!")
      exit()
elif marks >= 90 and marks <= 100:
        print("Your Grade is A")
elif marks >= 80 and marks <= 89:
        print("Your Grade is B")
elif marks >= 70 and marks <= 79:
        print("Your Grade is C")
elif marks >= 60 and marks <= 69:
        print("Your Grade is D")
else:
        print("Your Grade is F, Dissatisfied")


# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = input("ENTER THE fruit : ")
color = input("ENTER THE color : ")

if fruit == "banana":
    if color == "green":
        print(f"{fruit} is unripe")
    elif color == "yellow":
        print(f"{fruit} is ripe")
    elif color == "brown":
        print(f"{fruit} is over ripe")
    else:
        print("Unknown banana color")
else:
    print("Not a banana")

year = int(input("ENTER THE YEAR : "))

if (year%4 ==0 and year%100 !=0) or (year%400 ==0) :
     print("the year is the leap year")
else:
     print("the year is not a leap year")
