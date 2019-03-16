from chatterbot import ChatBot

bot = ChatBot(
    'Alfred',
    logic_adapters=[{
        'import_path': 'arduino_adapter.DesligaLuz',
        'default_response': 'Desculpe, não entendi.',
    }]
)

while True:
    chat = input("Você: ")
    resposta = bot.get_response(chat) or ''
    if resposta:
        print("Alfred:", resposta)

