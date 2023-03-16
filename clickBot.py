import pyautogui
import time
import keyboard

def escolherDelay(betweenClicks):
    try:
        while float(betweenClicks) < 0:
            betweenClicks = pyautogui.prompt('Escolha um valor válido')
            return escolherDelay(betweenClicks)
        return betweenClicks
    except: 
       betweenClicks = pyautogui.prompt('Escolha um valor válido')
       return escolherDelay(betweenClicks)
    
def clicar(hotkey):
    time.sleep(.5)
    pyautogui.click(pyautogui.position())
    startTime = time.time()
    while keyboard.is_pressed(hotkey) == False:
        if keyboard.is_pressed('esc') == True:
            return
        currentTime = time.time()
        if (currentTime - startTime >= betweenClicks):
            pyautogui.click(pyautogui.position())
            startTime = time.time()
    print("Parou...")        
    time.sleep(.5)
    return

betweenClicks = pyautogui.confirm('Escolha o espaço entre cliques em segundos', buttons=['1', '2', '3','4','5','personalizado...'])
if betweenClicks == 'personalizado...' or betweenClicks == None:
    betweenClicks = escolherDelay(betweenClicks)
pyautogui.alert("Escolha a tecla para ativar/desativar clique.\n (Pressione uma tecla após o 'OK' ")
hotkey = keyboard.read_key()
pyautogui.alert("Pronto!\nPara começar feche o alerta e clique '"+hotkey+"'")
betweenClicks = float(betweenClicks)
while keyboard.is_pressed('esc') == False:
    if keyboard.is_pressed(hotkey) == True:        
        print("Clicando...")
        clicar(hotkey)       
print("Fechou...") 
pyautogui.alert("Programa fechado.")
