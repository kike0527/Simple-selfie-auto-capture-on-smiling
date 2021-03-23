#Import out computer vision library.
import cv2
#Set video source.
video = cv2.VideoCapture(0)
#Initialize classifiers (for both face and smile detection).
faceCascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
smileCascade = cv2.CascadeClassifier("cascades/haarcascade_smile.xml")
#Start reading video stream.
while True:
    #Read next frame.
    _,img = video.read()
    #Convert image to grayscale
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Detect faces on image
    faces = faceCascade.detectMultiScale(grayImg,1.1,4)
    keyPressed = cv2.waitKey(1)
    #Iterate over found face(s) on image.
    for x,y,w,h in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),3)
        #Detect smile.
        smiles = smileCascade.detectMultiScale(grayImg,1.8,15)
        #Iterate over smiles
        for x,y,w,h in smiles:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(100,100,100),5)
            print("Image "+str(cnt)+"Saved")
            path=r'C:SOURCE\TO\STORE\IMAGE'+str(cnt)+'.jpg'
            #Write image to disk.
            cv2.imwrite(path,img)
            #Go back to detect smile(s) on face(s).
            break
    #Show current frame.   
    cv2.imshow('live video',img)
    #Exit the process when 'q' is pressed.
    if(keyPressed & 0xFF==ord('q')):
        break
#Release resources before finishing.
video.release()                                  
cv2.destroyAllWindows()
