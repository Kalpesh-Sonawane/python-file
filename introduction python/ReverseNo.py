'''
a three digit number is entered through keyboard . write a program to
A) reverse that  digit.
B) sum of digit.


A)  input                        output
    n=675 -------> logic ------>  576

B)  n=675 -------> logic -------> 6+7+5 = 18

     675=6*100+7*10+5*1
     576=5*100+7*10+6*1

     sum = 6+7+5

     digit separation => % and // with division 10
'''
#reverse number
x=print("Enter three digit number : ")
x= input()
n=int(x)  #convert string into integer

a=n%10 # a=5
b=n//10 #b=67
c=b%10  #c=67%10=7
d=b//10 #d=67//10=6

rev=a*100+c*10+d*1  # rev = 5*100+7*10+6*1 = 500+70+6=576
print("orignal number :", n)
print("reverse number :", rev)


#sum of all number

s = a+c+d
print("sum of digit:" , s)



'''
2 number are enter by users . write a program to swap content or value of two numbers.
'''

a = int(input("Enter number for a :"))
b = int(input("Enter number for b :"))

print('''BEFORE SWAPPING:
         X :''',a  , ","
      '''y :''',b)

# SWAPPING LOGIC

t=a
a=b
b=t


print('''AFTER SWAPPING:
         X :''',a  , ","
      '''y :''',b)


# swapping of two numbers using two variable.

# amount is entered by using, write a program to find how many
#demonation of 2000 rs notes , 500 rs notes , 200 rs notes and 100 rs notes will be given to user .


'''
Amount 3800

number of rs.2000 notes : 1
number of rs.500 notes : 3
number of rs.200 notes : 1
number of rs.100 notes : 1'''
