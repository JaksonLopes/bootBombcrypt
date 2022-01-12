
from time import time
import pyautogui

Descansar = 'descansar.PNG'
Trabalhar = 'trabalhar.PNG'
fecharherois = 'fherois.PNG'
mapa = 'mapa.PNG'
fecharMapa = 'fmapa.PNG'
entraHerois = 'herois.PNG'



bot = pyautogui

local = bot.locateCenterOnScreen(mapa)


print(local)

for i in range(1,20000):

    time.sleep(2)
    local = bot.locateCenterOnScreen(mapa)
    bot.click(local)

