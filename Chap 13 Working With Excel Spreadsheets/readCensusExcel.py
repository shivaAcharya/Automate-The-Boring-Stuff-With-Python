#! python3
# readCensusExcel.py - Program to Tabulate population and number of Census Tracts for each county

import openpyxl, pprint
print('Opening workbook......')

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

for row in range(2, sheet.max_row + 1):
    #Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    #TODO: Open a new text file and write the contents of countyData to it.

    #Make sure the key for this state exist.
    countyData.setdefault(state, {})

    #Make sure the this state has census tracts and population.
    countyData[state].setdefault(county, {'tracts' : 0, 'pop' : 0})

    #Each row represents one census tract, so increment by one.
    countyData[state][county]['tracts'] += 1
    #Increase the county pop by the pop in this census tract.
    countyData[state][county]['pop'] += int(pop)

#TODO: Open a new text file and write the contents of countyData to it.

print('Writing Results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
