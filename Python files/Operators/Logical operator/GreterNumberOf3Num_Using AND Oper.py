'''
logical operator

Gretest of the three number using logical operator 

'''
a = int(input("Enter First Number : ")#70, 70
b = int(input("Enter Second Number : ") #50,50
c = int(input("Enter Third Number : ") #20, 100
    
if a>b  and a>c: #70>50  and 70>20  =>   T and T => T
    print(a, "is Greter")
if b>a  and b>c: #50>70 and 50>20   =>   F and T => F
    print(b, "is Greter")
if c>a and c>b:  #20>70  and 20>50  =>   F and F => f
    print(c, "is Greter")

'''
In user inout of a = 70 , b = 50,  c  =20
First if condition is evaluated to be true and we got the result
of gretest of three numbers.

if we got thr result first if condition , then ideally there is no need o check if condition.
Since in above Program its checking other two conditions ,
there is wester of interpreter time in code exucation
wich is not going to give us output.

'''
