import pandas as pd
import re
frases = [
    "Conhecimento em abordagens de engenharia de software",
    "Controle de demandas de TIC",
    "Gerenciamento de requisitos",
    "Visão focada tanto em aspectos gerenciais quanto tecnológicos",
    "Alinhar os planos de TI com o planejamento estratégico da empresa",
    "Conhecer a cultura organizacional",
    "Ser capaz de adaptar práticas e aprendizados às necessidades do mercado",
    "Habilidades comportamentais essenciais, como valores para o processo de tomada de decisão",
    "Capacidade de liderar projetos",
    "Flexibilidade",
    "Competências funcionais",
    "Competências comportamentais",
    "Competências do nível do indivíduo",
    "Competências sobre processos",
    "Competências de serviço",
    "Competências sociais",
    "Competências soft skills",
    "Competências hard skills",
    "Competências humanas",
    "Escuta efetiva",
    "Explicações e perguntas produtivas",
    "Compromissos",
    "Conflito e julgamento",
    "Implementação de práticas de governança de TI",
    "Comunicação efetiva",
    "Alinhamento estratégico",
    "Mensuração do desempenho da TI",
    "Prevenção de riscos",
    "Criatividade",
    "Inovação",
    "Autoconfiança",
    "Resolução de conflitos de interesses",
    "Foco em resultados",
    "Administração de prioridades",
    "Flexibilidade",
    "Visão de negócio",
    "Liderança",
    "Relacionamento",
    "Conhecimento Técnico",
    "Autoridade formal",
    "Comprometimento profissional",
    "Habilidade em delegar autoridade",
    "Habilidade em realizar trocas compensatórias",
    "Habilidade em coordenação",
    "Percepção de seu papel e de suas responsabilidades",
    "Administrativa",
    "Comprometimento",
    "Relacionamento",
    "Conceituais",
    "Estratégica",
    "Gerenciamento de informações",
    "Identificação de informações relevantes para a organização",
    "A competência de impulsionar inovações",
    "Acompanhamento de mudanças no mercado",
    "Acompanhamento em mudanças nas demandas de clientes",
    "Antecipação de problemas com fornecedores e parceiros",
    "Identificação das necessidades de informação dos funcionários",
    "Filtragem da informação para evitar sobrecarga",
    "Seleção das melhores fontes internas e externas de informação"
]
data = pd.read_excel('C:\\Users\\victo\\Documents\\tcc\\excel\\import\\vagas_geral_novo.xlsx')
#criação do dataframe
df_art = pd.DataFrame(frases, columns=['Frase'])
df = pd.DataFrame(data=data)
# tratativa do case-sensitive
df['descricao_interna_vaga'] = df['descricao_interna_vaga'].str.upper().str.strip()
df['cargo_vaga'] = df['cargo_vaga'].str.upper().str.strip()
df_art['Frase'] = df_art['Frase'].str.upper().str.strip()
# identificação das competências
df['Frase_Encontrada'] = df['descricao_interna_vaga'].str.contains('|'.join(df_art['Frase']))

# contagem = df['Frase_Encontrada'].value_counts()
# print("Quantidade True:", contagem[True])
# print("Quantidade False:", contagem[False])


df['Comepetencia_artigo'] = ''

for frase in df_art['Frase']:
    mask = df['descricao_interna_vaga'].str.contains(frase)
    df.loc[mask, 'Comepetencia_artigo'] = frase

df = df.drop('Unnamed: 0', axis=1)



print(df)
print(df['descricao_interna_vaga'].str.contains('ENSINO SUPERIOR | FORMAÇÃO '))

# # # exportacao para excel
datatoexcel = pd.ExcelWriter('analise_sem_conjun.xlsx')
df.to_excel(datatoexcel)
datatoexcel.close()
print('export ok')

df_filtrado = df[(df['Comepetencia_artigo']!= '')]

datatoexcel = pd.ExcelWriter('analise_competencias.xlsx')
df_filtrado.to_excel(datatoexcel, index=False)
datatoexcel.close()



# def remover_conjuncoes(frase):
#     frase_sem_conjuncoes = re.sub(r'\b(A|COM|COMO|DA|DAS|DE|DO|DOS|E|EM|NAS|NO|OS|OU|PARA|QUANTO|SOBRE|TANTO|ÀS)\b', '',frase)
#     return frase_sem_conjuncoes
# df_art['Frase_sem_conjuncoes'] = df_art['Frase'].apply(remover_conjuncoes)
# pd.set_option('display.max_colwidth', None)
# print(df_art[['Frase_sem_conjuncoes','Frase']])
