# Importa as biblitoecas necessárias
from ultralytics import YOLO
import cv2 as cv

# Cria um objeto VideoCapture para capturar o vídeo da câmera (0 representa a câmera padrão)
web_cam = cv.VideoCapture(0)

# Inicializa o modelo YOLO com o modelo pré-treinado "best.pt"
model = YOLO("best.pt")

while True:
    # Lê um frame da captura de vídeo
    _, frame = web_cam.read()

    # Utiliza o modelo YOLO para prever objetos no frame com um limiar de confiança de 0.3
    result = model.predict(frame, conf=0.5)

    # Exibe os resultados da detecção de objetos em uma janela com o título "results"
    cv.imshow("results", result[0].plot())

    # Interrompe o loop se a tecla 'q' for pressionada
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Libera o objeto VideoCapture
web_cam.release()

# Fecha todas as janelas abertas pelo OpenCVG
cv.destroyAllWindows()
