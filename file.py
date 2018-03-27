# import the necessary packages
import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2
 
# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

# Set relay pins as output
GPIO.setup(9, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

# Turn all relays OFF
GPIO.setup(9, GPIO.LOW)
GPIO.setup(18, GPIO.LOW)
GPIO.setup(11, GPIO.LOW)
GPIO.setup(17, GPIO.LOW)
GPIO.setup(27, GPIO.LOW)
GPIO.setup(10, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)

upperbody_cacade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    img = frame.array
    count = 0
   
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    upperbody = upperbody_cacade.detectMultiScale(gray, 1.1, 1)
    for (x,y,w,h) in upperbody:
        print (str(x)+ ' '+ str(y) + ' '+str(w)+ ' '+str(h))
        print()
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        if (x >= 51 and x <= 542) and (y >= 269 and y <= 298) and (w >= 59 and w <= 122) and (h >= 39 and h <= 100):
            print ("1st fan")
        count += 1;
   
    print (count)
   
    if (count == 1):
        GPIO.setup(18, GPIO.HIGH)
    elif (count == 2):
        GPIO.setup(18, GPIO.HIGH)
        GPIO.setup(23, GPIO.HIGH)
    elif (count == 3):
        GPIO.setup(18, GPIO.HIGH)
        GPIO.setup(23, GPIO.HIGH)
        GPIO.setup(17, GPIO.HIGH)
    elif (count == 4):
        GPIO.setup(18, GPIO.HIGH)
        GPIO.setup(23, GPIO.HIGH)
        GPIO.setup(17, GPIO.HIGH)
        GPIO.setup(27, GPIO.HIGH)
    elif (count == 5):
        GPIO.setup(18, GPIO.HIGH)
        GPIO.setup(23, GPIO.HIGH)
        GPIO.setup(17, GPIO.HIGH)
        GPIO.setup(27, GPIO.HIGH)
        GPIO.setup(22, GPIO.HIGH)
    elif (count == 6):
        GPIO.setup(18, GPIO.HIGH)
        GPIO.setup(23, GPIO.HIGH)
        GPIO.setup(17, GPIO.HIGH)
        GPIO.setup(27, GPIO.HIGH)
        GPIO.setup(22, GPIO.HIGH)
        GPIO.setup(10, GPIO.HIGH)
    elif (count == 7):
        GPIO.setup(18, GPIO.HIGH)
        GPIO.setup(23, GPIO.HIGH)
        GPIO.setup(17, GPIO.HIGH)
        GPIO.setup(27, GPIO.HIGH)
        GPIO.setup(22, GPIO.HIGH)
        GPIO.setup(10, GPIO.HIGH)
        GPIO.setup(9, GPIO.HIGH)
    elif (count == 8):
        GPIO.setup(18, GPIO.HIGH)
        GPIO.setup(23, GPIO.HIGH)
        GPIO.setup(17, GPIO.HIGH)
        GPIO.setup(27, GPIO.HIGH)
        GPIO.setup(22, GPIO.HIGH)
        GPIO.setup(10, GPIO.HIGH)
        GPIO.setup(9, GPIO.HIGH)
        GPIO.setup(11, GPIO.HIGH)
   
    sleep(5)

    # show the frame
    cv2.imshow("Frame", img)
    key = cv2.waitKey(1) & 0xFF
 
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
 
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
