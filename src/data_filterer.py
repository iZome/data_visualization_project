import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

terrorist_attacks = np.genfromtxt(dir_path + '/../data/globalterrorismdb_0617dist.csv',
                                    delimiter = ',',
                                    missing_values='',
                                    filling_values=0.0)
