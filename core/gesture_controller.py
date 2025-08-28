import pyautogui
import math
import numpy as np


class GestureController:
    def __init__(self, screen_width=None, screen_height=None):
        self.screen_width = screen_width or pyautogui.size().width
        self.screen_height = screen_height or pyautogui.size().height

    def get_finger_distance(self, landmark1, landmark2):
        x1, y1 = landmark1.x, landmark1.y
        x2, y2 = landmark2.x, landmark2.y
        return math.hypot(x2 - x1, y2 - y1)

    def interpret_gesture(self, hand_landmarks):
        if not hand_landmarks:
            return None

        # Usamos la primera mano detectada
        hand = hand_landmarks[0]
        landmarks = hand

        # Ejemplo: distancia entre pulgar y índice
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        distance = self.get_finger_distance(thumb_tip, index_tip)

        # Umbral para gesto de "clic"
        if distance < 0.05:
            pyautogui.click()
            return "click"

        # Ejemplo: mover el cursor con la punta del índice
        cursor_x = int(landmarks[8].x * self.screen_width)
        cursor_y = int(landmarks[8].y * self.screen_height)
        pyautogui.moveTo(cursor_x, cursor_y)
        return "move"

        # Puedes añadir más gestos aquí (scroll, doble clic, etc.)

        #dibujar
    def __init__(self, screen_width=None, screen_height=None):
        self.screen_width = screen_width or pyautogui.size().width
        self.screen_height = screen_height or pyautogui.size().height
        self.drawing = False

    def is_drawing_gesture(self, landmarks, threshold=0.05):
        thumb_tip = np.array([landmarks[4].x, landmarks[4].y])
        index_tip = np.array([landmarks[8].x, landmarks[8].y])
        middle_tip = np.array([landmarks[12].x, landmarks[12].y])

        dist_thumb_index = np.linalg.norm(thumb_tip - index_tip)
        dist_thumb_middle = np.linalg.norm(thumb_tip - middle_tip)
        dist_index_middle = np.linalg.norm(index_tip - middle_tip)

        return dist_thumb_index < threshold and dist_thumb_middle < threshold and dist_index_middle < threshold
    
    def interpret_gesture(self, hand_landmarks):
        if not hand_landmarks:
            return None

        hand = hand_landmarks[0]
        landmarks = hand

        # Mover el cursor con el índice
        cursor_x = int(landmarks[8].x * self.screen_width)
        cursor_y = int(landmarks[8].y * self.screen_height)
        pyautogui.moveTo(cursor_x, cursor_y)

        # Detectar gesto de garra para dibujar
        if self.is_drawing_gesture(landmarks):
            if not self.drawing:
                pyautogui.mouseDown()
                self.drawing = True
            return "draw"
        else:
            if self.drawing:
                pyautogui.mouseUp()
                self.drawing = False
            return "move"


