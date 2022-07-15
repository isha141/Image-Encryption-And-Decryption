from  tkinter import *
root=Tk();  


root.geometry("800x600") 
root.resizable(False,False) 
##set background image 
root.backGroundImage=PhotoImage(file="background1.png") 
root.backGroundImageLabel=Label(root,image=root.backGroundImage)  
root.backGroundImageLabel.place(x=0,y=0)  

## Set template inside Gui

root.canvas=Canvas(root,width=600,height=330) 
root.canvas.place(x=150,y=100)
root.title=Label(root,text="Image Encryption And Decryption",font="comicsansms 13 bold ")
root.title.place(x=300,y=80) 
      
##Encryption 
def on_encrypt():  
   #  print("With labels ")
    print(f"Path Enterd by the user   {pathvalue.get()}")
    print(f"Emails Enterd by the user {emailvalue.get()}")
    print(f"Key enterd by the user    {keysvalue.get()}")
    k=int(keysvalue.get())  
    
    
     #open file in read mode  
    fin = open(pathvalue.get(), 'rb')
    image = fin.read() 
    fin.close() 
     
     ##converted into bytearary 
    image = bytearray(image) 
    for index, values in enumerate(image):
        image[index] = values ^ k 
     
     ##overide the encrypted values into orginal data 
    fin = open(pathvalue.get(), 'wb')
    fin.write(image)
    fin.close()  
    
    print("Encryption Succesfulll !!!!!")

##Decryption 

def on_decrypt(): 
     
    print(f"Path Enterd by the user   {pathvalue.get()}")
    print(f"Emails Enterd by the user {emailvalue.get()}")
    print(f"Key enterd by the user    {keysvalue.get()}") 
    k=int(keysvalue.get()) 
    
     ##open file in read mode 
    fin = open(pathvalue.get(), 'rb')
    image = fin.read()
    fin.close()
      
     ##convertedinto byteaarary 
    image = bytearray(image)
    for index, values in enumerate(image):
        image[index] = values ^ k
 
    ##overide the decrypted values in  orginal data 
    fin = open(pathvalue.get(), 'wb')
     
    fin.write(image)
    fin.close()
    print("Decryption Succesfulll !!!!!")
   

#GUI 
##createc labels
# Label(root,text="Image Encryption And Decryption",font="comicsansms 13 bold " ,pady=30).grid(row=5,column =3)
email=Label(root,text="Enter  Email Address ")
path=Label(root,text="Enter Image Path ")
keys=Label(root,text="Enter Secret Key ") 

##create pack
email.place(x=200,y=150)   
path.place(x=200,y=200)
keys.place(x=200,y=250) 

##store values
emailvalue=StringVar()
pathvalue=StringVar()
keysvalue=StringVar()
 
 
###Entry  
entry=Entry(root,textvariable="hyy")
emailentry=Entry(root,textvariable=emailvalue)
pathentry=Entry(root,textvariable=pathvalue)
keysentry=Entry(root,textvariable=keysvalue)
 
# Pack Entry GRID 
emailentry.place(x=320,y=155,width=240,height=20) 
pathentry.place(x=320,y=205,width=240,height=20)
keysentry.place(x=320,y=255,width=240,height=20)  


#Creating Buttons 
button=Button(root,text="Encryption ",command=on_encrypt) 
button.place(x=320,y =305) 
button1=Button(root,text="Decryption ",command=on_decrypt)
button1.place(x=320,y =355) 

root.mainloop() 