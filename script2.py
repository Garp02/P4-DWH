import pandas as pd
import numpy as np

datos = 'Branch.csv'

try:

    df = pd.read_csv(datos)

except FileNotFoundError:

    print(f"Error: No se encontró el archivo '{datos}'.")
    exit()

# Explorar los datos
print("Primeras filas del archivo Branch.csv:\n")
print(df.head()) 

# Identificar características
print("\nInformación general del DataFrame:\n")
print(df.info())

# Estadísticas 

# Total de registros
a1 = len(df)
print(f"\nTotal de registros = {a1}")

# Valores faltantes por campo
a2 = df.isnull().sum()
print("\nValores faltantes por campo:\n", a2.to_string())

completitud = 1 - (a2 / a1)
print("\nCompletitud campo:\n", completitud.round(3).to_string())

# Registros duplicados
a3 = df.duplicated().sum()
print(f"\nRegistros duplicados = {a3}")

# Códigos postales válidos (5 dígitos)
if 'branch_zip' in df.columns:
   
    zip_limpios = df['branch_zip'].fillna('').astype(str).str.replace(r'\.0$', '', regex = True)
    regex_zip = r'^\d{5}$'
    a4 = zip_limpios.str.match(regex_zip).sum()
    print(f"\nCódigos postales válidos = {a4}")

else:

    print("\nNo se encontró 'branch_zip' para validar códigos postales.")

# Indicadores estadísticos 
print("\nValores únicos por campo:")
print(df.nunique().to_string())