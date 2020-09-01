# For loop normal
print('What do you want to print?')
prntval = input()
print('How many time do you want to print?')
val = int(input())
# Iteration to start
for i in range(val):
    print(prntval + ' ' + str(i))


# For loop Range
print('What do you want to print?')
prntval = input()
print('How many time do you want to print?')
val = int(input())
# Iteration to start
for i in range(0, val):
    print(prntval + ' ' + str(i))


# For loop Step Up
print('What do you want to print?')
prntval = input()
print('How many time do you want to print?')
val = int(input())
# Iteration to start
for i in range(0, val, 2):
    print(prntval + ' ' + str(i))
