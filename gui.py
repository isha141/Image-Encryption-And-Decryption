from  tkinter import *
root=Tk();  
root.geometry("700x500") 


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
Label(root,text="Image Encryption And Decryption",font="comicsansms 13 bold " ,pady=30).grid(row=5,column =3)
email=Label(root,text="Enter  Email Address ")
path=Label(root,text="Enter Image Path ")
keys=Label(root,text="Enter Secret Key ") 

##create pack
email.grid(row=15,column=2)   
path.grid(row=20,column=2)
keys.grid(rows=20,column=2) 

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
emailentry.grid(row=15,column=3) 
pathentry.grid(row=20,column=3)
keysentry.grid(row=25,column=3)  


Button(root,text="Encryption ",command=on_encrypt).grid(row=30,column =3) 
Button(root,text="Decryption ",command=on_decrypt).grid(row=35,column =3) 



root.mainloop() 