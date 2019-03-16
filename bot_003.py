from chatterbot import ChatBot

bot = ChatBot(
    'Alfred',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.db'
)

while True:
    chat = input("Você: ")
    resposta = bot.get_response(chat)
    print("Alfred:", resposta)

