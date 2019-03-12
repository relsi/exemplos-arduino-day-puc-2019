# Palestra Arduino Day PUC/RS 2019
Tutorial e Código fonte do exemplo utilizado na palestra ***Assistente Pessoal com Arduino e IA*** (linux)

Instalação do ***Chatterbot***:

```bash
sudo pip3 install chatterbot
```

***Bot Básico:***

```python
# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Alfred')

dialogos = [
  ['oi', 'olá', 'como vai', 'tudo bem?', 'tudo bem, e com você?', 'eu estou bem', 'em que posso ajudar?'],
  ['qual é o seu nome', 'você gosta de séries', 'eu prefiro filmes', 'esse ano tem ótimos lançamentos no cimena', 'que tipos de filmes você gosta?', 'eu gosto de filmes de ficção científica', 'é bom de assistir'],
  ['de onde você é?', 'sou de porto alegre', 'no momento estou morando na memória do teu notebook', 'como está o clima em porto alegre?']
]

bot.set_trainer(ListTrainer)

for grupo in dialogos:
  bot.train(grupo)

while True:
  chat = input("Você: ")
  resposta = bot.get_response(chat)
  print("Alfred: ", resposta)



```
