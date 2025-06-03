import pandas as pd
import matplotlib.pylab as plt
import numpy as np


df = pd.read_csv(r'NBA\PlayerIndex_nba_stats.csv')


nueva_tabla = df.loc[:,['PLAYER_FIRST_NAME','TEAM_NAME','HEIGHT','WEIGHT','COUNTRY','TEAM_CITY']]


#eu_players = nueva_tabla[nueva_tabla['COUNTRY'].isin(['France','Spain'])]
#print(eu_players)
#print(eu_players.values)

#ITERATE DATAFRAMES

for n in range(len(nueva_tabla['HEIGHT'])):
    nueva_tabla.at[n, 'NEW_HEIGHT'] = float(str(nueva_tabla.at[n,'HEIGHT']).replace('-','.'))
    

#
nueva_tabla['weight_kg'] = round(nueva_tabla['WEIGHT'] * 0.45359237,ndigits=2)
nueva_tabla['height_m'] = round(nueva_tabla['NEW_HEIGHT'] *0.3048 , ndigits=2)
nueva_tabla['bmi'] = round(nueva_tabla['weight_kg'] / (nueva_tabla['height_m'] * nueva_tabla['height_m']),ndigits=2)
#print(nueva_tabla[['PLAYER_FIRST_NAME','weight_kg','height_m','bmi']])

#FILTERING
bmi_low = nueva_tabla[nueva_tabla['bmi'] < 20]
print(f"Head():------------------ \n {bmi_low[['PLAYER_FIRST_NAME','COUNTRY','bmi']].head()}")
print("MIN BMI PLAYER ----------------------------------------------")
min_bmi_player = bmi_low[bmi_low['bmi'] == bmi_low['bmi'].min()]
print(min_bmi_player) 
print("MIN BMI PLAYER ----------------------------------------------")

##################
#COUNTING_XD

prop_countries = nueva_tabla['COUNTRY'].value_counts(ascending=False)
print(prop_countries)


#DROPPING_DPLICATES 
no_duplicates_team = nueva_tabla.drop_duplicates(['COUNTRY','TEAM_NAME']).sort_values(['weight_kg','height_m'],ascending=False)
no_duplicates_team['repeateds_teams'] = no_duplicates_team['TEAM_NAME'].value_counts()
#print(no_duplicates_team)


    
    
    



        




 
