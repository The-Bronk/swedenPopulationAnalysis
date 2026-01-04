import pandas as pd
# import openpyxl

populationRaw = pd.read_excel("/home/jesper/sweden-population-analysis/be0101_folkmangdkom2024.xlsx", header= None)
6
förstaKommunAle = populationRaw.iloc[6,0]
sistaKommunÖvertåmeo = populationRaw.iloc[295,0]
#print(förstaKommunAle)
#print(sistaKommunÖvertåmeo)

#Ta bort kommentarer från dokumentet
if förstaKommunAle != 'Ale' or sistaKommunÖvertåmeo != 'Övertorneå':
    print('Throw Exception, unexpected pattern, review index')
else:
    populationRaw = populationRaw.iloc[5:296]


#Printing, debug
print(populationRaw.iloc[290, 1])
"""print(populationRaw.dtypes)
print(populationRaw.columns)
print(repr(populationRaw[0].iloc[1]))
print(repr(populationRaw[1].iloc[1]))
print(repr(populationRaw[2].iloc[1]))
print(repr(populationRaw[3].iloc[1]))
print(repr(populationRaw[4].iloc[1]))
print(populationRaw.isna().sum() """

#print(populationRaw.head(5))
#print(populationRaw.tail(5))





