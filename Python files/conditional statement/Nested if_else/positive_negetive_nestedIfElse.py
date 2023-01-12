'''
Nested if else
===============

When there is need to give decision based on more that one condition.

Syntax :

if condition :
       if condition2 :
             execute if block
       else:
           execute else block
else :
    if condition 3:
          excute if block
    else:
         execute else block

Example positive nigetive number

step1: first check for zero and non zero
step2: if zero then display neither positive nor negetive .
step3: if non-zero , then further check for positive and nigetive

'''
n = int(input("Enter number to check positive or negetive :"))

if n==0:
    print(n,"Is neither positive nor negetive")
else :
    if n > 0:
        print(n,"Is positive number  ")
    else :
        print(n,"Is negetive number ")
