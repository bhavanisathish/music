#music
#put all the images in a single folder
import os 
import threading
import time                
import tkinter.messagebox   
from tkinter import *
from mutagen.mp3 import MP3
from pygame import mixer
from tkinter import ttk
from ttkthemes import themed_tk as tk
from tkinter import filedialog
import ToolTip
root=tk.ThemedTk()
root.get_themes()
root.set_theme("plastik")       
menub=Menu(root)    #plastik
root.config(menu=menub)
#root.config(bg='blue')
#creating sub menu
smenu=Menu(menub,tearoff=0)

#playlist contain file name and path 
#list box contain only file name
 
playlist=[]

def browse():
    global fm          #load la place pannu
    fm=filedialog.askopenfilename()
    print(fm)
    addtoplay(fm)
def addtoplay(f):
    f=os.path.basename(f)
    index=0
    lab1.insert(index,f)
    playlist.insert(index,fm)
    index+=1
   
def about_us():
    tkinter.messagebox.showinfo('MUSIC PLAYER','')
menub.add_cascade(label="File",menu=smenu)  #cascade
smenu.add_command(label="Open",command=browse)
smenu.add_command(label="Exit",command=root.destroy)
smenu2=Menu(menub,tearoff=0)
menub.add_cascade(label="Help",menu=smenu2)
smenu2.add_command(label="about us",command=about_us)
mixer.init()    #intialization

root.title("player")
root.iconbitmap(r"images\l1.ico")
lw=ttk.Label(root,text="Crazy Player",font=("Times 25 italic"))
lw.pack()
sbar=ttk.Label(root,text="melody", relief=SUNKEN,anchor=W,font=("Times 15 italic"))        #play_music sbar["text"]="play"+os.path.basename(fm)
sbar.pack(side=BOTTOM,fill=X)

lframe=Frame(root)
lframe.pack(side=LEFT,padx=30,pady=30)

  # index contain 2 parameter index and name
lab1=Listbox(lframe)
lab1.pack()
def del_s():
     selected_song=lab1.curselection()
     selected_song=int(selected_song[0])
     playlist.pop(selected_song)
     lab1.delete(selected_song)
b1=ttk.Button(lframe,text="Insert",command=browse)
b1.pack(side=LEFT,padx=10,pady=10)
b2=ttk.Button(lframe,text="Delete",command=del_s)
b2.pack(side=RIGHT)

rframe=Frame(root)
rframe.pack(side=RIGHT)


tframe=Frame(rframe)
tframe.pack()

llabel=ttk.Label(tframe,text="Total length = --:-- ",relief=GROOVE,font=("Times 15 italic"))
llabel.pack(pady=10)
clabel=ttk.Label(tframe,text="Current time = --:--",relief=GROOVE,font=("Times 15 italic"))
clabel.pack(pady=10)


def show_det(playit):
    filedata=os.path.splitext(playit)
    if filedata[1] == '.mp3':
        audio=MP3(playit)
        len=audio.info.length
    else:
        a=mixer.Sound(playit)
        len=a.get_length()
    m,s=divmod(len,60)
    m=round(m)
    s=round(s)
    tformat='{:02d}:{:02d}'.format(m,s)
    llabel['text']="Total length = "+tformat
    t1=threading.Thread(target=sc,args=(len,))
    t1.start()
def sc(t):
    global paused
    current_time=0
    while current_time<=t and mixer.music.get_busy():
        if paused:
            continue
        else:
            m,s=divmod(current_time,60)
            m=round(m)
            s=round(s)
            tformat='{:02d}:{:02d}'.format(m,s)
            clabel['text']="current time = "+tformat
            time.sleep(1)    #milli seconds
            current_time+=1
            
def play_m():
    global paused
    if paused:
         mixer.music.unpause()
         sbar["text"]="resumed  |"
         paused=FALSE
    else:
         try:        #unpause the music
            play_s()
            time.sleep(1)
            selected_song=lab1.curselection()
            selected_song=int(selected_song[0])
            playit=playlist[selected_song]
            mixer.music.load(playit)
            mixer.music.play()
            sbar["text"]="play  |"+ os.path.basename(playit)
            #print("nj")
            show_det(playit)
         except:
            tkinter.messagebox.showerror("error","file not found")          
def play_s():
    sbar["text"]="music stopped |"
    mixer.music.stop()
def set_vol(val):       #val--string
    volume=float(val)/100     #val--int 
    mixer.music.set_volume(volume)      #set_volume-- takes the function value from 0 to 1 (0,0.1-0.99,1)
paused=FALSE
def paubut():
    global paused
    paused=TRUE
    mixer.music.pause()
    sbar['text']="pause"
def r_music():
    play_m()
    sbar["text"]="rewined |"
muted=False
def mute():
    global muted
    if muted:
         mixer.music.set_volume(0.5)
         mbut.config(image=umphoto)
         sca.set(50)
         muted=False          
    else:
        mixer.music.set_volume(0)
        mbut.config(image=mphoto)
        sca.set(0)
        muted=True   

def help(widget, position):
    import time
    return "The time is " + time.asctime()

    
middleframe=Frame(rframe) 
middleframe.pack(pady=30)
pphoto=PhotoImage(file="images/2.png")
pbtn=ttk.Button(middleframe,image=pphoto,command=play_m)       #button
pbtn.grid(row=0,column=0,padx=10)
ToolTip.register(pbtn, "Play the music")
#ToolTip.register(pbtn, help)
sphoto=PhotoImage(file="images/3.png")
sbtn=ttk.Button(middleframe,image=sphoto,command=play_s)
sbtn.grid(row=0,column=1,padx=10)
ToolTip.register(sbtn, "Stop the music")
#ToolTip.register(sbtn, help)
pauphoto=PhotoImage(file="images/4.png")
pb=ttk.Button(middleframe,image=pauphoto,command=paubut)
pb.grid(row=0,column=2,padx=10)
ToolTip.register(pb, "Pause the music")
#ToolTip.register(pb, help)
bframe=Frame(rframe)
bframe.pack(pady=30)
rephoto=PhotoImage(file="images/7.png")
pb1=ttk.Button(bframe,image=rephoto,command=r_music)
pb1.grid(row=0,column=0,padx=10)
ToolTip.register(pb1, "Rewind the music")
mphoto=PhotoImage(file="images/volume.png")
umphoto=PhotoImage(file="images/speaker.png")
mbut=ttk.Button(bframe,image=umphoto,command=mute)
mbut.grid(row=0,column=1)
ToolTip.register(mbut, "mute or unmute the music")
#get_busy==1 when music is paused
sca=ttk.Scale(bframe,from_=0,to=100,orient=HORIZONTAL,command=set_vol)
sca.set(50)
mixer.music.set_volume(0.5)  #setting volume
sca.grid(row=0,column=2,padx=10)


def on_closing():
    play_s()
    root.destroy()
root.protocol("WM_DELETE_WINDOW",on_closing)
root.mainloop()


'''
root-- status bar,left frame,right frame
lframe-- playlist,insert,delete
rframe-- other the else
'''