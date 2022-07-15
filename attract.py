from  tkinter import *

# def on_encrypt():  
#    #  print("With labels ")
#     print(f"Path Enterd by the user   {pathvalue.get()}")
#     print(f"Emails Enterd by the user {emailvalue.get()}")
#     print(f"Key enterd by the user    {keysvalue.get()}")
#     k=int(keysvalue.get())  
    
    
#      #open file in read mode  
#     fin = open(pathvalue.get(), 'rb')
#     image = fin.read() 
#     fin.close() 
     
#      ##converted into bytearary 
#     image = bytearray(image) 
#     for index, values in enumerate(image):
#         image[index] = values ^ k 
     
#      ##overide the encrypted values into orginal data 
#     fin = open(pathvalue.get(), 'wb')
#     fin.write(image)
#     fin.close()  
    
#     print("Encryption Succesfulll !!!!!")


# def on_decrypt(): 
   
     
#     print(f"Path Enterd by the user   {pathvalue.get()}")
#     print(f"Emails Enterd by the user {emailvalue.get()}")
#     print(f"Key enterd by the user    {keysvalue.get()}") 
#     k=int(keysvalue.get()) 
    
    
#      ##open file in read mode 
#     fin = open(pathvalue.get(), 'rb')
#     image = fin.read()
#     fin.close()
      
#      ##convertedinto byteaarary 
#     image = bytearray(image)
#     for index, values in enumerate(image):
#         image[index] = values ^ k
 
#     ##overide the decrypted values in  orginal data 
#     fin = open(pathvalue.get(), 'wb')
     
#     fin.write(image)
#     fin.close()
#     print("Decryption Succesfulll !!!!!")
   

class login(Tk):
   def __init__(self):
      super().__init__()
      self.geometry("800x600")
      self.resizable(False,False)
   def Label(self):
      self.backGroundImage=PhotoImage(file="background_img.png") 
      self.backGroundImageLabel=Label(self,image=self.backGroundImage)  
      self.backGroundImageLabel.place(x=0,y=0) 
   
      self.canvas=Canvas(self,width=600,height=330) 
      self.canvas.place(x=100,y=100)
      self.title=Label(self,text="Image Encryption And Decryption",font="comicsansms 13 bold ")
      self.title.place(x=300,y=80) 
      
      
      self.email=Label(self,text="Email Address ") 
      self.email.place(x=200,y=150) 
      
      self.path=Label(self,text="Image Path ") 
      self.path.place(x=200,y=200) 
      self.keys=Label(self,text="Secret Key ")  
      self.keys.place(x=200,y=250)
       
       
       
   def Entry(self):
         self.email=Text(self,borderwidth=0,highlightthicknes=0,width=30,height=1)
         self.email.place(x=320,y=155)
         
         
         self.path=Entry(self,borderwidth=0,highlightthickness=0)
         self.path.place(x=320,y=205,width=240,height=20)
         path1=self.path.get()
         print("heloo"+ path1)
         
         self.keys=Entry(self,borderwidth=0,highlightthickness=0)
         self.keys.place(x=320,y=255,width=240,height=20) 
         self.data=insert(250,)
          
          
         self.button=Button(self,text="Encryption ") 
         self.button.place(x=320,y=300,width=250,height=50)
         # Button(root,text="Decryption ",command=on_decrypt)
   

if __name__=="__main__":
   Login=login()
   Login.Label() 
   Login.Entry()
   Login.mainloop() 
