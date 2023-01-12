'''
Armstrong number =
===================

sum of cube of digit = orignal number

n = 153

1cube + 5 cube + 3 cube = 1+125+27 = 153

Que) A three digit number is entred by user . write a program to find whether number is armstrong or not


step1 : start
step2 : digit seperation => % , // 10
step3 : cube and add or summation.
step4 : check  summation is equal to number enter by user.
step5 : if it fount same then its armstrong
step6 : otherwise is not armstrong
step7 : stop


'''

n = int(input("Enter Three digit number : "))

a = n%10 # 153 % 10 = 3
b = n//10 # 153 // 10 = 15
c = b%10  # 15%10 = 5
d = b//10 # 15 // 10 = 1

s = a**3+c**3+d**3 # cube and summation

if s == n:
    print(n, "is armstrong number")
else:
     print(n, "is not armstrong number")


