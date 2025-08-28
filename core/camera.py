import cv2

class Camera:
    def __init__(self, camera_index=0, width=640, height=480): #camera index es la camara por defecto
        #configurar la camara
        self.cap = cv2.VideoCapture(camera_index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        if not self.cap.isOpened():
            raise IOError("No se pudo acceder a la cámara.")

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("No se pudo leer el frame de la cámara.")
         # 🔁 Invertir el eje X (efecto espejo)
        frame = cv2.flip(frame, 1)
        return frame


    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()