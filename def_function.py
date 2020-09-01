print ('enter any number')
input_i = int(input())

def hello(input_i):
    import random
    return random.randint(2, input_i)


rand_num = hello(input_i)
print('Random number is ' + str(rand_num))
