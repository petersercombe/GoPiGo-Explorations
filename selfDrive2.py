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
    speedFactor = 0.8

    for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True, resize=imageSize):
        # while True:
        # stream = io.BytesIO() # Capture image to an in-memory stream
        # camera.capture(stream, format='jpeg', resize=imageSize, use_video_port=True)
        # "Rewind" the stream to the beginning so we can read its content
        # stream.seek(0)
        image = frame.array

        start = dt.datetime.now()  # Capture start time
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # image = Image.open(stream).convert('L') # .convert('L') opens the image as greyscale

        # Apply slight blur to image to soften edges
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        # Convert to binary black and white using adaptive threshold method
        bnw = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 13)

        img = Image.fromarray(bnw, 'L')

        # Run photo through Lobe TF model and get prediction results

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
        # stream.truncate()
        rawCapture.truncate(0)

        key = cv2.waitKey(1) & 0xFF

        # if 'x' key is pressed, break from the loop.
        if key == ord('x'):
            break

    cv2.destroyAllWindows()
    motor(0, 0)
