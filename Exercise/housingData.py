import pandas as pd
csv = pd.read_csv("./data/Census_Population.csv")
df=pd.DataFrame(csv)
df_row=df.iloc[[89]]
df_row.to_csv('houseIncome.csv')
print(df_row)
#print(df['Mean earnings'][0])
