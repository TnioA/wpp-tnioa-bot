# -*- coding: utf-8 -*-
import requests, json, os, re

def getnews():
	#API DE NOTICIAS GLOBO BRASIL
	url = 'https://newsapi.org/v2/top-headlines?sources=globo&pageSize=5&apiKey=f6fdb7cb0f2a497d92dbe719a29b197f'
	#http = urllib3.PoolManager()
	#resp = http.request('GET',url)
	resp = requests.get(url)
	conteudo = json.loads((resp.content).decode('utf-8'))
	return(conteudo)

def gettabela():
	#API DE DE FUTEBOL
	url = 'http://restfutebol.herokuapp.com/api/futebol/serie-a/tabela'
	resp = requests.get(url)
	conteudo = json.loads((resp.content).decode('utf-8'))
	return(conteudo)

def getjogos():
	#API DE DE FUTEBOL
	url = 'http://restfutebol.herokuapp.com/api/futebol/serie-a/jogos'
	resp = requests.get(url)
	conteudo = json.loads((resp.content).decode('utf-8'))
	return(conteudo)

def getmovies():
	#API DE FILMES BRASIL
	url = 'http://restmovies.herokuapp.com/api/filmes'
	resp = requests.get(url)
	conteudo = json.loads((resp.content).decode('utf-8'))
	return(conteudo)

def getmoedas():
	#API DE COTACOES
	url = 'https://restcotacoes.herokuapp.com/'
	resp = requests.get(url)
	conteudo = json.loads((resp.content).decode('utf-8'))
	return(conteudo)

def getfofocas():
	#API DE FOFOCAS
	url = 'https://restfofocas.herokuapp.com/api/fofocas'
	resp = requests.get(url)
	conteudo = json.loads((resp.content).decode('utf-8'))
	return(conteudo)
