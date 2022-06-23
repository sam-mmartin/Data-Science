import pandas as pd
import matplotlib.pyplot as plt

notas = pd.read_csv("Data/ratings.csv")
print(notas.head())  # retorna as 5 primeiras linhas
print(notas.shape)

notas.columns = ["usuarioId", "filmeId", "nota",
                 "momento"]  # altera a descrição das colunas
print(notas.head())

print(notas['nota'])
# retorna os elementos unicos em uma sequencia - similar ao Distinct()
print(notas['nota'].unique())
# retorna a frequencia de cada elemento da serie
print(notas['nota'].value_counts())
print(notas['nota'].mean())  # retorna a media dos elementos da serie

plt.plot(notas.nota)
plt.show()
