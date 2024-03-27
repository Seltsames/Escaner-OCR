import cv2
import time
import threading
import winsound
from pyzbar import pyzbar 
from FormularioEnvio import SetSerial
from FormularioEnvio import app as Form

video = cv2.VideoCapture(1)

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    barcodes = pyzbar.decode(frame)
    winsound.MessageBeep(-1)

    for barcode in barcodes:
        barcode_value = barcode.data.decode("utf-8")
        print("codigo recibido = "+barcode_value)
        
        SetSerial(barcode_value)
        time.sleep(0.3)
        
        
    Form.update()
    cv2.imshow("Escaner de codigos de barras V1", frame)
    

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()