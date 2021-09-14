# Import Pi Camera library
from picamera import PiCamera

from time import sleep
import datetime as dt
import io, keyboard
from PIL import Image

# Import Lobe python library
from lobe import ImageModel

# Import motor controller
from motor import *

# Create a camera object
camera = PiCamera()

# Set size of images - this ideally is the same as the model used to train the images.
imageSize = (160, 128)

# Load Lobe TF Lite model
# --> Change model path
model = ImageModel.load('/home/pi/Desktop/GoPiGo-Explorations/GoPiGov2')

camera.start_preview(alpha=200)
sleep(2)
# Create the in-memory streami


if __name__ == '__main__':

    # Adjust speed factor if your bot is over or under steering.
    speedFactor = 0.8

    while True:
        stream = io.BytesIO()
        camera.capture(stream, format='jpeg', resize=imageSize, use_video_port=True)
        # "Rewind" the stream to the beginning so we can read its content
        stream.seek(0)
        image = Image.open(stream)
        # Run photo through Lobe TF model and get prediction results
        # result = model.predict_from_file('/home/pi/Documents/image.jpg')
        start = dt.datetime.now()
        result = model.predict(image)
        latency = (dt.datetime.now() - start).microseconds
        steering = float(result.prediction)
        # camera.annotate_text = 'Steering:' + result.labels[0][0] + " latency" + str(latency)
        print(result.prediction)
        print(latency)

        motor(speedFactor, steering * speedFactor)

        # Clear the stream in preparation for the next frame
        stream.truncate()
