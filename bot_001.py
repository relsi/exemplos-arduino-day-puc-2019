# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("Alfred")

dialogos = [
  ['oi', 'olá', 'como vai', 'tudo bem?', 'tudo bem, e com você?', 'eu estou bem', 'em que posso ajudar?'],
  ['qual é o seu nome', 'você gosta de séries', 'eu prefiro filmes', 'esse ano tem ótimos lançamentos no cimena', 'que tipos de filmes você gosta?', 'eu gosto de filmes de ficção científica', 'é bom de assistir'],
  ['de onde você é?', 'sou de porto alegre', 'no momento estou morando na memória do teu notebook', 'como está o clima em porto alegre?']
]

trainer = ListTrainer(bot)

for dialogo in dialogos:
  trainer.train(dialogo)

while True:
  chat = input("Você: ")
  resposta = bot.get_response(chat)
  print("Alfred: ", resposta)
