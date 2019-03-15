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

	if retorno == 'Bot:oibot':
		print('recebido comando ola')
		bot.write('Oi eu sou o bot do Tanio responda com Bot:comandos para receber a lista de comandos e conseguir se comunicar comigo')
	
	if retorno == 'Bot:filmes':
		conteudo = getmovies()
		c = 1
		print('recebido o comando filmes')
		for cont in conteudo['filmes']:
			bot.write('Filme {}: \n'.format(c) + 'Titulo: ' + cont['nome'] + ' Estreado em: ' + cont['data'])
			c = int(c) + 1
	
	if retorno == 'Bot:futebol':
		print('recebido o comando futebol')
		bot.write('Ainda em desenvolvimento')
	
	if retorno == 'Bot:noticias':
		print('recebido o comando noticias')
		conteudo = getnews()
		c = 1
		for cont in conteudo['articles']:
			bot.write('Noticia {}: '.format(c) + cont['title'])
			c = int(c) + 1

	if retorno == 'Bot:comandos':
		print('recebido comando lista de comandos')
		bot.write('Comandos ==================================> \n Bot:oibot = Para me chamar \n Bot:noticias = Para receber algumas noticias \n Bot:futebol = Para receber a tabela do Brasileirao Serie A \n Bot:filmes = Para receber os filmes que estao em cartaz \n Bot:comandos = Para receber uma lista de comandos \n >>=============================>')
pass