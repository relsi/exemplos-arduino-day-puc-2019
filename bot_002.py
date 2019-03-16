# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
	"Alfred",
	logic_adapters=[
		{
		    'import_path': 'chatterbot.logic.BestMatch',
		    'default_response': 'Desculpe, não entendi.',
		    'maximum_similarity_threshold': 0.90
		}
	]
)

dialogos = [
  'oi', 'olá', 'como vai', 'tudo bem?', 'tudo bem, e com você?', 'eu estou bem', 'em que posso ajudar?',
  'qual é o seu nome', 'Alfred', 'você gosta de séries', 'eu prefiro filmes',
  'de onde você é?', 'sou de porto alegre', 'onde você mora', 'no momento estou morando na memória do teu notebook'
]

trainer = ListTrainer(bot)

trainer.train(dialogos)

while True:
  chat = input("Você: ")
  resposta = bot.get_response(chat)
  print("Alfred:", resposta)
