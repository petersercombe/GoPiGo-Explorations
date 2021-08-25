from lobe import ImageModel
import io
import time
import picamera
from PIL import Image

model = ImageModel.load('path/to/exported/model')

# Create the in-memory stream
stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture(stream, format='jpeg')
# "Rewind" the stream to the beginning so we can read its content
stream.seek(0)
image = Image.open(stream)

# Predict from Pillow image
result = model.predict(image)

# Print top prediction
print("Top prediction:", result.prediction)

# Print all classes
for label, confidence in result.labels:
    print(f"{label}: {confidence*100:.6f}%")