import pyautogui

class MouseController:
    def __init__(self):
        self.clicking = False

    def handle_gesture(self, gesture):
        if gesture == "garra" and not self.clicking:
            pyautogui.mouseDown()
            self.clicking = True
        elif gesture != "garra" and self.clicking:
            pyautogui.mouseUp()
            self.clicking = False