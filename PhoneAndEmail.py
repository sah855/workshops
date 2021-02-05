#! python3
import re, pyperclip

# TODO: Create a regex for phone numbers
phoneRegex = re.compile(r''' 
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)
(\s|-)              # first seperator
\d\d\d              # first 3 digits
-                   # seperator
\d\d\d\d            # last 4 digits
(((ext(\.)?\s)|x)    # extention word-part (optionl)
 (\d{2,5}))?        # extention number-part (optional)
 )
''', re.VERBOSE)

# TODO: Create a regex for email address
emailRegex = re.compile(r'''
# something.+@something.com
[a-zA-Z0-9_.+]+    # name parrt
@                  # @ symbol
[a-zA-Z0-9_.+]+    # domain name part


''', re.VERBOSE)

# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

## print(extractedPhone)
## print(extractedEmail)


allPhoneNumbers =[]
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
## print(allPhoneNumbers)

# TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)