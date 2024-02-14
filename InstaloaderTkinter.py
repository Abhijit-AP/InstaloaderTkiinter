#Connection error at the moment with error code 401

from tkinter import *
import instaloader
from instaloader import *
import os

#initalize tkinter
root = Tk()

#Initialize instaloader
L = instaloader.Instaloader()

#set paths
path = "C:/Users/Loki/Videos/PY_INST_Videos/"
path_new = "C:/Users/Loki/Videos/"
os.chdir(path_new)

def clear_files_savedVideos():
    for file in os.listdir(path):
        if not file.endswith(".mp4"):
            os.remove(path+file)
    completeLabel_savedVideos = Label(root, text="Download Complete!")
    completeLabel_savedVideos.grid(row=8, column=1)

#Duplicate of above just to get the "download complete" message below the button
def clear_files_pVideos():
    for file in os.listdir(path):
        if not file.endswith(".mp4"):
            os.remove(path+file)
    completeLabel_pVideos = Label(root, text="Download Complete!")
    completeLabel_pVideos.grid(row=13, column=1)

#Duplicate of above just to get the "download complete" message below the button
def clear_files_cVideos():
    for file in os.listdir(path):
        if not file.endswith(".mp4"):
            os.remove(path+file)
    completeLabel_cVideo = Label(root, text="Download Complete!")
    completeLabel_cVideo.grid(row=17, column=1)

def savedVideo():
    uName = enterID.get()
    uPass = enterPass.get()
    svCount = enterSavedVideoCount.get()
    svCount = int(svCount)
    L.login(user=uName, passwd=uPass)
    
    i = 0

    profile = Profile.from_username(L.context, uName)
    if svCount>0:
        for post in profile.get_saved_posts():
            L.download_post(post, target="PY_INST_Videos")
            i +=1
            if i == svCount:
                break
        clear_files_savedVideos()
    else:
        for post in profile.get_saved_posts():
            L.download_post(post, target="PY_INST_Videos")
        clear_files_savedVideos()

def profileVideo():
    pname = enterProfileID.get()
    pCount = enterProfileVideoCount.get()
    pCount = int(pCount)

    i = 0 

    profile = Profile.from_username(L.context, pname)
    if pCount > 0:
        for post in profile.get_posts():
            L.download_post(post, target="PY_INST_Videos")
            i += 1
            if i == pCount:
                break
        clear_files_pVideos()
    else:
        for post in profile.get_posts():
            L.download_post(post, target="PY_INST_Videos")
        clear_files_pVideos()

def singleVideo():
    sCode = entersingleID.get()

    post = Post.from_shortcode(L.context, sCode)
    L.download_post(post, target="PY_INST_Videos")
    clear_files_cVideos()


#set frame for tkinter
filler1 = Label(root, text="_____________________________")
filler1.grid(row=1, column=0)

mainLabel = Label(root, text="Instagram Downloader", width=50)
mainLabel.grid(row=1, column=1)

filler2 = Label(root, text="_____________________________")
filler2.grid(row=1, column=2)

filler3 = Label(root, text="")
filler3.grid(row=8, column=0)

filler4 = Label(root, text="")
filler4.grid(row=13, column=0)

filler5 = Label(root, text="")
filler5.grid(row=17, column=0)

savedVideoLabel = Label(root, text="Download Saved Videos:")
savedVideoLabel.grid(row=3, column=0)
savedVideoID = Label(root, text="Enter your ID:", anchor="e", justify=RIGHT)
savedVideoID.grid(row=4, column=0)
enterID = Entry(root, width=50)
enterID.grid(row=4, column=1)
savedVideoPass = Label(root, text="Enter you Password:", anchor="e", justify=RIGHT)
savedVideoPass.grid(row=5, column=0)
enterPass = Entry(root, width=50)
enterPass.grid(row=5, column=1)
savedVideoCount = Label(root, text="# of Videos; 0 = all")
savedVideoCount.grid(row=6, column=0)
enterSavedVideoCount = Entry(root, width=20)
enterSavedVideoCount.grid(row=6, column=1)
downloadSavedVideoButton = Button(root, text="Download", padx=25, pady=5, bg="black", fg="white", command=savedVideo)
downloadSavedVideoButton.grid(row=7, column=1)

profileVideoLabel = Label(root, text="Download Profile Videos:")
profileVideoLabel.grid(row=9, column=0)
profileVideoID = Label(root, text="Enter profile ID:")
profileVideoID.grid(row=10, column=0)
enterProfileID = Entry(root, width=50)
enterProfileID.grid(row=10, column=1)
profileVideoCount = Label(root, text="# of Videos; 0 = all")
profileVideoCount.grid(row=11, column=0)
enterProfileVideoCount = Entry(root, width=20)
enterProfileVideoCount.grid(row=11, column=1)
downloadProfileVideoButton = Button(root, text="Download", padx=25, pady=5, bg="Black", fg="white", command=profileVideo)
downloadProfileVideoButton.grid(row=12, column=1)

singleVideoLabel = Label(root, text="Download Single Videos:")
singleVideoLabel.grid(row=14, column=0)
singleVideoID = Label(root, text="Enter Shortcode:")
singleVideoID.grid(row=15, column=0)
entersingleID = Entry(root, width=50)
entersingleID.grid(row=15, column=1)
downloadSingleVideoButton = Button(root, text="Download", padx=25, pady=5, bg="Black", fg="white", command=singleVideo)
downloadSingleVideoButton.grid(row=16, column=1)

#loop tkinter
root.mainloop()