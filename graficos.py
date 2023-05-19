import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from suavizado import suavizado

# Lee el archivo Excel y crea un DataFrame
df_0 = pd.read_excel('RESPUESTA_FRECUENCIA_0.xlsx')

# Extrae columna de frecuencias
frec_0 = df_0.iloc[:,[0]]

# Extrae columna de magnitud en dB
db_0 = df_0.iloc[:,[1]]

# Suavizado con función externa

suavizado_0 = suavizado(frec_0,db_0,3)