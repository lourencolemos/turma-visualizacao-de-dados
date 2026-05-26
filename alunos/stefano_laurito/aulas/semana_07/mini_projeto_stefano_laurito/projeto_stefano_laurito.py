
# Etapa 1 - Importação de bibliotecas e da base de dados
 
import pandas as pd

# Importação da base
df = pd.read_csv("base_varejo.csv", sep=";")

# Visualização inicial
print("\nVISUALIZAÇÃO INICIAL DA BASE")
print(df.head())

# Informações gerais do dataframe
print("\nVERIFICAÇÃO DOS TIPOS DE DADOS")
df.info()

print("\nPROBLEMA IDENTIFICADO:")
print("A coluna DATA foi carregada como texto (str) e precisará ser convertida para datetime.")

# Verificação de valores nulos
print("\nVERIFICAÇÃO DE VALORES NULOS")
print(df.isnull().sum())

print("\nPROBLEMA IDENTIFICADO:")
print("Foram encontradas colunas totalmente vazias (Unnamed), indicando inconsistência estrutural no arquivo CSV.")

# Criação de uma cópia da base original
df_limpo = df.copy()

print("\nCÓPIA DA BASE CRIADA COM SUCESSO")

# Remoção das colunas totalmente vazias
df_limpo = df_limpo.drop(columns=[
    "Unnamed: 10",
    "Unnamed: 11",
    "Unnamed: 12",
    "Unnamed: 13"
])

print("\nCOLUNAS VAZIAS REMOVIDAS")
print(df_limpo.info())

# Verificação de duplicatas
duplicatas = df_limpo.duplicated()
print("\nVERIFICAÇÃO DE DUPLICATAS")
print(f"Número de registros duplicados: {duplicatas.sum()}")

# Remoção de duplicatas
df_limpo = df_limpo.drop_duplicates()
print("\nDUPLICATAS REMOVIDAS")
print(f"Número total de registros após limpeza: {len(df_limpo)}")

# Conversão da coluna DATA para datetime
print("\nCONVERSÃO DA COLUNA DATA")

df_limpo["DATA"] = pd.to_datetime(
    df_limpo["DATA"],
    format="%d/%m/%Y"
)

print("\nTIPO DA COLUNA DATA APÓS CONVERSÃO:")
print(df_limpo["DATA"].dtype)