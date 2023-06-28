import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('mgck_1.txt', sep='\s+', comment='#')

# Asignar los números del 1 al 10 como cabeceras
nuevas_cabeceras = range(1, 11)
df = pd.concat([df], axis=1)
df.columns = nuevas_cabeceras
print(nuevas_cabeceras)
