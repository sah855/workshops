import requests
##res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res = requests.get('file://neonwmdmctl005.aus.amer.dell.com/FY21_RESULTS/CIL/FY22_0202/Run02_16thJan/report-Jan-16-00_22_files/transactions.html')
sc = res.status_code
len(res.text) # res.txt have all the content of the file
print(sc)
print(res.text[:500]) # prints first 500 characters of the file
badResponse = requests.get('https://google.com')
print (badResponse.text[:101])
print('####################################################################')
print('the length of "google.com" is: ' + str(len(badResponse.text)))
