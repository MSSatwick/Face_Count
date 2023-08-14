import cv2
cap= cv2.VideoCapture(0)
# reading the input using the camera
result, image = cap.read()
if result:
    facedetector=cv2.CascadeClassifier('E:\python codes\Face Detect\haarcascades\haarcascade_frontalface_default.xml')
    face=facedetector.detectMultiScale(image,1.1,5)
    
    for x,y,z,h in face:
        cv2.rectangle(image,(x,y),(x+z,y+h),(0,0,225),3)
        cv2.putText(image,"Detected", (x+50, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 225), 2)
 
    cv2.imshow("facedetective",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('Number of faces:',len(face))
else:
    print("Please try again")
