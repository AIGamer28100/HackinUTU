# facerec.py
import cv2, sys, numpy, os, time
size = 4
fn_haar = 'haarcascade_frontalface_default.xml'
fn_dir = 'database'
haar_cascade = cv2.CascadeClassifier(fn_haar)
def pathdir(fn_nam):
    path = os.path.join(fn_dir, fn_nam)
    if not os.path.isdir(path):
        os.mkdir(path)

(im_width, im_height) = (200, 175)

#OpenCV trains a model from the images
model = cv2.face.LBPHFaceRecognizer_create()
model.read('model.xml')

# Part 2: Use LBPHRecognizer on camera stream
face_cascade = cv2.CascadeClassifier(fn_haar)
webcam = cv2.VideoCapture(0)
count=0
while True:
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.7,
        minNeighbors=2,
        minSize=(50, 50)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )
    star=time.time()
    for (x,y,w,h) in faces:
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (im_width, im_height))
        # Try to recognize the face
        prediction = model.predict(face_resize)
        cv2.rectangle(im, (x, y), (x + w+10, y + h+10), (0, 255, 0), 2)

        if prediction[1]<=120 and prediction[1]>=40:
            print(prediction[0])
    cv2.imshow('..Facial Recogonision..', im)
    if cv2.waitKey(5) & 0xFF == ord('q'):
            break
