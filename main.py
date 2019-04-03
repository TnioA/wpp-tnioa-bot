# -*- coding: utf-8 -*-
import os, re, time, json
from app import Botzap


bot = Botzap('TanTanio_bot') #nome do usuario pra mandar mensagem de ativo

while True:

	conteudo = bot.message_loop()
	# verifica a chave 'text' dentro do json retorno
	if 'text' in conteudo:
		retorno = conteudo['text']
		if retorno == '/oibot':
			print('recebido comando ola')
			bot.sendMessage('ola')
		
		elif retorno == '/filmes':
			print('recebido o comando filmes')
			bot.sendMessage('filmes')
		
		elif retorno == '/tabela':
			print('recebido o comando tabela')
			bot.sendMessage('tabela')

		elif retorno == '/jogos':
			print('recebido o comando jogos')
			bot.sendMessage('jogos')
		
		elif retorno == '/noticias':
			print('recebido o comando noticias')
			bot.sendMessage('noticias')

		elif retorno == '/moedas':
			print('recebido o comando moedas')
			bot.sendMessage('moedas')

		elif retorno == '/comandos':
			print('recebido comando lista de comandos')
			bot.sendMessage('comandos')

		else:
			pass
	else:
		pass