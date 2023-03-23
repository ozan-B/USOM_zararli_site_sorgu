from tkinter import *
import datetime

def kontrol_et():
     dosya = open("usom.txt","r")
     icerik = dosya.read()
     dosya.close()
     URL = entry1.get()
     bugun= datetime.datetime.now()
     if str(URL) in icerik:
         dosya=open("log.txt","a")
         yazi=str(URL)+ "zararli\nTarih:"+str(bugun)+"\n"
         dosya.write(yazi)
         dosya.close()
         
         v.set("URL zararlidir")
         
     else:
         dosya=open("log.txt","a")
         yazi=str(URL)+ "zararli degildir\nTarih:"+str(bugun)+"\n"
         dosya.write(yazi)
         dosya.close()
         
         v.set("URL zararli degil ")


top =Tk()
top.title("USOM IP Kontrol") 
top.minsize(450,400)
top.maxsize(550,500)
top.resizable(False,False)


label1=Label(top,text="Kontrol Edilecek URL adresini giriniz:",bg="gray",fg="blue",font=("Times",17,"bold"))
label1.pack()


entry1= Entry(top)
entry1.place(x=40,y=100)
entry1.pack()

v=StringVar()

entry2=Entry(top,textvariable=v)
entry2.place(x=50,y=200)
entry2.pack()


B=Button(top,text="Kontrol Et" ,bg="green",fg="black",command=kontrol_et,font=("Arial",14))   
B.place(y=80)
B.pack()

top.mainloop()

        

         
     
