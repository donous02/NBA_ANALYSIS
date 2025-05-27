import pandas as pd
import matplotlib.pylab as plt

df = pd.read_csv(r'NBA\PlayerIndex_nba_stats.csv')

nueva_tabla = df.loc[:,['PLAYER_FIRST_NAME','TEAM_NAME','HEIGHT','COUNTRY']]

counter_of_less_than_6 = 0


for n in range(len(nueva_tabla['HEIGHT'])):
    nueva_tabla.at[n, 'NEW_HEIGHT'] = float(str(nueva_tabla.at[n,'HEIGHT']).replace('-','.'))
    
    
more_than_7_df = pd.DataFrame()

for i in range(len(nueva_tabla['NEW_HEIGHT'])):
    if nueva_tabla.at[i,'NEW_HEIGHT'] > 7.0:
        more_than_7_df = nueva_tabla.loc[:,['PLAYER_FIRST_NAME','NEW_HEIGHT','COUNTRY']]
        
        
print(more_than_7_df)
        
   
        





