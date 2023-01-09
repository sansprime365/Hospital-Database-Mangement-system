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

        b1ttn = Button(self.root,text="Camera for Staff",command=self.face_recog, font=("Arial", 20,"bold"),cursor="hand2",width=20,bg="red",fg="white")
        b1ttn.place(x=500, y=370)

    #===============attendance system============================

    def mark_attendance(self,i,n,r,d):
        with open("attendancestaff.csv","r+",newline="\n") as f:
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

                my_cursor.execute("select rgstrn from staff_data where rgstrn="+str(id))
                k=my_cursor.fetchone()
                k="+".join(k)

                my_cursor.execute("select staffname from staff_data where rgstrn="+str(id))
                p=my_cursor.fetchone()
                p="+".join(p)

                my_cursor.execute("select dept from staff_data where rgstrn="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select age from staff_data where rgstrn="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                if confidence>77:
                    cv2.putText(img,f"regisno:{k}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"staffname:{p}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"dept:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"age:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(k,p,r,d)
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
        clf.read("classifier2.xml")

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
    