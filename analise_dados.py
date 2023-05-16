import pandas as pd

# leitura do arquivo Excel
data = pd.read_excel('C:\\Users\\victo\\Documents\\tcc\\vagas_geral_novo.xlsx')

# criação do dataframe
df = pd.DataFrame(data=data)

df['detalhes_vaga'] = df['detalhes_vaga'].str.upper().str.strip()
df['detalhes_vaga'] = df['detalhes_vaga'].str.strip()
resultado1 = df[df['detalhes_vaga'].str.contains('ENSINO SUPERIOR|FORMAÇÃO')][['cargo_vaga', 'detalhes_vaga']]

resultado2 = df[~df['detalhes_vaga'].str.contains('ENSINO SUPERIOR|FORMAÇÃO')][['cargo_vaga', 'detalhes_vaga']]

total1 = resultado1['detalhes_vaga'].count()
total2 = resultado2['detalhes_vaga'].count()
# exibição do dataframe
pd.set_option('display.max_colwidth', None)

print("Resultado que contém")
print(resultado1)
print("Total " + str(total1))
print("Resultado que não contém")
print(resultado2)
print("Total " + str(total2))

# exportacao para excek
# datatoexcel = pd.ExcelWriter('analise_contains.xlsx')
# resultado1.to_excel(datatoexcel)
# datatoexcel.close()
# print('export ok')