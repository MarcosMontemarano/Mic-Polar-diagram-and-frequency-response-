import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from suavizado import suavizado

# Lee el archivo Excel y crea un DataFrame
df_0 = pd.read_excel('RESPUESTA_FRECUENCIA_0.xlsx')
df_45 = pd.read_excel('RESPUESTA_FRECUENCIA_45.xlsx')
df_90 = pd.read_excel('RESPUESTA_FRECUENCIA_90.xlsx')

# Extrae columna de frecuencias
frec_0 = df_0.iloc[1:,[0]]
frec_45 = df_45.iloc[1:,[0]]
frec_90 = df_90.iloc[1:,[0]]

# Extrae columna de magnitud en dB
db_0 = df_0.iloc[1:,[1]]
db_45 = df_45.iloc[1:,[1]]
db_90 = df_90.iloc[1:,[1]]

# Suavizado con función externa
suavizado_0 = suavizado(df_0['Unnamed: 0'], df_0['rta freq 0°'], 3)

#Plot Rta. Fcia. 0°
plt.figure(1)
plt.plot(frec_0,db_0)
plt.semilogx()
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude [dB]")
plt.title("Frequency Response 0°")
plt.ylim([-2,9])

#Plot Rta. Fcia. 45°
plt.figure(2)
plt.plot(frec_45,db_45)
plt.semilogx()
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude [dB]")
plt.title("Frequency Response 45°")
plt.ylim([-2,9])

#Plot Rta. Fcia. 90°
plt.figure(3)
plt.plot(frec_90,db_90)
plt.semilogx()
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude [dB]")
plt.title("Frequency Response 90°")
plt.ylim([-2,9])