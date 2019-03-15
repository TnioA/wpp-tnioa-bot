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
		self.driver = webdriver.Chrome(executable_path='driver/chromedriver')
		self.driver.get('https://web.whatsapp.com')
		time.sleep(5)
		#driver = webdriver.Edge(executable_path='\..') - se for microsoft edge
		#driver = webdriver.Firefox(executable_path='\..') se for firefox
		pesquisaBox = self.driver.find_element_by_class_name('jN-F5')
		pesquisaBox.send_keys(nome)
		time.sleep(2)
		contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome))
		contato.click()
		time.sleep(1)
		mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
		mensagemBox.send_keys('Estou ativo')
		time.sleep(1)
		enviar = self.driver.find_element_by_class_name('_35EW6')
		enviar.click()
		time.sleep(1)

	def write(self, texto):
		#print('Comando enviar mensagem')

		mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
		mensagemBox.send_keys(texto)
		time.sleep(2)

		enviar = self.driver.find_element_by_class_name('_35EW6')
		enviar.click()
		time.sleep(1)

	def monitor(self):
		#print('Comando escutar iniciado')
		#print('Buscar ultima conversa')
		post = self.driver.find_elements_by_class_name('_3_7SH')
		ultimo = len(post) - 1
		try:
			texto = post[ultimo].find_element_by_class_name('selectable-text').text
			if texto[:1] == '/':
				return(texto)
		except:
			pass



