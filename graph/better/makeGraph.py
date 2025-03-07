#!/bin/python3
import pandas as pd
import seaborn as sns
import sys

def process_country_group(group):
    # Sort by year to ensure we get the lowest year first
    group = group.sort_values('Year')
    # Get the first temperature (from lowest year)
    base_temp = group.iloc[0]['Temp']
    # Calculate the difference
    group['Temp'] = (group['Temp'] - base_temp)
    return group

df = pd.read_csv(sys.argv[1],names=['Country', 'Year','Temp'], header=None)
df = df[df["Year"] > int(sys.argv[2])]
df = df.groupby('Country', group_keys=False).apply(process_country_group)
df = df[df["Temp"] > -2]
print(df)

ax = sns.lineplot(x = 'Year',
                  y = 'Temp',
                  hue = 'Country',
                  data = df)

sns.regplot(data=df, x="Year", y="Temp", scatter=False)

ax.figure.savefig("year-temp.png")
