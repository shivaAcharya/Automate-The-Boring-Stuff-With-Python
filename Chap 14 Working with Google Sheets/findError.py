# Program to find error in googlesheet

import ezsheets
ss = ezsheets.Spreadsheet('##########################')
sheet = ss[0]
print(sheet.title)
'''i = 0

for i in range(2, sheet.rowCount):
    if int(sheet.getRow(i)[0])*int(sheet.getRow(i)[1]) != int(sheet.getRow(i)[2]):
        break
print(i)'''
