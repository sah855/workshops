def isphonenumber(text):
    if len(text) != 12:
        return False # not a phone number size
    for i in range(0,3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False # missing number
    if text[7] != '-':
        return False # missing second dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False # missing last four digit
    return True

print('Input any number')
phone = input()
print ('The phone number ' + str(phone) + ' seems to be ' + '"' + str(isphonenumber(phone)) + '"' +  ' for a a valid number')
