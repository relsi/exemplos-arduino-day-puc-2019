# -*- coding: utf-8 -*-
from chatterbot.logic import LogicAdapter

class DesligaLuz(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, txt):
        return True

    def process(self, txt, par):
        from chatterbot.conversation import Statement
        if 'apagar' in str(txt):
            import serial
            import time

            conexao = serial.Serial('/dev/ttyACM0', 9600)
            time.sleep(1.8)
            conexao.write(b'D')
            conexao.close()
            resposta = Statement(text='Apaguei a luz')
        else:
            resposta = Statement(text='Hummmmmm')
        
        return resposta
