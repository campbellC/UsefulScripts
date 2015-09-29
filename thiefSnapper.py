# This script takes photo with the webcam on the computer and stores it in your
# Dropbox. You must change the filename to suit your computer!
# Set this up with launchd to run everytime your computer turns on to have a
# chance of catching images of someone who has stolen your computer. This is a
# huge privacy violation so do it at your own risk!

import time
import cv2

# We store the file with the current date and time so we can automate cleaning
# up of old snaps
currentTime = time.strftime("%d:%m:%Y-%H:%M:%S")
filename = "/Users/chrisCampbell/Dropbox/securityPhotos/" + currentTime + ".png"


# opencv2 allows capture of images from webcam
vidcap = cv2.VideoCapture()
vidcap.open(0)
time.sleep(1)
retval,image = vidcap.read()
vidcap.release()
cv2.imwrite(filename,image)

