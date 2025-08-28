# helpers/gesture_helper.py

import numpy as np

def is_drawing_gesture(landmarks, threshold=0.05):
    """
    Detecta si el pulgar, índice y medio están formando una pinza.
    """
    if landmarks is None:
        return False

    # Coordenadas normalizadas de las puntas
    thumb_tip = np.array([landmarks[4].x, landmarks[4].y])
    index_tip = np.array([landmarks[8].x, landmarks[8].y])
    middle_tip = np.array([landmarks[12].x, landmarks[12].y])

    # Distancias entre las puntas
    dist_thumb_index = np.linalg.norm(thumb_tip - index_tip)
    dist_thumb_middle = np.linalg.norm(thumb_tip - middle_tip)
    dist_index_middle = np.linalg.norm(index_tip - middle_tip)

    # Si todas están cerca, activamos el gesto
    return dist_thumb_index < threshold and dist_thumb_middle < threshold and dist_index_middle < threshold