import pyautogui
import time
import keyboard

def escolherDelay(betweenClicks):
    try:
        while int(betweenClicks) <= 0:
            betweenClicks = pyautogui.prompt('Escolha um valor válido')
            return escolherDelay(betweenClicks)
        return betweenClicks
    except: 
       betweenClicks = pyautogui.prompt('Escolha um valor válido')
       return escolherDelay(betweenClicks)
    
def clicar(hotkey,running):
    #print (running)
    if running:
        pyautogui.click(pyautogui.position())
        startTime = time.time()
        while keyboard.is_pressed(hotkey) == False:
            if keyboard.is_pressed('esc') == True:
                break
            currentTime = time.time()
            if (currentTime - startTime >= betweenClicks):
                pyautogui.click(pyautogui.position())
                startTime = time.time()
        return
    else:
        time.sleep(1)
        return

betweenClicks = pyautogui.confirm('Escolha o espaço entre cliques em segundos', buttons=['1', '2', '3','4','5','personalizado...'])
if betweenClicks == 'personalizado...':
    betweenClicks = escolherDelay(betweenClicks)
pyautogui.alert("Escolha a tecla para ativar/desativar clique.\n (Pressione uma tecla após o 'OK' ")
hotkey = keyboard.read_key()
pyautogui.alert("Pronto!\nPara começar feche o alerta e clique '"+hotkey+"'")
betweenClicks = int(betweenClicks)
running = False
while keyboard.is_pressed('esc') == False:    
    if keyboard.is_pressed(hotkey) == True:
        running = not running
        clicar(hotkey,running)
        

pyautogui.alert("Programa fechado.")
