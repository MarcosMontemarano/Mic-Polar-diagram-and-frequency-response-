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
suavizado_0 = suavizado(df_0['Frequency (Hz)'], df_0['Magnitude (dB)'], 3)
suavizado_45 = suavizado(df_45['Frequency (Hz)'], df_45['Magnitude (dB)'], 3)
suavizado_90 = suavizado(df_90['Frequency (Hz)'], df_90['Magnitude (dB)'], 3)

# Traspaso de Dataframe a ndarray para que 
# data de magnitud y frecuencia matcheen 

frec_0 = frec_0.to_numpy()
frec_45 = frec_45.to_numpy()
frec_90 = frec_90.to_numpy()
suavizado_0 = suavizado_0[1:]
suavizado_45 = suavizado_45[1:]
suavizado_90 = suavizado_90[1:]

#Plot Rta. Fcia. 0°
plt.figure(1)
plt.plot(frec_0,suavizado_0)
plt.semilogx()
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude [dB]")
plt.title("Frequency Response 0°")
plt.ylim([-2,9])

#Plot Rta. Fcia. 45°
plt.figure(2)
plt.plot(frec_45,suavizado_45)
plt.semilogx()
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude [dB]")
plt.title("Frequency Response 45°")
plt.ylim([-2,9])

#Plot Rta. Fcia. 90°
plt.figure(3)
plt.plot(frec_90,suavizado_90)
plt.semilogx()
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude [dB]")
plt.title("Frequency Response 90°")
plt.ylim([-2,9])