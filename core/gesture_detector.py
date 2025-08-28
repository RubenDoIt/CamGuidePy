import mediapipe as mp
import cv2

class GestureDetector:
    def __init__(self, max_num_hands=1, detection_confidence=0.7, tracking_confidence=0.7):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=max_num_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils

    def detect(self, frame):
        # Convertir a RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        hand_landmarks = []
        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                hand_landmarks.append(hand)
        return hand_landmarks

    def draw_landmarks(self, frame, hand_landmarks):
        for hand in hand_landmarks:
            self.mp_draw.draw_landmarks(
                frame, hand, self.mp_hands.HAND_CONNECTIONS
            )
        return frame