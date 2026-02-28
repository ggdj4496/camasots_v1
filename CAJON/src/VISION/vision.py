import pyautogui, cv2, numpy as np, os

class EagleEye:
    def __init__(self):
        self.db_path = "C:/CAMASOTS_V1/database"

    def scan_screen(self):
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        cv2.imwrite(os.path.join(self.db_path, "current_view.png"), frame)
        return "Captura analizada por Virgilio."
