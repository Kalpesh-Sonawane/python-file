'''

need of conditional statement
==============================

In program when there is need to take decisin based on certain condition,
then there is need of conditional statement.

What is  conditional statement?
===============================
the statement or instruction wich helps to give decision based on certain condition on a program
are called as condition statement or conditionalv instruction or dicision control statement.

types of conditional statement :
=================================
1)if statement
2)if else statement
3)nested if else 
4)logical operator
5)elif

1)if statement
==============

Syntax:

if condition :
      code in if block


Working :
=========

if the condition is  true then execute if block of statement.

if the condition is  flase then it wont execute if block of statement.



if...else
=========

if condition :
    code in if block

else:
    code in else block
    
Working :
=========
    if the condition is  true then execute if block of statement.

if the condition is  flase then  execute else block of statement.



'''

# Two number enter by user , WAP to find gretest of two numbers

num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number :"))

if num1 > num2 :
    print(num1,"is greter than",num2)
   
else:
    
     print(num1,"is smaller than",num2,)

