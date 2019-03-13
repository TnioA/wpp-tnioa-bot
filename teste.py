from selenium import webdriver
import time
import os


driver = webdriver.Chrome(executable_path='driver/chromedriver')

#driver = webdriver.Edge(executable_path='\..') - se for microsoft edge
#driver = webdriver.Firefox(executable_path='\..') se for firefox

driver.get('http://web.whatsapp.com')
time.sleep(5)

nome = 'Samuel'

mensagem = 'bot:: Mensagem de teste enviada pelo bot de whatsapp do Tanio'

caixa_de_pesquisa = driver.find_element_by_class_name('jN-F5')
caixa_de_pesquisa.send_keys(nome)

time.sleep(5)

contato = driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome))
contato.click()

time.sleep(2)

caixa_de_mensagem = driver.find_element_by_class_name('_2S1VP')
caixa_de_mensagem.send_keys(mensagem)

time.sleep(2)

botao_enviar = driver.find_element_by_class_name('_35EW6')
botao_enviar.click()

botao_limpar_pesquisa = driver.find_element_by_class_name('_3Burg')
botao_limpar_pesquisa.click()