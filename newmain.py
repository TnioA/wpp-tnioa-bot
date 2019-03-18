# -*- coding: utf-8 -*-
import json, requests
from app import Botzap
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


bot = Botzap('+55 85 8407-3833')




while True:
	retorno = bot.message_loop()
	print(retorno)
	pass