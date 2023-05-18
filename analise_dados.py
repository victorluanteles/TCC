import pandas as pd

# leitura do arquivo Excel
data = pd.read_excel('C:\\Users\\victo\\Documents\\tcc\\vagas_geral_novo.xlsx')

# criação do dataframe
df = pd.DataFrame(data=data)

df['descricao_interna_vaga'] = df['descricao_interna_vaga'].str.upper().str.strip()
df['descricao_interna_vaga'] = df['descricao_interna_vaga'].str.strip()

# resultado1 = df[df['descricao_interna_vaga'].str.contains('ENSINO SUPERIOR | FORMAÇÃO ')][['id_vaga','cargo_vaga', 'descricao_interna_vaga']]
# resultado2 = df[~df['descricao_interna_vaga'].str.contains('ENSINO SUPERIOR | FORMAÇÃO')][['id_vaga', 'descricao_interna_vaga']]
# total1 = resultado1['descricao_interna_vaga'].count()
# total2 = resultado2['descricao_interna_vaga'].count()




#resultado_sem_superior = df[~df['descricao_interna_vaga'].str.contains('ENSINO SUPERIOR|FORMAÇÃO|GRADUAÇÃO')][['id_vaga','cargo_vaga','descricao_interna_vaga']]
#total_resultado_sem_superior = resultado_sem_superior['id_vaga'].count()
resultado_com_superior = df[df['descricao_interna_vaga'].str.contains('COMPETÊNCIAS|HABILIDADES|CONHECIMENTOS') ][['id_vaga','cargo_vaga']]
total_resultado_com_superior = resultado_com_superior['id_vaga'].count()



# gerentes_sem_superior = df[~df['descricao_interna_vaga'].str.contains('ENSINO SUPERIOR|FORMAÇÃO|GRADUAÇÃO') & df['cargo_vaga'].str.contains('GERENTE', case=False)][['id_vaga','cargo_vaga']]
# total_gerentes_sem_superior = gerentes_sem_superior['id_vaga'].count()
#
# gerentes_com_superior = df[(df['descricao_interna_vaga'].str.contains('ENSINO SUPERIOR|FORMAÇÃO|GRADUAÇÃO')) & (~df['descricao_interna_vaga'].str.contains('COMPETÊNCIAS|HABILIDADES|CONHECIMENTO')) & (df['cargo_vaga'].str.contains('GERENTE', case=False))][['id_vaga','cargo_vaga']]
#
# total_gerentes_com_superior = gerentes_com_superior['id_vaga'].count()

# exibição do dataframe
#pd.set_option('display.max_colwidth', None)



# #EXIBIÇÃO GERAL
# print("Profissionais sem superior")
# print(resultado_sem_superior)
# print("Total gerentes sem superior " + str(total_resultado_sem_superior))

# print("Profissionais com superior")
# print(resultado_com_superior)
# print("Total gerentes com superior "  + str(total_resultado_com_superior))


#EXIBIÇÃO GERENTES
#
# print("Somente gerentes sem superior")
# print(gerentes_sem_superior)
# print("Total gerentes sem superior " + str(total_gerentes_sem_superior))

print("Somente gerentes com superior")
print(gerentes_com_superior)
print("Total gerentes com superior "  + str(total_gerentes_com_superior))




# # exportacao para excek
# datatoexcel = pd.ExcelWriter('analise_contains.xlsx')
# resultado_sem_superior.to_excel(datatoexcel)
# datatoexcel.close()
# print('export ok')
