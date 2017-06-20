# Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered. 
#If no odd number was entered, it should print a message to that effect.

ask = 0
number = 0
largest = 0
while(ask < 10):
    number = int(input('enter an integer: '))
    ask += 1
    if(number %2 != 0):
        if(number > largest):
            largest = number
print(str(largest))
