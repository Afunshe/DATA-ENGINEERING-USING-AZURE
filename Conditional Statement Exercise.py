##IF STATEMENT

age = 20
if age >= 18:
    print('You are an adult')

age = 15
if age >= 18:
    print('You are an adult')

## CHECKING NUMBERS

number = 2
if number > 5:
    print('number is greater than 5')

##CHECKING SALARY

salary = 7000
if salary >5000:
    print('high income')

salary = 4000
if salary >5000:
    print('high income')

##IF...ELSE

age = 17
if age >= 18:
    print('eligible to vote')
else: 
    print('not eligible')

age = 25
if age >= 18:
    print('eligible to vote')
else: 
    print('not eligible')

##EVEN OR ODD

num = 8
if num % 2 == 0:
    print('even number')
else:
    print('odd number')
    
num = 21
if num % 2 == 0: ## modulus
    print('even number')
else:
    print('odd number')
    
##IF...ELIF...ELSE

marks = 85
if marks >= 90:
    print('Grade A')
elif marks >= 80:
    print('Grade B')
elif marks >= 70:
    print('Grade C')
else:
    print('Grade D')

##INPUT PROGRAMMING

age = int(input('Enter your age:  '))
if age >= 18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')

##USING MULTIPLE ELIF STATEMENT

marks = int(input('Enter your marks:  '))
if marks >= 90:
    print('Grade A')
elif marks >= 80:
    print('Grade B')
elif marks >= 70:
    print('Grade C')
elif marks >= 60:
    print('Grade D')
else:
    print('Grade F')




