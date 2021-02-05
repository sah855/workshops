'''

*********************
*                   *
*                   *
*                   *
*********************
'''

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"Symbol" needs to be a string of length 1')
    if (width < 2) or (height < 2):
        raise Exception('"Width" and "Height" must be greater or equal to 2')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width -2 )) + symbol)

    print(symbol * width)

boxPrint('O', 2, 4)

import traceback
import os

try:
    raise Exception('This error message will be displayed in Exception')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info is written to error_log,txt')
    print('The current working directory is: ' + os.getcwd())