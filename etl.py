import pandas as pd
import os
import glob

# Ler um arquivo

def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:

    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)

    return df_total

# Adicionar o kpi

def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:

    df['Total'] = df['Quantidade'] * df['Venda']

    return df

# Load dos meus arquivos em csv ou parquet

def carregar_dados(df: pd.DataFrame, fomarto_saida: list):
    for formato in fomarto_saida:
        if formato == 'csv':
            df.to_csv('dados.csv',index= False)
        if formato == 'parquet':
            df.to_csv('dados.parquet',index= False)

def pipeline(pasta: str, formato_saida: list):

    df_consolidado = extrair_dados_e_consolidar(pasta)
    df_consolidado_com_kpi = calcular_kpi_de_total_de_vendas(df_consolidado)

    carregar_dados(df_consolidado_com_kpi, formato_saida)