import time
from pynput.mouse import Button, Controller

boot = Controller()

""" 
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

print("entraHerois =",entraHerois)
print("descansar =",descansar)
print("Trabalhar =",Trabalhar)
print("fecharherois =",fecharherois)
print("mapa =",mapa)
print("fecharMapa =",fecharMapa)

time.sleep(444444)
 """



print("===========================================================")
print("--------POSIÇÃO DOS BOTÕES RECUPERADOS COM SUCESSO ------- ")
print("-----------DEIXA A TELA DO JOGO NA PAGINA INICIAL---------- ")
print("===========================================================")


print("===========================================================")
print("--------PODE DEIXA PQ AGORA É COMIGO ,BOM DESCANSO ------- ")
print("-----------DEIXA A TELA DO JOGO NA PAGINA INICIAL---------- ")
print("===========================================================")
time.sleep(10)

entraHerois = (1062, 648)
descansar = (633, 274)
Trabalhar = (567, 277)
fecharherois = (711, 224)
mapa = (668, 420)
fecharMapa = (213, 144)


while True:
    
    boot.position =(entraHerois)
    time.sleep(2)
    boot.click(Button.left)
    time.sleep(15)
    
    boot.position =(descansar)
    time.sleep(2)
    boot.click(Button.left)
    print("descanço")

    for i in range(0,12):
        time.sleep(420)

        boot.position =(fecharherois)
        time.sleep(2)
        boot.click(Button.left)
        time.sleep(5)

        boot.position =(entraHerois)
        time.sleep(2)
        boot.click(Button.left)
        time.sleep(5)


    boot.position =(Trabalhar)
    time.sleep(2)
    boot.click(Button.left)
    time.sleep(5)

    boot.position =(fecharherois)
    time.sleep(2)
    boot.click(Button.left)
    time.sleep(5)

    for i in range(0,11):

        boot.position =(mapa)
        time.sleep(2)
        boot.click(Button.left)
        time.sleep(200)
        print("mapa")

        boot.position =(fecharMapa)
        time.sleep(2)
        boot.click(Button.left)
        time.sleep(5)

        if i == 7 or i == 9 :
            
            boot.position =(entraHerois)
            time.sleep(2)
            boot.click(Button.left)
            time.sleep(5)

            boot.position =(Trabalhar)
            time.sleep(2)
            boot.click(Button.left)
            time.sleep(5)

            boot.position =(fecharherois)
            time.sleep(2)
            boot.click(Button.left)
            time.sleep(5)



