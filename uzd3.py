import pandas as pd
s = 0
data = pd.read_csv('data.txt')
for index, row in data.iterrows():
    if row['Country'] == 'Latvia':
        if row['Industry'] == 'Telecommunications':
            s+=1
print(s)





#if row['Country'] == 'Latvia':
#if [4] == 'Telecommunications':