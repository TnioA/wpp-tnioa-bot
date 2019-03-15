# -*- coding: utf-8 -*-
import json, requests
from simpleapp import Botzap
import re

def getnews():
	#API DE NOTICIAS BRASIL
	url = 'https://newsapi.org/v2/top-headlines?sources=globo&pageSize=5&apiKey=f6fdb7cb0f2a497d92dbe719a29b197f'
	#http = urllib3.PoolManager()
	#resp = http.request('GET',url)
	resp = requests.get(url)
	conteudo = json.loads(resp.content)
	return(conteudo)


def getmovies():
	#API DE FILMES BRASIL
	url = 'http://localhost:5000/api/filmes'
	resp = requests.get(url)
	conteudo = json.loads(resp.content)
	return(conteudo)


contato = str('BotTnioA')
mensagem = str('Bot:: Mensagem de teste enviada pelo bot do Tanio')


bot = Botzap('Teste')

#bot.send(contato, mensagem)

while True:
	retorno = bot.monitor()

	if retorno == '/oibot':
		print('recebido comando ola')
		bot.write('Oi eu sou o bot do Tanio responda com Bot:comandos para receber a lista de comandos e conseguir se comunicar comigo')
	
	if retorno == '/filmes':
		print('recebido o comando filmes')
		conteudo = getmovies()
		msg_movies = ''
		c = 1
		for cont in conteudo['filmes']:
			msg_movies = msg_movies + ('Filme {}: \n'.format(c) + 'Titulo: ' + cont['nome'] + ' Estreado em: ' + cont['data'] + '\n\n')
			c = int(c) + 1
		bot.write(msg_movies)
	
	if retorno == '/futebol':
		print('recebido o comando futebol')
		bot.write('Ainda em desenvolvimento')
	
	if retorno == '/noticias':
		print('recebido o comando noticias')
		conteudo = getnews()
		msg_news = ''
		c = 1
		for cont in conteudo['articles']:
			msg_news = (msg_news + ('Noticia {}: \n'.format(c) + cont['title'] + '\n\n'))
			c = int(c) + 1
		bot.write(msg_news)

	if retorno == '/comandos':
		print('recebido comando lista de comandos')
		bot.write('Comandos:\n/oibot = Para me chamar\n/noticias = Para receber algumas noticias\n/futebol = Para receber a tabela do Brasileirao Serie A\n/filmes = Para receber os filmes que estao em cartaz\n/comandos = Para receber uma lista de comandos')
pass