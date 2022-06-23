import pandas as pd

notas = pd.read_csv("Data/ratings.csv")
print(notas.head())  # retorna as 5 primeiras linhas
print(notas.shape)

notas.columns = ["usuarioId", "filmeId", "nota",
                 "momento"]  # altera a descrição das colunas
print(notas.head())

print(notas['nota'])
# retorna os elementos unicos em uma sequencia - similar ao Distinct()
print(notas['nota'].unique())
