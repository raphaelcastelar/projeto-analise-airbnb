import pandas as pd
import pathlib

caminho_bases = pathlib.Path('base de dados')
base_airbnb = pd.DataFrame()

for arquivo in caminho_bases.iterdir():
    df = pd.read_csv(r'base de dados\{}'.format(arquivo.name))
    base_airbnb = base_airbnb._append(df)


