from nba import nueva_tabla
import numpy as np
import matplotlib.pyplot as plt

grouping_by_team = nueva_tabla.groupby(["TEAM_CITY","COUNTRY"])[['weight_kg','height_m']].mean().sort_values(['TEAM_CITY'], ascending=True)
grouping_by_country = nueva_tabla.groupby('COUNTRY')['height_m'].agg([np.mean,np.median,np.min,np.max,np.size]).round(2)

to_dataframe = grouping_by_country.reset_index()
to_dataframe['proportion_of_players'] = (to_dataframe['size'] / to_dataframe['size'].sum()) *100
to_dataframe.sort_values('proportion_of_players',ascending=False)
print(to_dataframe)

highest_mean_players = to_dataframe[to_dataframe['mean'] == to_dataframe['mean'].max()]
print(highest_mean_players)
