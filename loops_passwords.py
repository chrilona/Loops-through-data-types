employees_salary = input("Input a list of employees salary").split()
for n in range(0, len(employees_salary)):
  employees_salary[n] = int(employees_salary[n])
  
total_salaries=0
for salary in employees_salary:
  total_salaries+=salary
print(total_salaries)  

employees=0
for employee in employees_salary:
  employees+=1
print(employees)  

average_salary=round(total_salaries/employees)
print(average_salary)

#finding the largest value without the max() method
highest_salary=0
for salary in employees_salary:
  if salary > highest_salary:
    highest_salary=salary
print(f"The highest salary is: {highest_salary}")

#finding sum of even numbers in range of 1 to 100 using for loops
divisible_by_two=[]
for num in range(1,101):
    if num%2==0:
         divisible_by_two.append(num)
print(divisible_by_two)
##prints a continous loop

#option1
total_sum =0
for number in range(2,101,2):
 total_sum+=number 
print(total_sum )  
#option2
total_numbers = 0
for number in range(1,101):
  if number%2==0:
    total_numbers+=number
    print(total_numbers)

    #fizzbuzz challenge 
for number in range(50,101):
  if number%3==0 and number%5==0:
    print("FizzBuzz")
  elif number%3==0:
    print("Fizz")
  elif number%5==0:
    print("Buzz")  
  else:
    print(number)   

    #password generator 
import random

# storing the available letters, numbers, and symbols in lists

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# user input
no_letters= int(input("Number of Letters: ")) 
no_numbers = int(input("Number of Numbers: "))
no_symbols = int(input("Number of Symbols: "))
print(" Ultimate PyPassword Generator \n")
# variables for storing the generated password and character type

password = ''  #empty
char_types = [letters, numbers, symbols]

#generating a random order for the selected quantity of each character type

char_type_order = (no_letters * [0] + no_numbers * [1] + no_symbols * [2])
random.shuffle(char_type_order)

# generating the random password

for char_type in char_type_order:
  password += random.choice(char_types[char_type])

# printing the password

print("\n" + password)  