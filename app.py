# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os
import re
import time
import requests
import json


# API NOTICIAS

# 'https://newsapi.org/v2/top-headlines?sources=globo&pageSize=5&apiKey=f6fdb7cb0f2a497d92dbe719a29b197f'


class Botzap:

	def __init__(self, nome):
		
		print('Bot Iniciado')
		self.driver = webdriver.Chrome(executable_path='driver/chromedriver')
		self.driver.get('https://web.whatsapp.com')
		time.sleep(5)
		#driver = webdriver.Edge(executable_path='\..') - se for microsoft edge
		#driver = webdriver.Firefox(executable_path='\..') se for firefox


	def send(self, nome_contato, texto):
		print('Comando enviar mensagem')

		pesquisaBox = self.driver.find_element_by_class_name('jN-F5')
		pesquisaBox.send_keys(nome_contato)
		time.sleep(5)

		contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome_contato))
		contato.click()
		time.sleep(2)

		mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
		mensagemBox.send_keys(texto)
		time.sleep(2)

		enviar = self.driver.find_element_by_class_name('_35EW6')
		enviar.click()

		limpar_pesquisa = self.driver.find_element_by_class_name('C28xL')
		limpar_pesquisa.click()
		limpar_pesquisa.click()


	def read(self):
		print('Comando escutar iniciado')
		print('Buscar ultima conversa')
		for conversa in self.driver.find_elements_by_class_name('_3j7s9'):
			conversa.click()
			time.sleep(2)
			post = self.driver.find_elements_by_class_name('_3_7SH')
			ultimo = len(post) - 1
			try:
				texto = post[ultimo].find_element_by_class_name('selectable-text').text.strip()
				print(texto)
			except:
				print('Texto Não encontrado')

	def answer(self, texto):
		print('Comando responder mensagem')
		
		response = str(texto)
		response = 'bot: ' + response

		mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
		mensagemBox.send_keys(response)
		time.sleep(2)

		enviar = self.driver.find_element_by_class_name('_35EW6')
		enviar.click()

		#main > div._3zJZ2 > div > div > div._9tCEa > div:nth-child(27) > div > div > div.copyable-text > div > span