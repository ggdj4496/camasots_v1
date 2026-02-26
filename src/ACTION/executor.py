import pyautogui
class HardwareAction:
    def move_to_element(self, x, y):
        pyautogui.moveTo(x, y, duration=0.5)
        pyautogui.click()
