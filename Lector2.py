from pyzbar import pyzbar
import time
import cv2
import os
import numpy as np

def nothing(x):
    pass

print("[INFO] starting video stream...")
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 22)
build = 1
count = True
i=0


time.sleep(2.0)

found = set()
found.clear()



while cv2.waitKey(1) !=27 and cap.isOpened():
    _,frame = cap.read()

    barcodes = pyzbar.decode(frame)


    for barcode in barcodes:

        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)


        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type


        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


        if barcodeData not in found:
            build = build+1
            print('saving')
            cv2.imwrite(os.path.join(str(text) + 'test.jpeg'),frame)
            found.add(barcodeData)

    cv2.imshow("Barcode Scanner", frame)
    key = cv2.waitKey(1) & 0xFF


    if key == ord("q"):
        break


print("[INFO] cleaning up...")
cap.release()
cv2.destroyAllWindows()