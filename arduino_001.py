# -*- coding: utf-8 -*-
import serial
import time
conexao = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(1.8)
conexao.write(b'D')
conexao.close()
