import pyautogui
import cv2
import numpy as np

class EagleEye:
    def capture_context(self):
        # Captura HD de monitor para análisis de IA
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        cv2.imwrite("C:/CAMASOTS_V1/database/last_scan.png", frame)
        return "Captura guardada para análisis."
