import cv2
import time
import threading
import winsound
from pyzbar import pyzbar
from pylibdmtx import pylibdmtx
from FormularioEnvio import SetSerial
from FormularioEnvio import app as Form

video = cv2.VideoCapture(1)
qr_code = cv2.QRCodeDetector()

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    barcodes = pyzbar.decode(frame)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #ret,thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    #pylib_value = pylibdmtx.decode(gray, max_count=1, threshold=50, min_edge=20, max_edge=60)

    #if len(pylib_value) > 0:
    #    result = pylib_value[0].data
    #    result = result.decode()
    #    result = result.replace(",","")
    #    result = result.upper()
    #    winsound.MessageBeep(-1)
    #    print(result)
    #    SetSerial(result)
    #    time.sleep(0.3)
    
    for barcode in barcodes:
        barcode_value = barcode.data.decode("utf-8")
        print("codigo recibido = "+barcode_value)
        winsound.MessageBeep(-1)
        barcode_value = barcode_value.upper()
        SetSerial(barcode_value)
        time.sleep(0.3)
        
        
    Form.update()
    cv2.imshow("Escaner de codigos de barras V1", frame)
    

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()