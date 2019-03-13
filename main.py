# -*- coding: utf-8 -*-
from app import Botzap
import re


contato = 'Samuel'
contato = str(contato)
mensagem = 'Bot:: Mensagem de teste enviada pelo bot do Tanio'
mensagem = str(mensagem)


bot = Botzap('robozin')

bot.send(contato, mensagem)
#bot.read()
