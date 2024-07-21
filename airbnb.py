import pandas as pd
import pathlib

caminho_bases = pathlib.Path('base de dados')
base_airbnb = pd.DataFrame()
meses = {'jan' : 1, 'fev' : 2, 'mar' : 3, 'abr' : 4, 'mai' : 5, 'jun' : 6, 'jul' : 7, 'ago' : 8, 'set' : 9, 'out': 10, 'nov' : 11, 'dez' : 12}


for arquivo in caminho_bases.iterdir():
    nome_mes = arquivo.name[:3]
    mes = meses[nome_mes]
    ano = arquivo.name[-8:]
    ano = int(ano.replace('.csv', ''))
    
    df = pd.read_csv(caminho_bases / arquivo.name)
    
    df['ano'] = ano
    df['mes'] = mes

    base_airbnb = base_airbnb._append(df)


