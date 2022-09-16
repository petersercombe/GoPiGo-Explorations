from motor import *
import keyboardController as kc
from time import sleep
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray

# Initialise Keyboard Controller
kc.init()

# Initialise the camera
camera = PiCamera()
# Set size of images to be collected and trained
# If you want a larger image size, use (320, 256) or (640, 512)
imageSize = (160, 128)

rawCapture = PiRGBArray(camera, size=imageSize)
sleep(2)

### NEW ###

# import modules for interacting with the local file system:
import os, sys, datetime
# Set up folders for storing the images in.
currentFolder = os.path.dirname(os.path.realpath(sys.argv[0]))
imagesFolder = currentFolder + '/images_bnw/'
if not os.path.exists(imagesFolder): os.mkdir(imagesFolder) #Create folder if it doesn't exist

###########

for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True, resize=imageSize):
    throttle, steering = kc.main()
    motor(throttle, steering)
    sleep(0.05)
    # Capture image from camera
    image = frame.array
    ### Convert to black and white
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray,(3,3),0)
    bnw = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 13)

    cv2.imshow("Live View", bnw)

    ### NEW ###

    # Save image into steering values folders if driving forwards
    if throttle > 0:
        folder = os.path.join(imagesFolder, str(steering))
        if not os.path.exists(folder): os.mkdir(folder)
        currentDT = datetime.datetime.now()
        filename = os.path.join(folder, currentDT.strftime("%Y-%m-%d %H-%M-%S-%f") + '.jpg')
        cv2.imwrite(filename, bnw)

    ############

    key = cv2.waitKey(1) & 0xFF

    # Clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if 'x' key is pressed, break from the loop.
    if key == ord('x'):
        break

cv2.destroyAllWindows()