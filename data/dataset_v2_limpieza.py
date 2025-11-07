import pandas as pd

# 1. Cargar el dataset
df = pd.read_csv("C:/Users/USER/automl_dvc/data/dataset_v2.csv")

# 2. Manejo de Valores Faltantes
# Mostrar el conteo y el porcentaje de valores faltantes
print("\n--- Verificación de Valores Faltantes (Nulos) ---")
missing_values = df.isnull().sum()
missing_percentage = 100 * missing_values / len(df)
missing_df = pd.DataFrame({
    'Conteo Faltante': missing_values,
    'Porcentaje Faltante (%)': missing_percentage
}).sort_values(by='Conteo Faltante', ascending=False)
print(missing_df[missing_df['Conteo Faltante'] > 0])

# En este caso, no se aplicó ninguna imputación o eliminación porque no hay nulos.

# 3. Manejo de Duplicados
initial_rows = len(df)
df.drop_duplicates(inplace=True)
duplicates_removed = initial_rows - len(df)

print(f"\n--- Verificación de Filas Duplicadas ---")
print(f"Filas iniciales: {initial_rows}")
print(f"Filas después de eliminar duplicados: {len(df)}")
print(f"Filas duplicadas eliminadas: {duplicates_removed}")

# 4. Guardar el DataFrame limpio en un nuevo archivo CSV
df.to_csv("C:/Users/USER/automl_dvc/data/dataset_v2.csv", index=False)
print("\nDatos limpios guardados en 'dataset_v2.csv'")
