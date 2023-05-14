from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
driver_service = Service(executable_path=r"C:\Users\victo\OneDrive\Área de Trabalho\Documentos\TCC\chromedriver.exe")
driver =webdriver.Chrome(service=driver_service)
driver.get("https://www.vagas.com.br/vagas-de-tecnologia-da-informacao?ordenar_por=mais_recentes")

while True:
    try:
        # Encontre o botão "mostrar mais" na página usando o XPath e clique nele
        driver.find_element("xpath",'//*[@id="maisVagas"]').click()

        # Aguarde a página ser carregada
        time.sleep(10)

    except:
        # Se o botão "mostrar mais" não puder mais ser encontrado, saia do loop
        print("não achou o botao")
        break

# Depois de clicar em todos os botões "mostrar mais", obtenha o HTML da página
html = driver.page_source

# Use o BeautifulSoup para analisar o HTML e encontrar as vagas
soup = BeautifulSoup(html, 'html.parser')
vagas = soup.find_all('li', {'class': 'vaga'})

# Imprima as vagas encontradas
export_data =[]
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
    vaga_info['descricao_interna_vaga'] = detalhes_soup.find('div', class_='job-tab-content job-description__text texto').get_text()
    export_data.append(vaga_info)

print(export_data)
data = export_data
df = pd.DataFrame(data=data)
datatoexcel = pd.ExcelWriter('vagas_geral.xlsx')
df.to_excel(datatoexcel)
datatoexcel.close()
print('export ok')