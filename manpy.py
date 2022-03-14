import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

basepath = "C:/Users/ERIKSSON/Documents/DataAnalytics"
archivo1 = basepath + "/venta1.xlsx"
archivo2 = basepath + "/venta2.xlsx"
df1 = pd.read_excel(archivo1, sheet_name = 'Tienda A')
df2 = pd.read_excel(archivo1, sheet_name = 'Tienda B')
df3 = pd.read_excel(archivo2, sheet_name = 'Tienda C')
df1.info