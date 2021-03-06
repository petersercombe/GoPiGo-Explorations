# Import Pi Camera library
from picamera import PiCamera
from picamera.array import PiRGBArray

from time import sleep
import datetime as dt
import io, cv2
from PIL import Image

# Import Lobe python library
from lobe import ImageModel

# Import motor controller
from motor import *

# Create a camera object
camera = PiCamera()

# Set size of images - this ideally is the same as the model used to train the images.
imageSize = (160, 128)

rawCapture = PiRGBArray(camera, size=imageSize)
sleep(2)

# Load Lobe TF Lite model
# --> Change model path
model = ImageModel.load('/home/pi/Desktop/GoPiGo-Explorations/GPGv4.1')

# camera.start_preview(alpha=200)
sleep(2)
# Create the in-memory streami


if __name__ == '__main__':

    # Adjust speed factor if your bot is over or under steering.
    speedFactor = 1
    steering = 0

    for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True, resize=imageSize):
        start = dt.datetime.now()  # Capture start time of the loop

        image = frame.array
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Apply slight blur to image to soften edges
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        # Convert to binary black and white using adaptive threshold method
        bnw = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 13)

        # Convert to a PIL format for model
        img = Image.fromarray(bnw, 'L')

        # Perform model prediction
        result = model.predict(img)
        latency = (dt.datetime.now() - start).microseconds  # Capture time difference
        steering = float(result.prediction)
        # camera.annotate_text = 'Steering:' + result.labels[0][0] + " latency" + str(latency)
        print(result.prediction)
        print(latency)

        cv2.imshow("Live View", bnw)

        motor(speedFactor, steering * speedFactor)

        # Clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        key = cv2.waitKey(1) & 0xFF

        # if 'x' key is pressed, break from the loop.
        if key == ord('x'):
            break

    cv2.destroyAllWindows()
    motor(0, 0)
