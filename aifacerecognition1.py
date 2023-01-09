from tkinter import*
from PIL import Image,ImageTk
import mysql.connector
from datetime import datetime
import cv2

class FaceRecognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1310x730+0+0")
        self.root.title("AI Face recognition and training")

        imgpr1=Image.open(r"D:\IPProjectFinal\backgrounds\v870-mynt-06.jpg")
        imgpr1=imgpr1.resize((1310,735),Image.ANTIALIAS)
        self.photoimgprbg1=ImageTk.PhotoImage(imgpr1)

        bgimg1=Label(self.root,image=self.photoimgprbg1)
        bgimg1.place(x=0,y=0,width=1310,height=735)

        title=Label(bgimg1,text="Face Recognition System",font=("times new roman",35,"bold"),bg="light gray",fg="orange")
        title.place(x=0,y=0,width=1300,height=60)

        b1ttn = Button(self.root,text="Camera for Patients",command=self.face_recog, font=("Arial", 20,"bold"),cursor="hand2",width=20,bg="red",fg="white")
        b1ttn.place(x=500, y=370)

    #===============attendance system============================

    def mark_attendance(self,i,n,r,d):
        with open("attendancepatient.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (r not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{r},{d},{dtString},{d1},Present")


    #=================face recgnition============================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
                my_cursor=conn.cursor()

                my_cursor.execute("select registration from patient_data where registration="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select patientname from patient_data where registration="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select gender from patient_data where registration="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select agegroup from patient_data where registration="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                if confidence>77:
                    cv2.putText(img,f"regisno:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"patientname:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"gender:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"agegroup:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,n,r,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"UNKNOWN FACE!!!",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier1.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("SAGEAIFACEreocgnition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ =="__main__":
    root=Tk()
    obj=FaceRecognition(root)
    root.mainloop()
    