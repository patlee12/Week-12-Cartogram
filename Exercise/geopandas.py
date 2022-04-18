import pandas as pd
import geopandas as gpd
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from descartes import PolygonPatch

df_counties = gpd.read_file("states.json")

df_counties.plot(figsize=(12, 10))

# Read in income data from census
csv = pd.read_csv("Census_Population.csv")
df = pd.DataFrame(csv)
df = df.loc[89].filter(like="!!Total!!Estimate")
df = df.to_frame().reset_index()
df.columns = ["state", "meanIncome"]
df = df.replace("!!Total!!Estimate", "", regex=True)
df = df.dropna()

print(df)

df.to_csv('houseIncome.csv')

df_counties_data = df_counties.join(df)
df_counties_data = df_counties_data.dropna()
print(df_counties_data)

df_counties_data.to_file("states_output.json", driver="GeoJSON")
