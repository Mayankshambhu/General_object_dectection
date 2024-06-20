'''
pip install opencv-contrib-python
pip install imutils
'''
import cv2
import imutils
#Read an image and display it
#img=cv2.imread("carpixel.net-2022-ferrari-499p-116889-wide.jpg")
#print(img)
#print(img.shape)
#Display the image
#cv2.imshow("Endurance Racing",img)
#we can make to be visable by using waitKey
#cv2.waitKey(5000)#milliseconds
#cv2.waitKey(0)

#Reading image in different flags
#img=cv2.imread("carpixel.net-2022-ferrari-499p-116889-wide.jpg",0)
#img=cv2.imread("carpixel.net-2022-ferrari-499p-116889-wide.jpg",cv2.IMREAD_REDUCED_GRAYSCALE_2)
#cv2.imshow("Endurance Racing",img)
#cv2.waitKey(0)

#Now let's check with the color formats-->cvtColor
#img=cv2.imread("carpixel.net-2022-ferrari-499p-116889-wide.jpg")#original image
#img1=cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb)
#img1=cv2.cvtColor(img,cv2.COLOR_RGBA2GRAY)
#cv2.imshow("Endurance Racing",img1)
#cv2.waitKey(0)

#Rotate an image-->imutils
#img1=imutils.rotate(img,+45)#-ve indicates clockwise,+ve -->anticlockwise
#cv2.imshow("Endurance Racing",img1)
#cv2.waitKey(0)
'''
#you want to read multiple angles at a time
for angle in range(0,360,90):
    #print(angle)
    #rotating the image
    rotated_image=imutils.rotate(img,angle)
    cv2.imshow("Angle=%d"%(angle),rotated_image)
cv2.waitKey(0)
'''
#Adding desired text over the image
#putText is the function which helps to add text over the image
'''
img: The output image .
text: The string of text we'd like to write/draw on the image.
pt:The starting point for the text.
font: I often use the cv2.FONT_HERSHEY_SIMPLEX.
scale: Text color.
thickness: The thickness of the stroke in pixels.


img=cv2.imread("carpixel.net-2022-ferrari-499p-116889-wide.jpg")
img1=img.copy()#take a copy of the image
cv2.putText(img1,"Famous",(10,25),cv2.FONT_HERSHEY_COMPLEX,1.5,(225,65,58),5)
cv2.imshow("Text Output",img1)
cv2.waitKey(0)

#Face Detection in image-->haarcascade classifier

#we will use pretrained cascade classifier along with detectMultiScale()

cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#let's read the image
img=cv2.imread("formula-one-2022-drivers-abu-dhabi-grand-prix-planet-f1.jpg")
#let's add scales and neighbors to be adjusted
faces=cascade.detectMultiScale(img,1.06,9)#need to adjust the scaling
#factors and min neighbors
#print(faces)
#Mark up the coordinates along with width and height to detect face in our image
for(x,y,w,h) in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),5)
    #put the text over the image
    cv2.putText(img,"Hi",(10,25),cv2.FONT_HERSHEY_SIMPLEX,1.25,(0,225,0),5)
#once the above process done
resized=cv2.resize(img,(700,700))
#display the image
cv2.imshow("Final_Output",resized)
cv2.waitKey(0)
'''

#Dectecting face from live webcam
cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#need to pass the source of image #0 for internal webcam,1-->external
cap=cv2.VideoCapture(0)
cap.set(3,640)#set width
cap.set(4,480)#set height
#will run a loop to capture the image and make the rectangle box displayed
while True:
    ret,img=cap.read()
    img=cv2.flip(img,1)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=cascade.detectMultiScale(gray,1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,225,0),2)
        roi_gray=gray[y:y+h,x:x+w]#region of interest
        roi_color=img[y:y+h,x:x+w]
    cv2.imshow('Myself',img)
    k=cv2.waitKey(30)&0xff#0xff is a bit mask which sets the left 24 bits to zero
    #since your keyboard only has a limited character set
    if k==27:#press 'ESC'to quit
        break
cap.release()
cv2.destroyAllWindows()





























