import pyautogui as posicaoMouse
import pyautogui as tempoEspera

#Tempo de espera para que o computador possa pensar.
tempoEspera.sleep(2)

#Movendo o mouse até  botão iniciar
posicaoMouse.moveTo(21, 889)

#Tempo de espera para que o computador possa pensar.
tempoEspera.sleep(2)

#Clicando na posição
posicaoMouse.click(21, 889)

#Tempo de espera para que o computador possa pensar.
tempoEspera.sleep(2)

#Escrevendo a palavra calc
posicaoMouse.typewrite('calc')

#Tempo de espera para que o computador possa pensar.
tempoEspera.sleep(1)

#Movendo o mouse até  o aplicativo da calculadora
posicaoMouse.moveTo(x=186, y=328)

#Tempo de espera para que o computador possa pensar.
tempoEspera.sleep(2)

#Clicando na calculadora
posicaoMouse.click(x=186, y=328)

#Tempo de espera para que o computador possa pensar.
tempoEspera.sleep(2)

#print(posicaoMouse.position())