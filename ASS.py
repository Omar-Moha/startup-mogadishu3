# Assignment One For Python
# Question 1
X = int(input("Enter integer Number: "))
if X > 100:
    z = 40
else:
    y = 20
print(X)


# Question 2
a = int(input("Enter Number: "))
if a == 100:
    b = 10
    c = 50
    print(b)
    print(c)

# Question 3
a = int(input("Enter a Number: "))
if a < 10:
    b = 0
else:
    b = 99
print(b)

# Question 4
Score = int(input("Enter Your Grade: "))
if Score >= 90:
    print("Your Score is grade A.")
elif Score >= 80:
    print("Your grade is grade B.")
elif Score >= 70:
    print("Your Score is grade C.")
elif Score >= 60:
    print("Your score is grade D.")
else:
    print("Your score is grade F")

# Question 5
Number = int(input("Enter a Number: "))

if(Number % 2) == 0:
    print(f'{Number} is a even number')

else:
    print(f'{Number} is a odd number')


# Question 6
length_1 = float(input("Enter length for triangle #1: "))
width_1 = float(input("Enter width for triangle #1: "))

area_1 = length_1 * width_1


length_2 = float(input("Enter length for triangle #2: "))
width_2 = float(input("Enter width for triangle #2: "))

area_2 = length_2 * width_2

if area_1 > area_2:
    print("Rectangle #1 has the greatest area at", area_1, "inches.")
elif area_2 > area_1:
    print("Rectangle #2 has the greatest area at", area_2, "inches.")
elif area_1 == area_2:
    print("Rectangle #1 and #2 have the Same area at", area_1, "inches.")


# Question 7
User_month = int(input("Enter a month between 1 and 12: "))

message = ""

if User_month < 1 or User_month > 12:
    message = "Error. Month Must be between 1 and 12."
else:
    message = "Month " + format(User_month) + " Is in the"

    if User_month >= 1 and User_month <= 3:
        message += " First"
    elif User_month >= 4 and User_month <= 6:
        message += " Second"
    elif User_month >= 7 and User_month <= 9:
        message += " Third"
    elif User_month >= 10 and User_month <=12:
        message += " Fourth"

    message += " Quarter.\n"

print(message)


# Question 8
user_number = int(input("Enter a number between 1 and 10: "))

Message = ""

if user_number < 1 or user_number > 10:
    Message = " Error. Number must be between 1 and 10."
else:
    Message = "\nThe roman numeral for "


    if user_number == 1:
        Message += format(user_number) + " is I"
    elif user_number == 2:
        Message += format(user_number) + " is II"
    elif user_number == 3:
        Message += format(user_number) + " is III"
    elif user_number == 4:
        Message += format(user_number) + " is IV"
    elif user_number == 5:
        Message += format(user_number) + " is V"
    elif user_number == 6:
        Message += format(user_number) + " is VI"
    elif user_number == 7:
        Message += format(user_number) + " is VII"
    elif user_number == 8:
        Message += format(user_number) + " is VIII"
    elif user_number == 9:
        Message += format(user_number) + " is IX"
    elif user_number == 10:
        Message += format(user_number) + " is X"

print(Message, '\n')


# Question 9
test_1_points = int(input("\nEnter points for test one: "))

Result = ""

if test_1_points >= 0 and test_1_points <= 25:
    test_2_points = int(input("\nEnter points for test two: "))

    if test_2_points >= 0 and test_2_points <= 25:
        exam_points = int(input("\nEnter points for exam: "))

        if exam_points >= 0 and exam_points <= 50:
            total_points = test_1_points + test_2_points + exam_points

            if total_points < 50 or exam_points < 25:
                Result = "Fail!!"
            else:
                if total_points > 80:
                    Result = "Distinction"
                elif total_points <= 80 and total_points >= 60:
                    Result = "Credit"
                elif total_points < 60:
                    Result = "Pass Congratulation !!!"
        else:
            Result = "\nInvalid points for exam must be between 0 - 50."


print(Result)


# Question 10
price_per_package = 99.00

number_of_package = float(input('Enter number of packages purchased: '))

display_message = ""

if number_of_package < 0:
    display_message = "Error. number of packages must be greater than 0."
else:
    discount_percentage = ""

    if number_of_package < 10:
        discount_percentage = 0
    elif number_of_package >= 10 and number_of_package <= 19:
        discount_percentage = .10
    elif number_of_package >= 20 and number_of_package <=49:
        discount_percentage = .20
    elif number_of_package >= 50 and number_of_package <=99:
        discount_percentage = .30
    elif number_of_package >= 100:
        discount_percentage = .40


    package_total = number_of_package * price_per_package
    discount_amount = (package_total) * discount_percentage
    grand_total = package_total - discount_amount
    display_message = "Package total = $" + format(package_total, ',.2f') + \
                      "\nDiscount percentage = " + format(discount_percentage, '.0%') + \
                      "\nDiscount amount = " + format(discount_amount, ',.2f') + \
                      "\nGrand total = $" + format(grand_total, ',.2f')

print("\n" + display_message + "\n")
