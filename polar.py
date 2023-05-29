import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lectura de excel y armado de data (Magnitud)

df_patronpolar = pd.read_excel('PATRON_POLAR_MODIFICADO.xlsx')
df_patronpolar = df_patronpolar.to_numpy()

# Magnitud en todos los grados, para cada fcia

# 32 Hz
pp_32_2 = df_patronpolar[22,1:13]
pp_32_2 = pp_32_2[::-1]
pp_32 = np.hstack((df_patronpolar[22,1:],pp_32_2))
# 63 Hz
pp_63_2 = df_patronpolar[54,1:13]
pp_63_2 = pp_63_2[::-1]
pp_63 = np.hstack((df_patronpolar[54,1:],pp_63_2))
# 125 Hz
pp_125_2 = df_patronpolar[117,1:13]
pp_125_2 = pp_125_2[::-1]
pp_125 = np.hstack((df_patronpolar[117,1:],pp_125_2))
# 250 Hz
pp_250_2 = df_patronpolar[188,1:13]
pp_250_2 = pp_250_2[::-1]
pp_250 = np.hstack((df_patronpolar[188,1:],pp_250_2))
# 500 Hz
pp_500_2 = df_patronpolar[259,1:13]
pp_500_2 = pp_500_2[::-1]
pp_500 = np.hstack((df_patronpolar[259,1:],pp_500_2))
# 1000 Hz
pp_1000_2 = df_patronpolar[329,1:13]
pp_1000_2 = pp_1000_2[::-1]
pp_1000 = np.hstack((df_patronpolar[329,1:],pp_1000_2))
# 2000 Hz
pp_2000_2 = df_patronpolar[442,1:13]
pp_2000_2 = pp_2000_2[::-1]
pp_2000 = np.hstack((df_patronpolar[442,1:],pp_2000_2))
# 4000 Hz
pp_4000_2 = df_patronpolar[517,1:13]
pp_4000_2 = pp_4000_2[::-1]
pp_4000 = np.hstack((df_patronpolar[517,1:],pp_4000_2))
# 8000 Hz
pp_8000_2 = df_patronpolar[667,1:13]
pp_8000_2 = pp_8000_2[::-1]
pp_8000 = np.hstack((df_patronpolar[667,1:],pp_8000_2))
# 16000 Hz
pp_16000_2 = df_patronpolar[775,1:13]
pp_16000_2 = pp_16000_2[::-1]
pp_16000 = np.hstack((df_patronpolar[775,1:],pp_16000_2))

# Datos de ángulos 
angulos = [0, 15, 30, 45, 60, 75, 90, 105, 120, 135,
            150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300, 315, 330, 345, 360]
terc_octava = [32,63,125,250,500,1000,2000,4000,8000,16000]

# Crear un DataFrame con los datos

df = pd.DataFrame({'Ángulo': angulos, 'Magnitud 32':pp_32,
                    'Magnitud 63': pp_63, 'Magnitud 125':pp_125, 'Magnitud 250':pp_250,
                    'Magnitud 500':pp_500, 'Magnitud 1000':pp_1000, 
                    'Magnitud 2000':pp_2000,'Magnitud 4000':pp_4000,
                    'Magnitud 8000':pp_8000,'Magnitud 16000':pp_16000})

# Calcular las coordenadas polares
df['Radianes'] = df['Ángulo'].apply(
    lambda x: x * (3.14159/180))  # Convertir a radianes
df['X'] = df['Magnitud 1000'] * np.cos(df['Radianes'])
df['Y'] = df['Magnitud 1000'] * np.sin(df['Radianes'])

# Graficar el diagrama polar
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(df['Radianes'], df.iloc[:,1:11], label=['32Hz','63Hz'
                                                ,'125Hz','250Hz'
                                                ,'500Hz','1000Hz'
                                                ,'2000Hz','4000Hz'
                                                ,'8000Hz','16000Hz'])
angle = np.deg2rad(225)
ax.legend(loc="upper left",
          bbox_to_anchor=(.9 + np.cos(angle)/2, .9 + np.sin(angle)/2))

# Personalizar el gráfico
ax.set_xticks(df['Radianes'])
ax.set_xticklabels(df['Ángulo'])
# ax.set_rticks([0.2, 0.4, 0.6, 0.8, 1.0])
ax.set_title('Diagrama Polar Behringer ECM8000')
ax.grid(True)

# Mostrar el gráfico
plt.show()
