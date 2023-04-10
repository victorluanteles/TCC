from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_service = Service(executable_path=r"C:\Users\victo\OneDrive\Área de Trabalho\Documentos\TCC\chromedriver.exe")
driver =webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.get("https://www.google.com.br/")

