# create_database.py
import cv2, sys, numpy, os, time
count = 0
size = 4
fn_haar = 'haarcascade_frontalface_default.xml'
dirr = 'database'
fn_name = input("Enter Name of the person : ")   #name of the person

(im_width, im_height) = (92, 72)
haar_cascade = cv2.CascadeClassifier(fn_haar)
webcam = cv2.VideoCapture(0)
print ("-----------------------Taking pictures----------------------")
print ("--------------------Give some expressions---------------------")
# The program loops until it has 20 images of the face.

model = cv2.face.LBPHFaceRecognizer_create()
try:
    model.read('model.xml')
    i = model.getLabels()[-1][0] + 1
except:
    i = 0
(images, lables, names, id) = ([], [], {}, 0)
print(i)
while count < 10:
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    mini = cv2.resize(gray, (gray.shape[1] // size, gray.shape[0] // size))
    faces = haar_cascade.detectMultiScale(mini)
    faces = sorted(faces, key=lambda x: x[3])
    if faces:
        face_i = faces[0]
        (x, y, w, h) = [v * size for v in face_i]
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (im_width, im_height))
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(im, fn_name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
        images.append(face_resize)
        lables.append(int(i))
        count += 1

    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if cv2.waitKey(5) & 0xFF == ord('q'):
            break

#Create a Numpy array from the two lists above
(images, lables) = [numpy.array(lis) for lis in [images, lables]]

model.update(images, lables)
model.save('model.xml')
