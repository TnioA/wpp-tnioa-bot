# -*- coding: utf-8 -*-
import os, re, time, json
from app import Botzap


bot = Botzap('TanTanio_bot') #nome/numero do usuario pra mandar mensagem de ativo

while True:
    conteudo = bot.message_loop()
    # verifica a chave 'text' dentro do json retorno
    if 'text' in conteudo:
        retorno = conteudo['text']
        retorno = retorno + '.'
        if retorno[0] == '/':
            if retorno == '/oibot.':
                print('recebido o comando ola')
                bot.sendMessage('ola')
            elif retorno == '/relatorio.':
                print('recebido o comando relatorio')
                bot.sendMessage('relatorio')
            elif retorno == '/clima.':
                print('recebido o comando clima')
                bot.sendMessage('clima')
            elif retorno == '/filmes.':
                print('recebido o comando filmes')
                bot.sendMessage('filmes')
            elif retorno == '/fofocas.':
                print('recebido o comando fofocas')
                bot.sendMessage('fofocas')
            elif retorno == '/tabela.':
                print('recebido o comando tabela')
                bot.sendMessage('tabela')
            elif retorno == '/jogos.':
                print('recebido o comando jogos')
                bot.sendMessage('jogos')
            elif retorno == '/noticias.':
                print('recebido o comando noticias')
                bot.sendMessage('noticias')
            elif retorno == '/moedas.':
                print('recebido o comando moedas')
                bot.sendMessage('moedas')
            elif retorno == '/desliga_luz.':
                print('recebido o comando desligar luz')
                bot.sendMessage('desligaluz')
            elif retorno == '/liga_luz.':
                print('recebido o comando ligar luz')
                bot.sendMessage('ligaluz')
            elif retorno == '/comandos.':
                print('recebido o comando lista de comandos')
                bot.sendMessage('comandos')
            else:
                print('Recebido comando incorreto')
                bot.sendMessage('erro')
        else:
            pass
    else:
        pass