# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import content
import os, re, time, json, csv


class Botzap:

	def __init__(self,nome):
		
		print('Bot Iniciado')
		#self.driver = webdriver.Edge(executable_path='driver/windows/MicrosoftWebDriver') # - se for microsoft edge
		self.driver = webdriver.Chrome(executable_path='driver/windows/chromedriver') # se for chrome
		#self.driver = webdriver.Firefox(executable_path='driver/mac/geckodriver') # se for firefox
		
		self.driver.get('https://web.whatsapp.com/source=&data=#')
		actions = ActionChains(self.driver)
		time.sleep(10)

		#try:
		print(nome)
		print("Enviando mensagem de boas vindas!")
		#----- MENSAGEM DE ATIVO----------#
		pesquisaBox = self.driver.find_element_by_class_name('_2zCfw')
		pesquisaBox.send_keys(nome)
		time.sleep(2)
		contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome))
		contato.click()
		time.sleep(1)

		#PRIMEIRA MENSAGEM
		mensagemBox = self.driver.find_element_by_class_name('_3u328')
		mensagemBox.click()
		actions.send_keys('Estou ativo:')
		actions.key_down(Keys.SHIFT)
		actions.send_keys(Keys.ENTER)
		actions.key_up(Keys.SHIFT)
		actions.send_keys("Ativo desde agora")
		actions.perform()
		actions.reset_actions()
		time.sleep(1)
		enviar = self.driver.find_element_by_class_name('_3M-N-')
		enviar.click()
		time.sleep(1)

		#except Exception as e:
			#print("Nao foi possivel ler o QR-Code!")

		

	def quebra_linha(self, times):
		actions = ActionChains(self.driver)
		if times == 1:
			actions.key_down(Keys.SHIFT)
			actions.send_keys(Keys.ENTER)
			actions.key_up(Keys.SHIFT)
			actions.perform()
			actions.reset_actions()
		if times == 2:
			actions.key_down(Keys.SHIFT)
			actions.send_keys(Keys.ENTER)
			actions.send_keys(Keys.ENTER)
			actions.key_up(Keys.SHIFT)
			actions.perform()
			actions.reset_actions()
			
	def valida_contato(self, contato):
		actions = ActionChains(self.driver)
		senha = '123456'
		contatos_liberados = ['Tanio', '+55 85 98407-3833', 'TanTanio_bot', 'jurema']
		if contato in contatos_liberados:
			print('contato liberado!!!')
			return(True)
		else:
			print('contato nao liberado!')
			mensagemBox = self.driver.find_element_by_class_name('_3u328')
			mensagemBox.click()
			actions.send_keys('*Acesso Negado!*')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(1)
			actions.send_keys('Comando liberado apenas para o Administrador, entre com a senha de administrador para usá-lo:')
			actions.perform()
			actions.reset_actions()
			botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
			botaoEnviar.click()

			#------- aguardando a senha...
			for contagem in range(0,10):
				try:
					#-- pega a ultima mensagem
					post = self.driver.find_elements_by_class_name('_3_7SH')
					ultimo_post = len(post) - 1
					texto = post[ultimo_post].find_element_by_class_name('selectable-text').text
					
					if texto == senha:
						print('liberado por senha')
						mensagemBox.click()
						actions.send_keys('Contato liberado com sucesso!')
						actions.perform()
						actions.reset_actions()
						botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
						botaoEnviar.click()
						return(True)
				except:
					pass
	
				time.sleep(1)

			return(False)
	def sendMessage(self, comando):
		actions = ActionChains(self.driver)
		if(comando == 'ola'):
		    mensagemBox = self.driver.find_element_by_class_name('_3u328')
		    mensagemBox.click()
		    actions.send_keys('Oi eu sou o bot do Tanio responda com /comandos para receber a lista de comandos e conseguir se comunicar comigo')
		    actions.perform()
		    actions.reset_actions()
		    botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
		    botaoEnviar.click()
			
		elif(comando == 'erro'):
			texto = 'Comando desconhecido digite /comandos para receber a lista dos comandos válidos!'
			mensagemBox = self.driver.find_element_by_class_name('_3u328')
			mensagemBox.click()
			actions.send_keys(texto)
			actions.perform()
			actions.reset_actions()
			botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
			botaoEnviar.click()

		elif(comando == 'relatorio'):
		    mensagemBox = self.driver.find_element_by_class_name('_3u328')
		    mensagemBox.click()
		    actions.send_keys('*Comando ainda em manutenção*')
		    actions.perform()
		    actions.reset_actions()
		    '''
		    arquivo = open('C:/VIRTUAL AGE/novoarquivo/relatorio449.csv')
		    linhas = csv.reader(arquivo, delimiter=';')
		    mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
		    mensagemBox.click()
		    actions.send_keys('*449 - RELATORIO DE CLIENTES ATENDIDOS*')
		    actions.perform()
		    actions.reset_actions()
		    self.quebra_linha(2)
		    actions.send_keys('         *Nome*         |         *Telefone*      ')
		    actions.perform()
		    actions.reset_actions()
		    self.quebra_linha(1)
		    for linha in linhas:
		        mensagemBox = self.driver.find_element_by_class_name('_2S1VP')
		        mensagemBox.click()
		        actions.send_keys(linha[3] + ' - ' + linha[8])
		        actions.perform()
		        actions.reset_actions()
		        self.quebra_linha(1)
		    
		    '''    
		    botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
		    botaoEnviar.click()
		    
		elif(comando == 'clima'):
		    mensagemBox = self.driver.find_element_by_class_name('_3u328')
		    mensagemBox.click()
		    conteudo = content.getclima()
		  
		    actions.send_keys('*Clima agora*')
		    actions.perform()
		    actions.reset_actions()
		    self.quebra_linha(1)
		    actions.send_keys('*' + conteudo['name'] + ' ' + conteudo['state'] + '*')
		    actions.perform()
		    actions.reset_actions()
		    self.quebra_linha(1)
		    actions.send_keys(conteudo['data']['condition'])
		    actions.perform()
		    actions.reset_actions()
		    self.quebra_linha(2)
		    actions.send_keys('Temperatura: ' + str(conteudo['data']['temperature']) + '°')
		    actions.perform()
		    actions.reset_actions()
		    self.quebra_linha(1)
		    actions.send_keys('Sensação: ' + str(conteudo['data']['sensation']) + '°')
		    actions.perform()
		    actions.reset_actions()
		    self.quebra_linha(1)
		    actions.send_keys('Umidade: ' + str(conteudo['data']['humidity']) + '°')
		    actions.perform()
		    actions.reset_actions()
		    self.quebra_linha(1)
		    actions.send_keys('Pressão: ' + str(conteudo['data']['pressure']) + 'hPa')
		    actions.perform()
		    actions.reset_actions()
		    self.quebra_linha(1)
		    actions.send_keys('Vento: ' + str(conteudo['data']['wind_velocity']) + 'Km/h')
		    actions.perform()
		    actions.reset_actions()
		    self.quebra_linha(2)
		    actions.send_keys('Atualização: ' + conteudo['data']['date'])
		    actions.perform()
		    actions.reset_actions()
		    self.quebra_linha(1)
		    
		    
		    botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
		    botaoEnviar.click()
		
		elif(comando == 'filmes'):
			mensagemBox = self.driver.find_element_by_class_name('_3u328')
			mensagemBox.click()
			conteudo = content.getmovies()
			
			mensagemBox.click()
			actions.send_keys('*Filmes em Cartaz*')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(2)

			for cont in conteudo['filmes']:
				actions.send_keys('Titulo: ' + cont['nome'])
				actions.perform()
				actions.reset_actions()
				self.quebra_linha(1)
				actions.send_keys('Estreado em: ' + cont['data'])
				actions.perform()
				actions.reset_actions()
				self.quebra_linha(2)

			botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
			botaoEnviar.click()

		elif(comando == 'fofocas'):
			mensagemBox = self.driver.find_element_by_class_name('_3u328')
			mensagemBox.click()
			conteudo = content.getfofocas()
			
			mensagemBox.click()
			actions.send_keys('*Ultimas Fofocas*')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(2)

			for cont in conteudo['ultimas']:
				actions.send_keys('Noticia: ' + cont['conteudo'])
				actions.perform()
				actions.reset_actions()
				self.quebra_linha(1)
				actions.send_keys('Data: ' + cont['data'])
				actions.perform()
				actions.reset_actions()
				self.quebra_linha(2)

			botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
			botaoEnviar.click()

		elif(comando == 'tabela'):
			mensagemBox = self.driver.find_element_by_class_name('_3u328')
			mensagemBox.click()
			conteudo = content.gettabela()

			mensagemBox.click()
			actions.send_keys('*Tabela Brasileirão*')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(2)

			for cont in conteudo['tabela']:
				actions.send_keys(cont['posicao'] + ' - ' + cont['time'] + ' - ' + cont['pontos'])
				actions.perform()
				actions.reset_actions()
				self.quebra_linha(1)

			botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
			botaoEnviar.click()

		elif(comando == 'jogos'):
			mensagemBox = self.driver.find_element_by_class_name('_3u328')
			mensagemBox.click()
			conteudo = content.getjogos()

			mensagemBox.click()
			actions.send_keys('*Jogos da ' + conteudo['rodada'] + '*')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(2)

			for cont in conteudo['jogos']:
				actions.send_keys(cont['jogo'])
				actions.perform()
				actions.reset_actions()
				self.quebra_linha(1)
				actions.send_keys(cont['sigla_time_casa'] + ' ' + cont['placar_time_casa'] + ' X ' + cont['placar_time_fora'] + ' ' + cont['sigla_time_fora'])
				actions.perform()
				actions.reset_actions()
				self.quebra_linha(2)

			botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
			botaoEnviar.click()

		elif(comando == 'noticias'):
			mensagemBox = self.driver.find_element_by_class_name('_3u328')
			mensagemBox.click()
			conteudo = content.getnews()

			mensagemBox.click()
			actions.send_keys('*Últimas Notícias*')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(2)
			c = 1
			for cont in conteudo['articles']:
				actions.send_keys('Noticia {}: '.format(c) + cont['title'])
				actions.perform()
				actions.reset_actions()
				self.quebra_linha(2)
				c = int(c) + 1

			botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
			botaoEnviar.click()

		elif(comando == 'moedas'):
			mensagemBox = self.driver.find_element_by_class_name('_3u328')
			mensagemBox.click()
			conteudo = content.getmoedas()

			mensagemBox.click()
			actions.send_keys('*Cotação Diária*')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(2)
			for cont in conteudo['moedas']:
				actions.send_keys(cont['nome'] + ': ' + cont['valor'])
				actions.perform()
				actions.reset_actions()
				self.quebra_linha(1)

			botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
			botaoEnviar.click()
			
		elif(comando == 'desligaluz'):
			chatid = self.driver.find_element_by_class_name('_3XrHh').find_element_by_class_name('_1wjpf').text
			print('tentando validar usuario: ' + chatid)
			if self.valida_contato(chatid):
				mensagemBox = self.driver.find_element_by_class_name('_3u328')
				mensagemBox.click()
				actions.send_keys('Luz Desligada!')
				actions.perform()
				actions.reset_actions()
				botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
				botaoEnviar.click()
			else:
				mensagemBox = self.driver.find_element_by_class_name('_3u328')
				mensagemBox.click()
				actions.send_keys('Voce não tem acesso para esse comando!')
				actions.perform()
				actions.reset_actions()
				botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
				botaoEnviar.click()
				
				
		elif(comando == 'ligaluz'):
			chatid = self.driver.find_element_by_class_name('_3XrHh').find_element_by_class_name('_1wjpf').text
			print('tentando validar usuario: ' + chatid)
			if self.valida_contato(chatid):
				mensagemBox = self.driver.find_element_by_class_name('_3u328')
				mensagemBox.click()
				actions.send_keys("Luz Ligada!")
				actions.perform()
				actions.reset_actions()
				botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
				botaoEnviar.click()
			else:
				mensagemBox = self.driver.find_element_by_class_name('_3u328')
				mensagemBox.click()
				actions.send_keys('Voce não tem acesso para esse comando!')
				actions.perform()
				actions.reset_actions()
				botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
				botaoEnviar.click()
				

		elif(comando == 'comandos'):
			mensagemBox = self.driver.find_element_by_class_name('_3u328')
			mensagemBox.click()
			actions.send_keys('*Lista Comandos*')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(2)
			actions.send_keys('/oibot = Para me chamar')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(1)
			actions.send_keys('/clima = Para receber as informações do clima agora')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(1)
			actions.send_keys('/noticias = Para receber algumas noticias')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(1)
			actions.send_keys('/fofocas = Para receber as ultimas fofocas')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(1)
			actions.send_keys('/moedas = Para receber a cotação atual das principais moedas')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(1)
			actions.send_keys('/tabela = Para receber a tabela do Brasileirao Serie A')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(1)
			actions.send_keys('/jogos = Para receber os jogos da rodada atual do Brasileirao Serie A')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(1)
			actions.send_keys('/filmes = Para receber os filmes que estao em cartaz')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(1)
			actions.send_keys('/desliga_luz = Para desligar a luz do corredor')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(1)
			actions.send_keys('/liga_luz = Para ligar a luz do corredor')
			actions.perform()
			actions.reset_actions()
			self.quebra_linha(1)
			actions.send_keys('/comandos = Para receber uma lista de comandos')
			actions.perform()
			actions.reset_actions()
			botaoEnviar = self.driver.find_element_by_class_name('_3M-N-')
			botaoEnviar.click()


	def message_loop(self):
		data = {'chatid': '', 'text': '', 'time': ''}
		contactBox = self.driver.find_elements_by_class_name('_2wP_Y')
		try:
			if(self.driver.find_element_by_class_name('_3KRbU')):
				droppage = self.driver.find_element_by_class_name('_3KRbU')
				droppage.click()
		except:
			pass
		try:
			if(self.driver.find_element_by_class_name('P6z4j')):
				escolha_contato = self.driver.find_element_by_class_name('P6z4j')
				escolha_contato.click()
				time.sleep(1)
				chatid = self.driver.find_element_by_class_name('_19RFN').text
				
				post = self.driver.find_elements_by_class_name('_1ays2')
				ultimo_post = len(post) - 1
				print(post[ultimo_post].find_element_by_class_name('_F7Vk').find_element_by_tag_name('span').text)
				try:
					time.sleep(1)
					hora = post[ultimo_post].find_element_by_class_name('_3fnHB').text
					texto = post[ultimo_post].find_element_by_class_name('_F7Vk').find_element_by_tag_name('span').text
					data = {'chatid': str(chatid),
						    'text': str(texto),
						    'time': str(hora)}
				
					return data

				except:
					print('recebido mensagem sem texto')
					return data
		except:
			return data
