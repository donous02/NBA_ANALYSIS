import pandas as pd
import matplotlib.pylab as plt
import numpy as np


df = pd.read_csv(r'Projects\NBA_ANALYSIS\PlayerIndex_nba_stats.csv')


nueva_tabla = df.loc[0:10,['PLAYER_FIRST_NAME','TEAM_NAME','HEIGHT','COUNTRY']]


#ITERATE DATAFRAMES
for lab, row in nueva_tabla.iterrows():
    nueva_tabla.loc[lab,'num_of_country'] = len(row['COUNTRY'])
print(nueva_tabla)

for n in range(len(nueva_tabla['HEIGHT'])):
    nueva_tabla.at[n, 'NEW_HEIGHT'] = float(str(nueva_tabla.at[n,'HEIGHT']).replace('-','.'))
    


    
#FILTERING
more_than_7 = nueva_tabla["NEW_HEIGHT"] > 7
#NP_FILTERING
between_two = nueva_tabla[np.logical_and(nueva_tabla['NEW_HEIGHT'] > 7.2, nueva_tabla['NEW_HEIGHT']<7.5)]
            #print(between_two)



        




 
