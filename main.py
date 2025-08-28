from core.camera import Camera
from core.gesture_controller import GestureController
from core.hand_tracker import HandTracker
from core.helpers.mouse_controller import MouseController
import cv2

def main():
    cam = Camera()
    tracker = HandTracker()
    controller = GestureController()
    mouse = MouseController()

    try:
        while True:
            frame = cam.get_frame()
            hand_landmarks_list = tracker.get_landmarks(frame)

            if hand_landmarks_list:
                # Usamos la primera mano detectada
                landmarks = hand_landmarks_list[0]
                gesture = controller.interpret_gesture([landmarks])

                if gesture:
                    mouse.handle_gesture(gesture)
                    cv2.putText(frame, f"Gesto: {gesture}", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("CamComand - Control por gestos", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break
    finally:
        cam.release()

if __name__ == "__main__":
    main()