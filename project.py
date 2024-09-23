import face_recognition
import numpy as np
import cv2 
import pandas as pd
import csv
import os
import pyttsx3 #speech
from datetime import datetime
from collections import deque
import time

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.popleft()
    
    def peek(self):
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
        
    def size(self):
        return len(self.items)
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []   
    def top(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items
files= Stack()
student1 = Queue()
roll_num1 = Queue()

video_capture = cv2.VideoCapture(0)
#BTS
Namjoon = face_recognition.load_image_file("pictures/namjoon.jpeg")
Namjoon_encoding = face_recognition.face_encodings(Namjoon)[0]
Jin = face_recognition.load_image_file("pictures/jin.jpeg")
Jin_encoding = face_recognition.face_encodings(Jin)[0]
Suga = face_recognition.load_image_file("pictures/suga.jpeg")
Suga_encoding = face_recognition.face_encodings(Suga)[0]
J_hope = face_recognition.load_image_file("pictures/jhope.jpeg")
J_hope_encoding = face_recognition.face_encodings(J_hope)[0]
Jimin = face_recognition.load_image_file("pictures/jimin.jpeg")
Jimin_encoding = face_recognition.face_encodings(Jimin)[0]
V = face_recognition.load_image_file("pictures/v.jpeg")
V_encoding = face_recognition.face_encodings(V)[0]
Jungkook = face_recognition.load_image_file("pictures/jk.jpeg")
Jungkook_encoding = face_recognition.face_encodings(Jungkook)[0]

# random
billgates= face_recognition.load_image_file("pictures/billgates.jpeg")
bill_encoding = face_recognition.face_encodings(billgates)[0]

imran = face_recognition.load_image_file("pictures/imran.jpeg")
imran_encoding = face_recognition.face_encodings(imran)[0]

#CS_02
LBK = face_recognition.load_image_file("pictures/lbk.jpeg")
LBK_encoding = face_recognition.face_encodings(LBK)[0]

Tashfeen = face_recognition.load_image_file("pictures/tashfeen.jpeg")
Tashfeen_encoding = face_recognition.face_encodings(Tashfeen)[0]

maham = face_recognition.load_image_file("pictures/maham.jpeg")
maham_encoding = face_recognition.face_encodings(maham)[0]

zainab = face_recognition.load_image_file("pictures/zainab.jpeg")
zainab_encoding = face_recognition.face_encodings(zainab)[0]

#zinirah = face_recognition.load_image_file("pictures/zinirah.jpeg")
#zinirah_encoding = face_recognition.face_encodings(zinirah)[0]

Amna = face_recognition.load_image_file("pictures/amna.jpeg")
Amna_encoding = face_recognition.face_encodings(Amna)[0]

sundas = face_recognition.load_image_file("pictures/sundas.jpeg")
sundas_encoding = face_recognition.face_encodings(sundas)[0]

laiba = face_recognition.load_image_file("pictures/laiba.jpeg")
laiba_encoding = face_recognition.face_encodings(laiba)[0]

#laiba_ehsan = face_recognition.load_image_file("pictures/laiba_ehsan.jpeg")
#laiba_ehsan_encoding = face_recognition.face_encodings(laiba_ehsan)[0]

#LIST :
known_face_encoding = [bill_encoding, imran_encoding,  LBK_encoding, Tashfeen_encoding, Amna_encoding,zainab_encoding ,maham_encoding ,sundas_encoding,laiba_encoding,
                       Namjoon_encoding, Jin_encoding, Suga_encoding, J_hope_encoding, Jimin_encoding, V_encoding, Jungkook_encoding]

known_face_names = ["Bill Gates", "Imran Khan" , "Laraib","Tashfeen", "Amna","Zainab","Maham", "Sundas","Laiba",
                    "Kim Namjoon", "Kim SeokJin", "Min Yoongi", "Jung HoSeok", "Park Jimin", "Kim Taehyung", "Jeon Jungkook"]
dept_cs_rollno = ['2102010098', '210201067', '210201001', '210201004', '210201005', '210201006', '210201007','210201008', '210201002', '210201010', '210201011',
                  '210201012', '210201013', '210201014', '210201015', '210201016']
# department CS_02
dept_cs= ["Laraib","Tashfeen","Amna","Zainab","Maham","Sundas","Laiba"]

dept_ee=[ "Imran Khan","Kim Namjoon", "Kim SeokJin", "Min Yoongi", "Jung HoSeok", "Park Jimin", "Kim Taehyung", "Jeon Jungkook"]

students = known_face_names.copy()
roll_num = dept_cs_rollno.copy()
face_locations =[]
face_encodings = []
face_names = []

s = True

# date -- time 
now = datetime.now()

current_date = now.strftime("%m-%d-%Y")
f1 = open(current_date +" CS" + '.csv', 'w+' , newline = '')
f2 = open(current_date +" EE" + '.csv', 'w+' , newline = '')

lnwriter1= csv.writer(f1)
lnwriter1.writerow(["Roll Number", "Name","Time","Department","Attendence"])

lnwriter2= csv.writer(f2)
lnwriter2.writerow(["Roll Number", "Name","Time","Department","Attendence"])

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") 
while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx = 0.25, fy=0.25 ) 
    rgb_small_frame = small_frame[:,:, ::-1]
    frame =frame.copy()

    # Detect the faces
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces  = face_cascade.detectMultiScale(image=gray, scaleFactor=1.5, minNeighbors=5 )
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (188,143,143), 2)
    
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        
        # Loop through each face found in the unknown image (for face_encoding in face_encodings:)
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            # if variable not initialized : garbage value
            name =''
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)
            
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                roll = dept_cs_rollno[best_match_index]

                ## Voice Output :
                speech_=pyttsx3.init()
                if (cv2.waitKey(1) & 0xFF == ord('s')):
                    l=[]
                    if name in known_face_names and name not in l:
                        speech_.say(str(name)+" is Present")
                        speech_.runAndWait()
                        #speech.say(str(name)+" is Present")
                        l.append(name)
                    else:
                        speech_.say("Attendence Already Marked")
                    break

                #y,x,h,w=face_locations[0],face_locations[1],face_locations[2],face_locations[3]
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (188,143,143), 2)
          
                    frame= cv2.putText(img = frame,text = name, org = (x,y-10), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1.5, color = (188,143,143),  thickness = 1)

            face_names.append(name)
             # if face matches to the listed people
            if name in  known_face_names:
                if name in students:
                    students.remove(name)
                    roll_num.remove(roll)
                    
                    current_time = time.strftime("%H:%M:%S")
                    if name in dept_cs :  # if person beolongs to CS_02
                        lnwriter1.writerow([roll, name,  current_time , 'Cs_02',"P"])
                    else:
                        lnwriter2.writerow([roll, name, current_time, 'EE_02',"P"]) 
            
            students1= students.copy()  
            for i in range(len(students1)):
                student1.enqueue(students1[i])
                roll_num1.enqueue(roll_num[i]) 
                              
                   
    cv2.imshow("Attendance System  *_*", frame)

   # cv2.waitKey(1) : get a continuous live video feed from my laptops webcam
   #cv2.waitKey(0) :  get still images

    if (cv2.waitKey(1) & 0xFF == ord('l')):
        for i  in range(len(students)):

            # absent students are enqueued in the frame and after exit ing the frame they are
            # dequeued and there name is added into csv file with ' A '
            stdname = student1.dequeue()
            rnum = roll_num1.dequeue()
            if stdname in students1:
                if  stdname in dept_cs :  # if person beolongs to CS_02
                    current_time = time.strftime("%H:%M:%S")
                    lnwriter1.writerow([rnum,stdname ,current_time, 'Cs_02',"A"]) 
                elif stdname in dept_ee:
                    current_time = time.strftime("%H:%M:%S")
                    lnwriter2.writerow([rnum,stdname, current_time, 'EE_02',"A"]) 
        break
    class_timing='19:46:00'
    #elif str(current_time)==str(class_timing):
    #break


# Displaying
video_capture.release()
cv2.destroyAllWindows()
import pandas as pd


f1.close()
f2.close()

df = pd.read_csv(current_date +" CS" + '.csv')
sorted_df = df.sort_values(by=["Roll Number"], ascending=True)
sorted_df.to_csv(current_date +" CS" + '.csv', index=False)

df = pd.read_csv(current_date +" EE" + '.csv')
sorted_df = df.sort_values(by=["Roll Number"], ascending=True)
sorted_df.to_csv(current_date +" EE" + '.csv', index=False)


files1 = Stack()

files.push(current_date +" CS")
files1.push(current_date +" EE")                              