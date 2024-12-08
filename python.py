import pandas as pd
import numpy as np
data = pd.read_csv("data/Barcelona_Fotocasa_HousingPrices.csv")
data.rename(columns={'real_state': 'property_type'}, inplace=True)
data = data.dropna(subset=['property_type'])
data.reset_index(drop=True, inplace=True)


