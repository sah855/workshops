import os
import pandas as pd
defaultpath =os.getcwd()
filpath = os.chdir(r"C:\Users\abhinav_sah\AppData\Local\Programs\Python\Python37-32")

## Initialization & csv file reading
result = pd.read_csv('sample.csv', index_col=0)
length = len(result)

## Having the logic to insert a blank row when there is no "transaction" label
temp2 = result.iloc[[0]]
for i in range(length-1):
	temp = result.iloc[[i]]
	# print("*******************TEMP****************")
	# print(temp)
	temp2 = temp2.append(temp)
	# print("*******************TEMP ONE****************")
	# print(temp1)
	if result.index[i+1] == 'End' and result.index[i] !='transaction':
		temp2 = temp2.append(pd.Series(name='empty_row', dtype='object'))
		# print("*******************TEMP ONE CONDITION****************")
		# print(temp1)

## Renaming the column named "index" to "Scenario"
temp3 = temp2.rename(columns={'index': 'Scenarios'})

## Writing to csv file
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
temp3.to_csv('testing_result_rowinsert_' + timestr +'.csv')