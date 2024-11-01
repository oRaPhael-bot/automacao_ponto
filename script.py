import pyautogui
import time
# pyautogui.click
# pyautogui.write
# pyautogui.press
# pyautogui.hotkey

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(6)
pyautogui.write("https://tecnosetinformatica144050.rm.cloudtotvs.com.br/FrameHTML/web/app/RH/PortalMeuRH/#/home")
pyautogui.press("enter")

time.sleep(6)

pyautogui.click(x=339, y=442)
pyautogui.click(x=359, y=528)
pyautogui.click(x=279, y=517)
pyautogui.click(x=331, y=534)
