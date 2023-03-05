import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.vagas.com.br/vagas-de-tecnologia-informa%C3%A7%C3%A3o'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
placas = soup.find_all('li', class_='vaga odd')
#descvaga = post.find('div',class_='detalhes').get_text().strip()
#cargo = post.find('a',class_='link-detalhes-vaga').get_text().strip()

placa = placas[0]
teste = placa.find('a', class_='link-detalhes-vaga')

vagas=[]
for vaga in soup.findAll('li', attrs = {'class': 'vaga odd'}):
    vaga_info = {}
    vaga_info['href'] = 'https://www.vagas.com.br'+vaga.find('a', class_='link-detalhes-vaga').get('href')
    vaga_info['id_vaga']= vaga.find('a', class_='link-detalhes-vaga').get('id')
    vaga_info['cargo_vaga'] = vaga.find('a', class_='link-detalhes-vaga').get_text().strip()
    vaga_info['detalhes_vaga'] = vaga.find('div',class_='detalhes').get_text().strip()

    url = 'https://www.vagas.com.br' + vaga.find('a', class_='link-detalhes-vaga').get('href')
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    descricaointernavaga = soup.find('div', class_='job-tab-content job-description__text texto').get_text()
    vaga_info['descricao_interna_vaga'] = soup.find('div', class_='job-tab-content job-description__text texto').get_text()
    vagas.append(vaga_info)

print(vagas)


