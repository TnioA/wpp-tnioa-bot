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
		#self.driver = webdriver.Edge(executable_path='driver\MicrosoftWebDriver') # - se for microsoft edge
		self.driver = webdriver.Chrome(executable_path='driver/chromedriver') # se for chrome
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

		mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
		mensagemBox.send_keys(texto)
		time.sleep(2)

		enviar = self.driver.find_element_by_class_name('_35EW6')
		enviar.click()
		time.sleep(1)

	def message_loop(self):

		contactBox = self.driver.find_elements_by_class_name('_2wP_Y')
		data = []
		try:
			if(self.driver.find_element_by_class_name('OUeyt')):
				escolha_contato = self.driver.find_element_by_class_name('OUeyt')
				escolha_contato.click()
				time.sleep(2)
				chatid = self.driver.find_element_by_class_name('_3XrHh').find_element_by_class_name('_1wjpf').text
				
				post = self.driver.find_elements_by_class_name('_3_7SH')
				ultimo_post = len(post) - 1
				try:
					time.sleep(2)
					hora = post[ultimo_post].find_element_by_class_name('_3EFt_').text
					texto = post[ultimo_post].find_element_by_class_name('selectable-text').text
					data.append({'chatid': chatid,
								'text': texto,
								'time': hora})

					#print(data)
					return jsonify(data)
				except:
					pass
				
		except:
			pass



		

		