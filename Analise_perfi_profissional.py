import pandas as pd
frases = [
    "Graduação",
    "Ensino superior",
    "Superior completo"
    "Base em Tecnologia da Informação",
    "Experiência profissional de 10 a 15 anos",
    "Experiência",analise_competencias
    "Pós graduação",
    "Especialização",
    "Mestrado",
    "Diversos setores",
    "Experiência em diferentes segmentos",
    "Multissetorial",
    "Experiência em cargos de liderança",
    "Experiência em gerência ou coordenação",
    "Experiência relevante na área",
    "Curso técnico"
]
#data = pd.read_excel('C:\\Users\\victo\\Documents\\tcc\\analise_competencias.xlsx')
data = pd.read_excel('C:\\Users\\victo\\Documents\\tcc\\excel\\import\\vagas_geral_novo.xlsx')
#criação do dataframe
df_art = pd.DataFrame(frases, columns=['Frase'])
df = pd.DataFrame(data=data)
# tratativa do case-sensitive
df['descricao_interna_vaga'] = df['descricao_interna_vaga'].str.upper().str.strip()
df_art['Frase'] = df_art['Frase'].str.upper().str.strip()
# identificação das competências
df['Frase_Encontrada'] = df['descricao_interna_vaga'].str.contains('|'.join(df_art['Frase']))

# contagem = df['Frase_Encontrada'].value_counts()
# print("Quantidade True:", contagem[True])
# print("Quantidade False:", contagem[False])

df['carac_prof_artigo'] = ''

for frase in df_art['Frase']:
    mask = df['descricao_interna_vaga'].str.contains(frase)
    df.loc[mask, 'carac_prof_artigo'] = frase

# # # exportacao para excel

datatoexcel = pd.ExcelWriter('excel\\analise_perfil_profissional.xlsx')
df.to_excel(datatoexcel, index=False)
datatoexcel.close()
print('export ok')

