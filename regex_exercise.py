import re
beginswithRegex = re.compile(r'^Hello') # for any digit search in the beginning
print(beginswithRegex.search('Hello 777 8889999. This is my number 7776089999 and the other number is 6089999'))

endswithRegex = re.compile(r'Hello$')
mo = endswithRegex.search('This is Tom and i say Hello')
print ("I matched the test ", mo.group(0)) #Match Object will have the searched value in clear form

alldigitsRegex = re.compile(r'^\d+$')
mo = alldigitsRegex.search('23433432432432')
print("Print only if the string start and ends with digit  and no characters in between", mo.group())
