from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
import socket

def element_presence(by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        # conectarse al host: nos dice si el host es en realidad
        # accesible
        socket.create_connection(("www.google.com", 80))
        return True
    except:
        is_connected()

chrome_options = ChromeOptions()
chrome_options.add_extension('D:\Wstp\metamask.crx')

driver = webdriver.Chrome(executable_path="D:\Wstp\chromedriver.exe", options=chrome_options)
driver.get("https://exchange.pancakeswap.finance/#/swap")
#sleep(2)

semilla = open('D:\Wstp\semilla.txt').readline().strip()
contraseña = open('D:\Wstp\contraseña.txt').readline().strip()
nombre_red = "Binance Smart Chain Mainnet"
url = "https://bsc-dataseed1.ninicoin.io"
id_cadena = "56"

driver.switch_to_window(driver.window_handles[-1])
sleep(1)
driver.switch_to_window(driver.window_handles[0])
element_presence(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/button', 2)

comenzar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/button')
comenzar.click()
sleep(2)

importar_billetera = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/button')
importar_billetera.click()
sleep(2)

estoy_de_acuerdo = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/div/div[5]/div[1]/footer/button[2]')
estoy_de_acuerdo.click()
sleep(2)

input_semilla = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/form/div[4]/div[1]/div/input')
input_contraseña = driver.find_element_by_xpath('//*[@id="password"]')
input_re_contraseña = driver.find_element_by_xpath('//*[@id="confirm-password"]')
acepto_tyc = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/form/div[7]/div')
importar = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/form/button')


input_semilla.send_keys(semilla)
input_contraseña.send_keys(contraseña)
input_re_contraseña.send_keys(contraseña)
acepto_tyc.click()
sleep(1)
importar.click()
sleep(1)
todo_listo = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/button')
todo_listo.click()


element_presence(
        By.XPATH, '//*[@id="popover-content"]/div/div/section/header/div/button', 15)
        
driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[2]/div[1]/div').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/li[7]/span').click()
sleep(1)

input_nombre_red = driver.find_element_by_xpath('//*[@id="network-name"]')
input_url = driver.find_element_by_xpath('//*[@id="rpc-url"]')
input_id = driver.find_element_by_xpath('//*[@id="chainId"]')

input_nombre_red.send_keys(nombre_red)
input_url.send_keys(url)
input_id.send_keys(id_cadena)
sleep(1)
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div[2]/div[2]/div/div[2]/div[2]/div[7]/button[2]').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[1]/img[1]').click()
sleep(1)

#driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]').click()
#sleep(1)
#driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
#sleep(1)

# Cambiar de pestaña
driver.switch_to_window(driver.window_handles[-1])
sleep(1)
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/nav/div[2]/div[1]/button').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="wallet-connect-metamask"]/div').click()
sleep(1)

driver.switch_to_window(driver.window_handles[0])
driver.refresh()
#driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[1]/img[1]').click()
#sleep(1)
element_presence(
        By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]', 10)
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
sleep(1)

driver.switch_to_window(driver.window_handles[-1])




#driver.execute_script("window.open('');")



input("Presiona [ENTER] para cerrar el navegador")

driver.quit()