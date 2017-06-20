#Finger exercise 2.2
# Write a program that examines three variables -- x, y, and z -- and prints the largest odd number among them. If none of them are odd, it should print a message to that effect.
max = 0
if x % 2:
  max = x
if y % 2:
  if y > x:
    max = y
if z % 2:
  if x > y:
    max = z
if max:
  print('Largest odd number is ' + str(max))
else:
  print('No odd value')
