'''
Need of Loops:
=============
    To achive the reusability or to reduce code repetation, there is need of loop.

   
'''

# display "hello word" 5 or 10 times on the console.

print("Hello Words")
print("Hello Words")
print("Hello Words")
print("Hello Words")
print("Hello Words")
print("Hello Words")
print("Hello Words")
print("Hello Words")
print("Hello Words")
print("Hello Words")

'''
in above approch of writing same instruction or statement
again and again , this led to code repeatation.

code repetation has following disadvantages:
============================================

1)length of the program increses due to wich
debugging sometimes become difficult.

2)memory difficult.

3)waste of compilere or enterpreter time as same code id exicuted.

In order to remove discard disadvantage caused by the
code repeataion there is need of loop control instruction .


WHAT IS LOOP CONTROL INSTRUCTION?
=================================

The instruction wich allows us to write code once and repeat
N number of time or infinite number of time are called as
loop control instruction.

Types of loops :
===============
1)while loops
2)for loops

'''

#Working of loops =>
=================

working:
step1:initialization [Done only once]
step2:check condition 
step3:If condition is True then executed code or loop body.
step4:increment or decrement 
step5:repeat step2 to step4 till condition is True.
step6:Once condition is False ,go to step7.
step7:stop

                          initialization
                                |
				|       False
                 ----------->condition-------->Out of loop
                |               |
                |               | True
                |          code in loop[Body]
                |               |
                |               |
                |               |
		incre/decre<----
'''

#printing Hello World 10 times

i=1
while i<=10:
    print("Hello World")
    i+=1 #i=i+1
    
'''
i   i<=10   print("Hello World")   i+=1 => i=i+1
1   1<=10 T Hello World            i=1+1=2
2   2<=10 T Hello World            i=2+1=3
3   3<=10 T Hello world            i=3+1=4
4   4<=10 T Hello World            i=4+1=5
5   5<=10 T Hello World            i=5+1=6
6
7
8
9
10  10<=10T Hello World            i=10+1=11
11  11<=10F Loop Stops
'''




