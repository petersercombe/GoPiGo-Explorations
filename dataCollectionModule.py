from motor import *
import keyboardController as kc
from time import sleep
import os, sys, datetime, cv2
from picamera import PiCamera
from picamera.array import PiRGBArray

# Initialise Keyboard Controller
kc.init()

# Initialise the camera
camera = PiCamera()
# Set size of images to be collected and trained
imageSize = (160, 120)

rawCapture = PiRGBArray(camera, size=imageSize)
sleep(2)

# Set up folders for storing the images in.
currentFolder = os.path.dirname(os.path.realpath(sys.argv[0]))
imagesFolder = currentFolder + '/images/'
if not os.path.exists(imagesFolder): os.mkdir(imagesFolder) #Create folder if it doesn't exist

for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True, resize=imageSize):
    throttle, steering = kc.main()
    motor(throttle, steering)
    sleep(0.05)
    # Capture image from camera
    image = frame.array
    cv2.imshow("Live View", image)
    # Save image into steering values folders
    if throttle > 0:
        folder = os.path.join(imagesFolder, str(steering))
        if not os.path.exists(folder): os.mkdir(folder)
        currentDT = datetime.datetime.now()
        filename = os.path.join(folder, currentDT.strftime("%Y-%m-%d %H-%M-%S-%f") + '.jpg')
        cv2.imwrite(filename, image)

    key = cv2.waitKey(1) & 0xFF

    # Clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if 'x' key is pressed, break from the loop.
    if key == ord('x'):
        break

cv2.destroyAllWindows()