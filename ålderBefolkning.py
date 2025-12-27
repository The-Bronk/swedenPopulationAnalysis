import pandas as pd

populationWithAge = pd.read_csv("/home/jesper/sweden-population-analysis/rawData/TAB5890_sv.csv", encoding= 'Latin1')

print(populationWithAge.head)
print(populationWithAge.tail)

