import time
from pynput.mouse import Button, Controller

boot = Controller()


print("===========================================================")
print("----VAMOS INICIAR ,PREPARE-SE PARA RECUPERAR OS BOTÕES---- ")
print("===========================================================")
time.sleep(3)

print("VC TEM 10 SEGUNDOS PRA NAVEGAR ATE OS BOTÕES")
time.sleep(3)

print("LEVE O MOUSE ATE A CASA DOS HEROIS ")
time.sleep(10)
entraHerois = boot.position
print("PRONTO")

print("LEVE O MOUSE ATE O BOTÃO DESCANSAR ")
time.sleep(10)
descansar = boot.position
print("PRONTO")

print("LEVE O MOUSE ATE O TRABALHAR")
time.sleep(10)
Trabalhar = boot.position
print("PRONTO")

print("LEVE O MOUSE ATE FECHAR CASA DOS HEROIS  ")
time.sleep(10)
fecharherois = boot.position
print("PRONTO")

print("LEVE O MOUSE ATE O MAPA ")
time.sleep(10)
mapa = boot.position
print("PRONTO")

print("LEVE O MOUSE PARA FECHA O MAPA ")
time.sleep(10)
fecharMapa = boot.position
print("PRONTO")

print("===========================================================")
print("--------POSIÇÃO DOS BOTÕES RECUPERADOS COM SUCESSO ------- ")
print("-----------DEIXA A TELA DO JOGO NA PAGINA INICIAL---------- ")
print("===========================================================")

time.sleep(10)
print("===========================================================")
print("--------PODE DEIXA PQ AGORA É COMIGO ,BOM DESCANSO ------- ")
print("===========================================================")

while True:

    boot.position =(entraHerois)
    time.sleep(2)
    boot.click(Button.left)
    time.sleep(5)

    boot.position =(descansar)
    time.sleep(2)
    boot.click(Button.left)
    time.sleep(3600)

    boot.position =(Trabalhar)
    time.sleep(2)
    boot.click(Button.left)
    time.sleep(5)

    boot.position =(fecharherois)
    time.sleep(2)
    boot.click(Button.left)
    time.sleep(5)

    for i in range(1,5):

        boot.position =(mapa)
        time.sleep(2)
        boot.click(Button.left)
        time.sleep(420)

        boot.position =(fecharMapa)
        time.sleep(2)
        boot.click(Button.left)
        time.sleep(10)
