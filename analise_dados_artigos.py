import pandas as pd
import re
import numpy as np
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
data = pd.read_excel('C:\\Users\\victo\\Documents\\tcc\\vagas_geral_novo.xlsx')
df_com_art = pd.DataFrame(frases, columns=['Frase'])
df_vagas_site = pd.DataFrame(data=data)

df_vagas_site['descricao_interna_vaga'] = df_vagas_site['descricao_interna_vaga'].str.upper().str.strip()

df_com_art['Frase'] = df_com_art['Frase'].str.upper().str.strip()

df_vagas_site['Frase_Encontrada'] = df_vagas_site['descricao_interna_vaga'].str.contains('|'.join(df_com_art['Frase']))


#
# def remover_conjuncoes(frase):
#     frase_sem_conjuncoes = re.sub(r'\b(a|com|como|da|das|de|do|dos|e|em|nas|no|os|ou|para|quanto|sobre|tanto|às)\b', '',frase)
#     return frase_sem_conjuncoes
#
# df['Frase_sem_conjuncoes'] = df['Frase'].apply(remover_conjuncoes)
#
contagem = df_vagas_site['Frase_Encontrada'].value_counts()

print("Quantidade True:", contagem[True])
print("Quantidade False:", contagem[False])


df_vagas_site['TESTE'] = ''

for frase in df_com_art['Frase']:
    mask = df_vagas_site['descricao_interna_vaga'].str.contains(frase)
    df_vagas_site.loc[mask, 'TESTE'] = frase

print(df_vagas_site)

# # # exportacao para excel
datatoexcel = pd.ExcelWriter('analise_sem_conjun.xlsx')
df_vagas_site.to_excel(datatoexcel)
datatoexcel.close()
print('export ok')
