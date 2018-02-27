import pandas as pd
import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

#terrorist_attacks = np.genfromtxt(dir_path + '/../data/globalterrorismdb_0617dist.csv',
#                                    delimiter = ',',
#                                    missing_values='',
#                                    filling_values=0.0)

terrorist_attacks = pd.read_csv(dir_path + '/../data/globalterrorismdb_0617dist.csv',
                                delimiter = ',',
                                encoding = 'ISO-8859-1')

terrorist_attacks.rename(columns={'iyear':'Year','imonth':'Month','iday':'Day',
                        'country_txt':'Country','region_txt':'Region',
                        'attacktype1_txt':'AttackType','target1':'Target',
                        'nkill':'Killed','nwound':'Wounded','summary':'Summary',
                        'gname':'Group','targtype1_txt':'Target_type',
                        'weaptype1_txt':'Weapon_type','motive':'Motive'},inplace=True)

print terrorist_attacks.head(3)
