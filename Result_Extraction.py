import os
import pandas as pd
defaultpath =os.getcwd()
filpath = os.chdir(r"C:\Users\abhinav_sah\AppData\Local\Programs\Python\Python37-32")

## Initialization & csv file reading
result = pd.read_csv('sample.csv', index_col=0)
length = len(result)

## Having the logic to select only the transaction name and value rows
temp1 = result.iloc[[0]]
for i in range(length-1):
    if result.index[i] == 'End':
        temp = result.iloc[[i + 1]]
        temp1 = temp1.append(temp)
        if result.index[i + 8] == 'transaction' or result.index[i + 8] == 'End':
            temp = result.iloc[[i + 7]]
            temp1 = temp1.append(temp)

## Reset index to treat index as a column and index resetted to 0, 1, 2, 3..values
## Having the value copied from the ...cell to the one above cell, all blanks are removed

temp2 = temp1
temp2 = temp2.reset_index()
col_len = len(temp2.columns)
temp2_len = len(temp2)
for outer_column in range(1, col_len, 1):
    for l in range(0, temp2_len - 2, 2):
        temp2.iat[l + 1, outer_column] = temp2.iat[l + 2, outer_column]

## Renaming the column named "index" to "Scenario"
temp3 = temp2.rename(columns={'index': 'Scenarios'})

## Dropping the rows which have...values
temp4 = temp3.drop(temp3[temp3.Scenarios.str.contains(r'[^0-9a-zA-Z_]')].index)

## Dropping the duplicate rows
temp4 = temp4.drop_duplicates()

## Writing to csv file
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
temp4.to_csv('testing_result_' + timestr +'.csv')

