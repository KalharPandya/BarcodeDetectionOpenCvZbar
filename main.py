from pyzbar import pyzbar
import cv2
import time
import datetime
from datetime import datetime
# cap = cv2.VideoCapture(0) 
# _, image = cap.read()
image = cv2.imread("fix.png")
height, width, layers = image.shape
size = (width,height)
print(size)
out = cv2.VideoWriter(str(datetime.now())+'.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         20, size)
fps = 20
ptime = time.time()
while True:
    # _, image = cap.read()
    image = cv2.imread("fix.png")

    barcodes = pyzbar.decode(image)
   
    for barcode in barcodes:
        
        (x, y, w, h) = barcode.rect
        if w < 10: w = 100
        if h < 10: w = 100
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y-20), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (45, 45, 0), 2)
        print("[INFO] Found {} barcode: {}".format(
            barcodeType, barcodeData))
    
    cv2.putText(image, "FPS: "+str(fps), (width - 100, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (45, 45, 0), 2)
    cv2.imshow("Image", image)
    out.write(image)
    fps = round(1/(time.time() - ptime))
    ptime = time.time()
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()