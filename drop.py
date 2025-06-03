from nba import nueva_tabla
import pandas as pd


table = nueva_tabla
print(table['bmi'].median())

drop_duplicates = table.drop_duplicates(['COUNTRY','TEAM_NAME']).sort_values(['weight_kg','height_m'],ascending=True)
print(drop_duplicates)