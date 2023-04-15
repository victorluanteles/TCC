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
        time.sleep(5)

    except:
        # Se o botão "mostrar mais" não puder mais ser encontrado, saia do loop
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
    #receber no url para acessar descricao interna
    url = 'https://www.vagas.com.br' + vaga.find('a', class_='link-detalhes-vaga').get('href')
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    vaga_info['descricao_interna_vaga'] = soup.find('div',class_='job-tab-content job-description__text texto').get_text()
    export_data.append(vaga_info)

print(export_data)

data = export_data
df = pd.DataFrame(data=data)
datatoexcel = pd.ExcelWriter('vagas_geral.xlsx')
df.to_excel(datatoexcel)
datatoexcel.close()
print('DataFrame is written to Excel File successfully.')