from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from time import sleep
import pickle

driver =  webdriver.Firefox()
driver.maximize_window()
pages =open('pages.txt', 'r')
page= int(pages.readline())
pages.close()
url="https://www.linkedin.com/search/results/people/?geoUrn=%5B%22106104855%22%5D&keywords=front%20end&origin=FACETED_SEARCH&page="
driver.get(url+str(page))
sleep(5)
login=  driver.find_element(By.XPATH, "/html/body/div[1]/main/div/p/a")
login.click()
sleep(5)
email = driver.find_element("id", "username")
email.send_keys("") #Preencher Email
email.submit()
password = driver.find_element("id", "password")
password.send_keys("") #Preencher Senha
password.submit()
btnEntrar = driver.find_element(By.XPATH,"/html/body/div/main/div[2]/div[1]/form/div[3]/button")
btnEntrar.click()
sleep(5)
conexoes=0
while conexoes!=100: #Quantidade de conexões
    count = len(driver.find_elements(By.XPATH, '//button//span[contains(., "Conectar")]'))
    if count>0:
        for i in range(1, count+1):
            conectar = driver.find_element(By.XPATH, '//button//span[contains(., "Conectar")]')
            try:
                conectar.click()
                sleep(2)
                conexoes=conexoes + 1
                print('Conexões:' + str(conexoes))
            except:
                conexoes = conexoes - 1
                driver.find_element(By.XPATH, "//button[@aria-label='Fechar']").click()
                sleep(1)
                driver.execute_script("arguments[0].innerText = 'pular'", conectar)
            mensagem = driver.find_element(By.XPATH, '//button//span[contains(., "Enviar sem nota")]')
            try:
                mensagem.click()
                sleep(120)
            except:
                driver.find_element(By.XPATH, "//button[@aria-label='Fechar']").click()
                sleep(1)
                driver.execute_script("arguments[0].innerText = 'pular'", conectar)
    page=page+1
    print('Pagina:'+str(page))
    with open('pages.txt','w') as pages:
        pages.write(str(page))
    driver.get(url+str(page))
    sleep(5)