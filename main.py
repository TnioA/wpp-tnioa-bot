# -*- coding: utf-8 -*-
import json
import requests
from app import Botzap
import re
import time

def getnews():
	#API DE NOTICIAS GLOBO BRASIL
	url = 'https://newsapi.org/v2/top-headlines?sources=globo&pageSize=5&apiKey=f6fdb7cb0f2a497d92dbe719a29b197f'
	#http = urllib3.PoolManager()
	#resp = http.request('GET',url)
	resp = requests.get(url)
	conteudo = json.loads(resp.content)
	return(conteudo)

def getfutebol():
	#API DE DE FUTEBOL
	url = 'http://restfutebol.herokuapp.com/api/futebol/serie-a/tabela'
	resp = requests.get(url)
	conteudo = json.loads(resp.content)
	return(conteudo)

def getmovies():
	#API DE FILMES BRASIL
	url = 'http://restmovies.herokuapp.com/api/filmes'
	resp = requests.get(url)
	conteudo = json.loads(resp.content)
	return(conteudo)

bot = Botzap('TanTanio_bot')

while True:

	conteudo = bot.message_loop()
	# verifica a chave 'text' dentro do json retorno
	if 'text' in conteudo:
		retorno = conteudo['text']
		if retorno == '/oibot':
			print('recebido comando ola')
			bot.sendMessage('Oi eu sou o bot do Tanio responda com /comandos para receber a lista de comandos e conseguir se comunicar comigo')
		
		elif retorno == '/filmes':
			print('recebido o comando filmes')
			conteudo = getmovies()
			msg_movies = ''
			c = 1
			for cont in conteudo['filmes']:
				msg_movies = msg_movies + ('Filme {}: \n'.format(c) + 'Titulo: ' + cont['nome'] + ' Estreado em: ' + cont['data'] + '\n')
				c = int(c) + 1
			bot.sendMessage(msg_movies)
		
		elif retorno == '/futebol':
			print('recebido o comando futebol')
			conteudo = getfutebol()
			msg_futebol = ''
			for cont in conteudo['tabela']:
				msg_futebol = msg_futebol + (cont['posicao'] + ' - ' + cont['time'] + '\n')
			bot.sendMessage(msg_futebol)
		
		elif retorno == '/noticias':
			print('recebido o comando noticias')
			conteudo = getnews()
			msg_news = ''
			c = 1
			for cont in conteudo['articles']:
				msg_news = (msg_news + ('Noticia {}: \n'.format(c) + cont['title'] + '\n'))
				c = int(c) + 1
			bot.sendMessage(msg_news)

		elif retorno == '/comandos':
			print('recebido comando lista de comandos')
			bot.sendMessage('Comandos:\n/oibot = Para me chamar\n/noticias = Para receber algumas noticias\n/futebol = Para receber a tabela do Brasileirao Serie A\n/filmes = Para receber os filmes que estao em cartaz\n/comandos = Para receber uma lista de comandos')

		else:
			pass
	else:
		pass