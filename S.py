from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import datetime
import requests
import pandas as pd
from bs4 import BeautifulSoup


# Inicializar o driver do Chrome
driver_service = Service(executable_path=r"C:\Users\victo\OneDrive\Área de Trabalho\Documentos\TCC\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

# Carregar a página de vagas
driver.get("https://www.vagas.com.br/vagas-de-?a%5B%5D=24")

# Clicar no botão "mostrar mais" até que não haja mais botões para clicar
while True:
    agora = datetime.datetime.now()
    hora_formatada = agora.strftime("%H:%M:%S")
    try:
        # Encontrar o botão "mostrar mais" na página usando o XPath e clique nele
        driver.execute_script("arguments[0].click();", driver.find_element("xpath",'//*[@id="maisVagas"]'))
        time.sleep(6)
        print("clicando em botao " + str(hora_formatada))
    except:
        # Se o botão "mostrar mais" não puder mais ser encontrado, saia do loop
        break
        print("nao achou botao")

# Depois de clicar em todos os botões "mostrar mais", obtenha o HTML da página
html = driver.page_source

# Use o BeautifulSoup para analisar o HTML e encontrar as vagas
soup = BeautifulSoup(html, 'html.parser')
vagas = soup.find_all('li', {'class': 'vaga'})
contador = 0
# Imprima as vagas encontradas
export_data =[]
print("entrou loop")
for vaga in vagas:
    vaga_info = {}
    vaga_info['href'] = 'https://www.vagas.com.br' + vaga.find('a', class_='link-detalhes-vaga').get('href')
    vaga_info['id_vaga'] = vaga.find('a', class_='link-detalhes-vaga').get('id')
    vaga_info['cargo_vaga'] = vaga.find('a', class_='link-detalhes-vaga').get_text().strip()
    vaga_info['detalhes_vaga'] = vaga.find('div', class_='detalhes').get_text().strip()
    detalhes_url = 'https://www.vagas.com.br' + vaga.find('a', class_='link-detalhes-vaga').get('href')
    detalhes_response = requests.get(detalhes_url)
    detalhes_html = detalhes_response.content
    detalhes_soup = BeautifulSoup(detalhes_html, 'html.parser')
    elemento = detalhes_soup.find('div', class_='job-tab-content job-description__text texto')
    if elemento is not None:
        vaga_info['descricao_interna_vaga'] = elemento.get_text()
    else:
        vaga_info['descricao_interna_vaga'] = ''
    export_data.append(vaga_info)
    contador = contador + 1
    print("Exe: "+ str(contador))
    print(vaga_info['cargo_vaga'])
    print(elemento)

print(export_data)
data = export_data
df = pd.DataFrame(data=data)
datatoexcel = pd.ExcelWriter('vagas_geral_novo.xlsx')
df.to_excel(datatoexcel)
datatoexcel.close()
print('export ok')

# Fechar o navegador
driver.quit()
