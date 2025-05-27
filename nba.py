import pandas as pd
import matplotlib.pylab as plt

df = pd.read_csv(r'NBA\PlayerIndex_nba_stats.csv')

nueva_tabla = df.loc[:,['PLAYER_FIRST_NAME','TEAM_NAME','HEIGHT','COUNTRY']]


for n in range(len(nueva_tabla['HEIGHT'])):
    nueva_tabla.at[n, 'NEW_HEIGHT'] = float(str(nueva_tabla.at[n,'HEIGHT']).replace('-','.'))
    
    

more_than_7 = nueva_tabla["NEW_HEIGHT"] > 7
        
print(nueva_tabla[more_than_7])
        




 
