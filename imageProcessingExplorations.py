def imageProcessing():
    import cv2, os, sys

    folderLocation = os.path.dirname(os.path.realpath(sys.argv[0]))
    images = folderLocation + "/images/"

    for root, dirs, files in os.walk(images):
        for file in files:
            # open image
            filepath = root + os.sep + file
            print (filepath)
            # process image
            img = cv2.imread(filepath, 0) # Reads file in greyscale
            #greyFilePath = root + os.sep + 'grey' + os.sep + file
            #cv2.imwrite(greyFilePath, img)
            blurred = cv2.GaussianBlur(img, (3, 3), 0)

            #_, bnw = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)
            #(T, bnw) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            bnw = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 13)
            bnwFilePath = root + os.sep + 'bnw' + os.sep + file
            print(bnwFilePath)
            cv2.imwrite(bnwFilePath, bnw)

            #cv2.imshow('Live View', bnw)

            #cv2.waitKey(0)


    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        print ("Camera detected")
    else:
        print ("Camera not detected")
    # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, bnw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        # bnw = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 13)

        cv2.imshow('Live View', bnw)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    imageProcessing()