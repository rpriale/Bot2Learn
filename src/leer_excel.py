import pandas as pd
# Ruta al archivo excel
ruta_excel = 'Users/rpria/OneDrive/Documentos/AI_projects/Ai Design Course/Ley_contra_crimen_organizado_estructurado.xlsx'

# Leer tabla Excel en un dataframe de Pandas
df = pd.read_excel(ruta_excel)

# Mostrar las primeras filas para verificar la carga
print(df.head())

# Opcional: Mostrar la estructura general del DataFrame
print(df.info())

# Opcional: Imprimir algunas estadísticas descriptivas
print(df.describe(include='all'))