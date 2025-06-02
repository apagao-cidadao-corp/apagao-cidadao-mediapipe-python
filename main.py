import cv2
import mediapipe as mp
import threading
import pygame
import numpy as np

# Inicializa o mixer de som
pygame.mixer.init()

# Configuração do MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Flags para controle dos alertas
alert_emergency = False
alert_medical = False
lanterna_ativa = False
status_chamado = "Nenhum"

# Funções de som
def play_emergency():
    pygame.mixer.music.load("sounds/alert_urgente.wav")
    pygame.mixer.music.play()

def play_medical():
    pygame.mixer.music.load("sounds/alerta_medico.wav")
    pygame.mixer.music.play()

# Função de lanterna
def show_flashlight():
    white_screen = 255 * np.ones((480, 640, 3), dtype=np.uint8)
    start_time = cv2.getTickCount()
    duration = 5  # segundos
    while (cv2.getTickCount() - start_time)/cv2.getTickFrequency() < duration:
        cv2.imshow("Lanterna de Emergência", white_screen)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyWindow("Lanterna de Emergência")

# Função para contar dedos
def count_fingers(hand_landmarks, hand_label):
    finger_tips = [8, 12, 16, 20]
    count = 0
    for tip_id in finger_tips:
        if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y:
            count += 1
    if hand_label == "Right":
        if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
            count += 1
    else:
        if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
            count += 1
    return count

# Inicia a webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Simula ambiente escuro
    dark_frame = cv2.convertScaleAbs(frame, alpha=0.4, beta=0)
    rgb = cv2.cvtColor(dark_frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(result.multi_hand_landmarks):
            hand_label = result.multi_handedness[idx].classification[0].label
            finger_count = count_fingers(hand_landmarks, hand_label)
            mp_draw.draw_landmarks(dark_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if finger_count == 5 and not alert_emergency:
                print("🚨 Pedido de ajuda URGENTE detectado!")
                threading.Thread(target=play_emergency).start()
                alert_emergency = True
                status_chamado = "Urgente"

            elif finger_count == 3 and not alert_medical:
                print("🩺 Pedido de AJUDA MÉDICA detectado!")
                threading.Thread(target=play_medical).start()
                alert_medical = True
                status_chamado = "Medico"

            elif finger_count == 1 and not lanterna_ativa:
                print("💡 Lanterna de emergencia ativada!")
                threading.Thread(target=show_flashlight).start()
                lanterna_ativa = True
                status_chamado = "Lanterna de Emergencia"

            elif finger_count == 0:
                if alert_emergency or alert_medical or lanterna_ativa:
                    print("🔕 Alertas cancelados")
                    alert_emergency = False
                    alert_medical = False
                    lanterna_ativa = False
                    status_chamado = "Nenhum"

            # Mostra número de dedos e tipo de alerta na tela
            cv2.putText(dark_frame, f'Dedos: {finger_count}', (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
            cv2.putText(dark_frame, f'Alerta: {status_chamado}', (10, 120),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 2)

    cv2.imshow("Helping Hands - Emergencia por Gestos", dark_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
