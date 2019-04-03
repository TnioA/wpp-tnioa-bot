# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import content
import os, re, time, json


class Botzap:

	def __init__(self, nome):
		
		print('Bot Iniciado')
		#self.driver = webdriver.Edge(executable_path='driver/windows/MicrosoftWebDriver') # - se for microsoft edge
		self.driver = webdriver.Chrome(executable_path='driver/mac/chromedriver') # se for chrome
		#self.driver = webdriver.Firefox(executable_path='driver/mac/geckodriver') # se for firefox
		
		self.driver.get('https://web.whatsapp.com/source=&data=#')
		actions = ActionChains(self.driver)

		time.sleep(5)

		try:
			#----- MENSAGEM DE ATIVO----------#

			pesquisaBox = self.driver.find_element_by_class_name('jN-F5')
			pesquisaBox.send_keys(nome)
			time.sleep(2)
			contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome))
			contato.click()
			time.sleep(1)

			#PRIMEIRA MENSAGEM
			mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
			mensagemBox.click()
			actions.send_keys('Estou ativo:')
			actions.key_down(Keys.SHIFT)
			actions.send_keys(Keys.ENTER)
			actions.key_up(Keys.SHIFT)
			actions.send_keys("Ativo desde agora")
			actions.perform()
			actions.reset_actions()
			time.sleep(1)
			enviar = self.driver.find_element_by_class_name('_35EW6')
			enviar.click()
			time.sleep(1)

			# SEGUNDA MENSAGEM
			mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
			mensagemBox.click()
			actions.send_keys('Nossa conversa ainda nao acabou:')
			actions.key_down(Keys.SHIFT)
			actions.send_keys(Keys.ENTER)
			actions.key_up(Keys.SHIFT)
			actions.send_keys("Fale comigo a hora que quiser ok")
			actions.perform()
			actions.reset_actions()
			time.sleep(1)
			enviar = self.driver.find_element_by_class_name('_35EW6')
			enviar.click()
			time.sleep(1)
			
		except Exception as e:
			print("Aguardando leitura do QR-Code")

		
	def sendMessage(self, comando):
		actions = ActionChains(self.driver)
		#mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
		#mensagemBox.send_keys(texto)
		#time.sleep(2)

		#botaoEnviar = self.driver.find_element_by_class_name('_35EW6')
		#enviar.click()
		#time.sleep(1)
		if(comando == 'ola'):
			mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
			mensagemBox.click()
			actions.send_keys('Oi eu sou o bot do Tanio responda com /comandos para receber a lista de comandos e conseguir se comunicar comigo')
			actions.perform()
			actions.reset_actions()
			botaoEnviar = self.driver.find_element_by_class_name('_35EW6')
			botaoEnviar.click()

		elif(comando == 'filmes'):
			mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
			mensagemBox.click()
			conteudo = content.getmovies()
			
			mensagemBox.click()
			actions.send_keys("*Filmes em Cartaz*")
			actions.key_down(Keys.SHIFT)
			actions.send_keys(Keys.ENTER)
			actions.send_keys(Keys.ENTER)
			actions.key_up(Keys.SHIFT)
			actions.perform()
			actions.reset_actions()

			for cont in conteudo['filmes']:
				actions.send_keys('Titulo: ' + cont['nome'])
				actions.key_down(Keys.SHIFT)
				actions.send_keys(Keys.ENTER)
				actions.key_up(Keys.SHIFT)
				actions.send_keys('Estreado em: ' + cont['data'])
				actions.key_down(Keys.SHIFT)
				actions.send_keys(Keys.ENTER)
				actions.send_keys(Keys.ENTER)
				actions.key_up(Keys.SHIFT)
				actions.perform()
				actions.reset_actions()

			botaoEnviar = self.driver.find_element_by_class_name('_35EW6')
			botaoEnviar.click()

		elif(comando == 'tabela'):
			mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
			mensagemBox.click()
			conteudo = content.gettabela()

			mensagemBox.click()
			actions.send_keys("*Tabela Brasileirão*")
			actions.key_down(Keys.SHIFT)
			actions.send_keys(Keys.ENTER)
			actions.send_keys(Keys.ENTER)
			actions.key_up(Keys.SHIFT)
			actions.perform()
			actions.reset_actions()

			for cont in conteudo['tabela']:
				actions.send_keys(cont['posicao'] + ' - ' + cont['time'])
				actions.key_down(Keys.SHIFT)
				actions.send_keys(Keys.ENTER)
				actions.key_up(Keys.SHIFT)
				actions.perform()
				actions.reset_actions()

			botaoEnviar = self.driver.find_element_by_class_name('_35EW6')
			botaoEnviar.click()

		elif(comando == 'jogos'):
			mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
			mensagemBox.click()
			conteudo = content.getjogos()

			mensagemBox.click()
			actions.send_keys('*Jogos da ' + conteudo['rodada'] + '*')
			actions.key_down(Keys.SHIFT)
			actions.send_keys(Keys.ENTER)
			actions.send_keys(Keys.ENTER)
			actions.key_up(Keys.SHIFT)
			actions.perform()
			actions.reset_actions()

			for cont in conteudo['jogos']:
				actions.send_keys(cont['jogo'])
				actions.key_down(Keys.SHIFT)
				actions.send_keys(Keys.ENTER)
				actions.key_up(Keys.SHIFT)
				actions.send_keys(cont['sigla_time_casa'] + ' __ X __ ' + cont['sigla_time_fora'])
				actions.key_down(Keys.SHIFT)
				actions.send_keys(Keys.ENTER)
				actions.send_keys(Keys.ENTER)
				actions.key_up(Keys.SHIFT)
				actions.perform()
				actions.reset_actions()

			botaoEnviar = self.driver.find_element_by_class_name('_35EW6')
			botaoEnviar.click()

		elif(comando == 'noticias'):
			mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
			mensagemBox.click()
			conteudo = content.getnews()

			mensagemBox.click()
			actions.send_keys("*Últimas Notícias*")
			actions.key_down(Keys.SHIFT)
			actions.send_keys(Keys.ENTER)
			actions.send_keys(Keys.ENTER)
			actions.key_up(Keys.SHIFT)
			actions.perform()
			actions.reset_actions()
			c = 1
			for cont in conteudo['articles']:
				actions.send_keys('Noticia {}: '.format(c) + cont['title'])
				actions.key_down(Keys.SHIFT)
				actions.send_keys(Keys.ENTER)
				actions.send_keys(Keys.ENTER)
				actions.key_up(Keys.SHIFT)
				actions.perform()
				actions.reset_actions()
				c = int(c) + 1

			botaoEnviar = self.driver.find_element_by_class_name('_35EW6')
			botaoEnviar.click()

		elif(comando == 'moedas'):
			mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
			mensagemBox.click()
			conteudo = content.getmoedas()

			mensagemBox.click()
			actions.send_keys("*Cotação Diária*")
			actions.key_down(Keys.SHIFT)
			actions.send_keys(Keys.ENTER)
			actions.send_keys(Keys.ENTER)
			actions.key_up(Keys.SHIFT)
			actions.perform()
			actions.reset_actions()
			for cont in conteudo['moedas']:
				actions.send_keys(cont['nome'] + ': ' + cont['valor'])
				actions.key_down(Keys.SHIFT)
				actions.send_keys(Keys.ENTER)
				actions.key_up(Keys.SHIFT)
				actions.perform()
				actions.reset_actions()

			botaoEnviar = self.driver.find_element_by_class_name('_35EW6')
			botaoEnviar.click()


		elif(comando == 'comandos'):
			mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
			mensagemBox.click()
			actions.send_keys("*Lista Comandos*")
			actions.key_down(Keys.SHIFT)
			actions.send_keys(Keys.ENTER)
			actions.send_keys(Keys.ENTER)
			actions.key_up(Keys.SHIFT)
			actions.send_keys('/oibot = Para me chamar')
			actions.key_down(Keys.SHIFT)
			actions.send_keys(Keys.ENTER)
			actions.key_up(Keys.SHIFT)
			actions.send_keys('/noticias = Para receber algumas noticias')
			actions.key_down(Keys.SHIFT)
			actions.send_keys(Keys.ENTER)
			actions.key_up(Keys.SHIFT)
			actions.send_keys('/moedas = Para receber a cotação atual das principais moedas')
			actions.key_down(Keys.SHIFT)
			actions.send_keys(Keys.ENTER)
			actions.key_up(Keys.SHIFT)
			actions.send_keys('/tabela = Para receber a tabela do Brasileirao Serie A')
			actions.key_down(Keys.SHIFT)
			actions.send_keys(Keys.ENTER)
			actions.key_up(Keys.SHIFT)
			actions.send_keys('/jogos = Para receber os jogos da rodada atual do Brasileirao Serie A')
			actions.key_down(Keys.SHIFT)
			actions.send_keys(Keys.ENTER)
			actions.key_up(Keys.SHIFT)
			actions.send_keys('/filmes = Para receber os filmes que estao em cartaz')
			actions.key_down(Keys.SHIFT)
			actions.send_keys(Keys.ENTER)
			actions.key_up(Keys.SHIFT)
			actions.send_keys('/comandos = Para receber uma lista de comandos')
			actions.perform()
			actions.reset_actions()
			botaoEnviar = self.driver.find_element_by_class_name('_35EW6')
			botaoEnviar.click()


	def message_loop(self):
		data = {'chatid': '', 'text': '', 'time': ''}
		contactBox = self.driver.find_elements_by_class_name('_2wP_Y')
		try:
			if(self.driver.find_element_by_class_name('_298R6')):
				droppage = self.driver.find_element_by_class_name('_298R6')
				droppage.click()
		except:
			pass
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
					data = {'chatid': str(chatid),
						    'text': str(texto),
						    'time': str(hora)}
					return data

				except:
					print('Não consegui trazer a informações da msg.')
					return data		
		except:
			#print('Sem últimas conversas...')
			return data