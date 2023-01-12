'''
code editor ----print()----> console (output screen)

if there is need to bring user input from output screen or console to the code editor or to store in a variable, we need
input() function.

syntax:

    variable = input()

step 1= give message to user => print()
step 2 = store that imput intp variable => var = input()

'''


'''
print("Enter first number : ")
x = input()
#print("value of x is : ", x)
print("Enter Second number : ")
y = input()
z=x+y
print("Addition of ",x,"and",y, "is : ",z)

In above code value are not getting added, they are joinred or concatenated.

Input given by user in python is always stored as string by default.

if there is need to convert string to number use following
functions.

int() : this functions is used to convert string to int.
float : this functions is used to convert string to float.

'''

print("Enter first number : ")
x = input() #string
#print(type(x))
a=float(x)
#print(type (a))      


print("Enter the second number : ")
y = input()
b = int(y)

z=a+b
print("Addition of", a , "and" , b , "is" , z)

