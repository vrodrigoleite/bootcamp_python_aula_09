from etl import pipeline   

pasta: str = 'data'
formato_saida: list = ['csv', 'parquet']

pipeline(pasta, formato_saida)