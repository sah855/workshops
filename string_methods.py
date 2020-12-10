# islower(), isupper(), isalpha, isalnum, isspace, istitle(),
# startswith(), endswith(), join(), split()
spam = 'THIS IS the mix of text file with alphanumeric values 12345'
print('+++++++++++++++++++++++++++++++++++++++++++++\n+ Below is the string which will be tested: +\n+++++++++++++++++++++++++++++++++++++++++++++\n')
print('"' + spam +'"' + '\n')
test = spam.islower()
print('Testing islower() :' + str(test))
test = spam.isupper()
print('Testing isupper() :' + str(test))
test = spam.isalpha()
print('Testing isalpha() :' + str(test))
test = spam.isalnum()
print('Testing isalnum() :' + str(test))
test = spam.isspace()
print('Testing isspace() :' + str(test))
test = spam.istitle()
print('Testing istitle() :' + str(test))
test = spam.startswith('THIS')
print('Testing startswith() :' + str(test))
test = spam.endswith('12345')
print('Testing endswith() :' + str(test))
test = ' #JOIN MARK# '.join(['cat', 'bat', 'rat'])
print('Testing join() :' + str(test))
joinmark = ' #VRIABLE JOIN MARK# '
test = joinmark.join(['cat', 'bat', 'rat'])
print('Testing join() :' + str(test))
print('Testing join() with 2 new line\n\n' + '\n\n'.join(['cat', 'bat', 'rat']))
test = spam.split()
print('Testing Split() :' + str(test) )
test = spam.split('a')
print('Testing Split() on specific alphabet "a" :' + str(test) )

# Center alignment of test
print('\nEneter your name :')
name = input()A
length = len(name)
print('\nBelow is the sample of Center(), Leftjust() and rightjust()\n')
print(name.center(length + 10, '+'))
# Leftjust() and rightjust()
print(name.ljust(length + 10, '+'))
print(name.rjust(length + 10, '+'))

# Using strip() for whitespace and any test
print('\n')print('      rstrip() with spaces    '.rstrip())
print('      lstrip() with spaces    '.lstrip())
print('SpamSpammSpamSpamBaconSpamEggsSpamSpam'.strip('Spam'))


# Using replace()
replaceablestring = 'Hi its been a hot day'
print('using replace()')
print(replaceablestring.replace('hot', 'HOT'))










