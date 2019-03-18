# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os
import re
import time
import requests
import json


class Botzap:

	def __init__(self, nome):
		
		print('Bot Iniciado')
		self.driver = webdriver.Edge(executable_path='driver\MicrosoftWebDriver') # - se for microsoft edge
		#self.driver = webdriver.Chrome(executable_path='driver/chromedriver') # se for chrome
		#self.driver = webdriver.Firefox(executable_path='driver/geckodriver') # se for firefox
		self.driver.get('https://web.whatsapp.com/source=&data=#')
		time.sleep(5)
		
		#pesquisaBox = self.driver.find_element_by_class_name('jN-F5')
		#pesquisaBox.send_keys(nome)
		#time.sleep(2)
		#contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome))
		#contato.click()
		#time.sleep(1)
		#mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
		#mensagemBox.send_keys('Estou ativo')
		#time.sleep(1)
		#enviar = self.driver.find_element_by_class_name('_35EW6')
		#enviar.click()
		#time.sleep(1)

	def sendMessage(self, texto):
		#print('Comando enviar mensagem')

		mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
		mensagemBox.send_keys(texto)
		time.sleep(2)

		enviar = self.driver.find_element_by_class_name('_35EW6')
		enviar.click()
		time.sleep(1)

	def message_loop(self):
		#print('Comando escutar iniciado')
		#print('Buscar ultima conversa')
		contato = self.driver.find_element_by_class_name('_2wP_Y')
		chatid = self.driver.find_element_by_class_name('_1wjpf').text
		contato.click()
		time.sleep(1)
		post = self.driver.find_elements_by_class_name('_3_7SH')
		ultimo_post = len(post) - 1
		try:
			time.sleep(2)
			texto = post[ultimo_post].find_element_by_class_name('selectable-text').text
		except:
			pass
		conteudo = {chatid, texto}
		boxbotao_apagar = self.driver.find_element_by_class_name('rAUz7 _3TbsN')
		#ultimo_botao = len(boxbotao_apagar) - 1
		#botao_apagar = ultimo_botao.find_element_by_class_name('')
		boxbotao_apagar.click()

		return(conteudo)




		