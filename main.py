from socket import timeout
from tkinter import *
from tkinter import messagebox
from plyer import notification
import time



if __name__ == "__main__":


# making of the GUI 
  gui = Tk()
  gui.title("TIM")
  gui.geometry("500x500")
  gui.config(background="whitesmoke")
  gui.resizable(0,0)


# # making function for ferring detials
  def get_detials():
      get_title = title.get()
      get_message = message.get()
      get_time = interval.get()
      get_method = select.get()
      
      if get_title == "" or get_message == "" or get_time == "" or get_method == "":
          messagebox.showerror("Warning", "All fields are required!!!")
      else:
          int_time = int(float(get_time))
          min_to_sec = 60 * int_time
          int_method = int(get_method)
          messagebox.showinfo("Notifier SET", "Show Notification ?")
          gui.destroy()
  
      
      if int_method == 1:
        time.sleep(min_to_sec)
        notification.notify( title=get_title, message=get_message, app_icon="clock.ico", app_name="TIM", timeout=5)  
      elif int_method == 2:
        while True:
          notification.notify( title=get_title, message=get_message, app_icon="clock.ico", app_name="TIM", timeout=5)
          time.sleep(min_to_sec)
          
      
        

  

  #Lable 0 App Name
  gui_lable0 = Label(gui, text='''TIME IS MONEY''', font="Bodoni_MT 15 bold", bg="azure4",height=2,width=500,fg="black")
  gui_lable0.pack()

  #Lable 1
  gui_lable1 = Label(gui, text="Title of Notification", font="Serif 12 ", bg="whitesmoke", fg="black")
  gui_lable1.place(x=20,y=60)
    #entry 1
  title = Entry(gui, width=50, font="Ariel 12 italic", bg="white")
  title.place(x=20,y=90)

  #Lable 2
  gui_lable2 = Label(gui, text="Display Message", font="Serif 12 ", bg="whitesmoke", fg="black")
  gui_lable2.place(x=20,y=130)
    #entry 2
  message = Entry(gui, width=50, font="Ariel 12 italic", bg="white")
  message.place(x=20,y=160)


  #Lable 3
  gui_lable3 = Label(gui, text="Set Time Interval", font="Serif 12 ", bg="whitesmoke", fg="black")
  gui_lable3.place(x=20,y=200)
    #entry 3
  interval = Entry(gui, width=15, font="Ariel 12 bold", bg="white")
  interval.place(x=20,y=230)
    #time unit
  unit = Label(gui, text="(minutes)", font="Serif 8 italic", bg="whitesmoke", fg="black")
  unit.place(x=165,y=234)

  #Lable 4
  gui_lable4 = Label(gui, text="Please Type", font="Serif 12 ", bg="whitesmoke", fg="black")
  gui_lable4.place(x=20,y=274)
    #LIST
  listItem1 = Label(gui, text="1 for Onetime Notification", font="Serif 11 italic", bg="whitesmoke", fg="black")
  listItem1.place(x=30,y=304)
  listItem2 = Label(gui, text="2 for Loop", font="Serif 11 italic", bg="whitesmoke", fg="black")
  listItem2.place(x=30,y=324)
    #entry 4
  select = Entry(gui, width=5, font="Ariel 12 ", bg="white")
  select.place(x=30,y=354)

  #submit button
  submit = Button(gui, text="SET REMINDER !!", bg="lightblue", font="Ariel 14 ", width=40, command= get_detials)
  submit.place(x=25,y=404)

  #Signature
  signature = Label(gui, text="-Gyanendra Tiwari", bg="whitesmoke", font="Forte 12", fg="cornsilk4")
  signature.place(x=350,y=460)



  gui.mainloop()
