import pandas as pd
import numpy as np

citi_csv = 'database-sucia-citi.csv'

try:
    df_original = pd.read_csv(citi_csv, delimiter = ',', header = 0)
    print(f"\n'{citi_csv}' cargado correctamente.")

except FileNotFoundError:

    print(f"Error: No se pudo encontrar el archivo '{citi_csv}'.")
    print("Asegúrate de que el archivo esté en la misma carpeta que este script.")
    exit()

# Renombrar los encabezados con un diccionario
columnas_branch = {
    'Branch Name': 'branch_name',
    'Street Address': 'branch_address',
    'State': 'branch_state',
    'County': 'branch_city',
    'Zipcode': 'branch_zip'
}

# Copia para no alterar el original
df_branch = df_original[columnas_branch.keys()].copy()
df_branch = df_branch.rename(columns = columnas_branch)

# Llenamos las columnas faltantes
df_branch['branch_key'] = np.arange(1, len(df_branch) + 1)
df_branch['branch_type'] = np.nan

# Ordenar columnas de Branch
columnas_finales = [
    'branch_key',
    'branch_name',
    'branch_address',
    'branch_city',
    'branch_state',
    'branch_zip',
    'branch_type'
]

df_branch = df_branch[columnas_finales]

archivo_final = 'Branch.csv'
df_branch.to_csv(archivo_final, index = False, sep = ',')

print(f"\nArchivo '{archivo_final}' guardado.")

print(df_branch.head())