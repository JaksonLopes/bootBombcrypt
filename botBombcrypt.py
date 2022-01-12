
import time
import pyautogui

descansar = 'descansar.PNG'
Trabalhar = 'trabalhar.PNG'
fecharherois = 'fherois.PNG'
mapa = 'mapa.PNG'
fecharMapa = 'fmapa.PNG'
entraHerois = 'herois.PNG'
cheio = 'cheio.PNG'

boot = pyautogui

while True:
    if boot.locateCenterOnScreen(cheio) or boot.locateCenterOnScreen(cheio):
        print('entrei no descanço dos herois')
        local = boot.locateCenterOnScreen(Trabalhar)
        boot.click(local)
        time.sleep(15)

        local = boot.locateCenterOnScreen(fecharherois)
        boot.click(local)
        time.sleep(15)

        for i in range(1,4):
            print('entrei no mapa ')
            local = boot.locateCenterOnScreen(mapa)
            boot.click(local)
            time.sleep(300)

            local = boot.locateCenterOnScreen(fecharMapa)
            boot.click(local)
            time.sleep(15)
        
        local = boot.locateCenterOnScreen(entraHerois)
        boot.click(local)
        time.sleep(15)

        local = boot.locateCenterOnScreen(descansar)
        boot.click(local)
        time.sleep(3600)

        

    elif boot.locateCenterOnScreen(mapa) or boot.locateCenterOnScreen(entraHerois):
        print('?????????')
        local = boot.locateCenterOnScreen(entraHerois)
        boot.click(local)
        time.sleep(10)
    else:
        print('não achei nehuma imagem correspondente ')
