# Import Pi Camera library
import cv2
from time import sleep

#Import Lobe python library
from lobe import ImageModel

# Create a camera object
cap = cv2.VideoCapture(0)

# Load Lobe TF Lite model
# --> Change model path
model = ImageModel.load('C:/Users/peter.sercombe/OneDrive - Bundaberg Christian College/@ 10 Digital Tech/2021/Term 3/DrinkingNotDrinking model/Drinking Vs. Not Drinking TFLite')

while True:
    ret, frame = cap.read()

    # Temporarily write the frame to disc and open as stream
    img = cv2.resize(frame, (200, 66))
    cv2.imwrite('img.png', img)
    # imageData = open('frame.png', "rb")

    # Run photo through Lobe TF model and get prediction results
    result = model.predict_from_file('img.png')
    # result = model.predict(frame)

    print(result.labels)

    cv2.putText(frame, text=result.labels[0][0], org=(30, 30),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.6, color=(0, 0, 0),
                thickness=2, lineType=cv2.LINE_AA)

    cv2.imshow('frame', frame)

    # sleep(1)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()