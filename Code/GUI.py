# Create GUI
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from ChatRead import chatbot_response, but_scan

def sendText():
    per_msg = box_send.get(1.0,END).strip()
    box_send.delete(0.0,END)
    box_rel.config(state=NORMAL)
    if not per_msg:
        res = "Please try sending again ! Thank you !"
    elif per_msg == "hello" :
        res = "Hello there!"
    else:
        msg = but_scan(per_msg)
        res = chatbot_response(msg)
    box_rel.insert(END," You: " + per_msg +"\n\n" )
    box_rel.insert(END," Bot: " + res +"\n\n" )
    box_rel.config(state=DISABLED)
    box_rel.yview(END)

# create values of GUI
Bot_name = "PROPOSED"
BG_GUI = "E:/ChatBox/Proposed/images/Chatbot_bg.png"
BG_send = "E:/ChatBox/Proposed/images/sendbtn.png"

# create window 
chatbot = tk.Tk()
chatbot.title("CHATBOT SYSTEM")
chatbot.iconbitmap("E:/ChatBox/Proposed/images/Chatbot_icon.ico")

chatbot.resizable(width=False, height=False)
chatbot.configure(width=500, height=650)

load_bg = Image.open(BG_GUI)
img_bg = ImageTk.PhotoImage(load_bg)
img = Label(chatbot, image = img_bg)
img.place(x = 0, y = 0 )

# head label
name_sys = Label(chatbot, text = Bot_name, fg = "#000000", bd = 0, bg = "#DFFFFF")
name_sys.config(font=("Bookman Old Style",25,"bold"))
name_sys.place(y = 10, x = 155)

# box message
box_rel = Text(chatbot, width = 43, height = 21,font= ("Arial",14), bd = 1, bg = "#FAFAFA") #ECECEC  ,F5F5F5 , DEDEDE or D4D4D4
box_rel.place(y = 65, x = 11)
box_rel.config(state=DISABLED)

# box send
box_send = Text(chatbot, width = 35, height = 4,font= ("Arial",14), bd = 1, bg = "#FAFAFA")
box_send.place(y = 540, x = 11)

# send button
send_bg = Image.open(BG_send)
send = ImageTk.PhotoImage(send_bg)
sendbtn = Button(chatbot,bg = "#DFFFFF", bd = 0,image = send,width = 75 , height = 75, command = sendText)
sendbtn.place(y = 547, x = 410)
box_send.bind("<Return>", lambda x: sendText())


chatbot.mainloop()