'''
elif = > else if
Gretest of the three number using logical operator 

'''
a = int(input("Enter First Number : "))#70, 70
b = int(input("Enter Second Number : ")) #50,50
c = int(input("Enter Third Number : ")) #20, 100
    
if a>b  and a>c: #70>50  and 70>20  =>     T and T => T
    print(a, "is Greter")
elif b>a  and b>c: #50>70 and 50>20   =>   F and T => F
    print(b, "is Greter")
elif c>a and c>b:  #20>70  and 20>50  =>   F and F => f
    print(c, "is Greter")
