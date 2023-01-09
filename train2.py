from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1310x730+0+0")
        self.root.title("Image recognition and training")

        imgpr1=Image.open(r"D:\IPProjectFinal\backgrounds\v870-mynt-06.jpg")
        imgpr1=imgpr1.resize((1310,735),Image.ANTIALIAS)
        self.photoimgprbg1=ImageTk.PhotoImage(imgpr1)

        bgimg1=Label(self.root,image=self.photoimgprbg1)
        bgimg1.place(x=0,y=0,width=1310,height=735)

        title=Label(bgimg1,text="Image Recognition And Training",font=("times new roman",35,"bold"),bg="light gray",fg="orange")
        title.place(x=0,y=0,width=1300,height=60)

        b1ttn = Button(self.root,text="Train Data", font=("Arial", 20,"bold"),command=self.train_classifier,cursor="hand2",width=20,bg="red",fg="white")
        b1ttn.place(x=500, y=370)

    def train_classifier(self):
        data_dir=("datastaff")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #for gray scale images recorded
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #============train the classifier for face training================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier2.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Image Training Completed!")

if __name__ =="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()