from tkinter import *
from PIL import Image,ImageTk
import os

def rotate_image():
    global counter
    counter+=1
    if counter == len(img_array) :
        counter = 0
    image_label.config(image=img_array[counter])
counter = 0
root = Tk()
root.title("Wallpaper Viewer")

root.geometry("340x550")
root.configure(background="black")

files = os.listdir("Wallpapers")

img_array = []

for file in files:
    img = Image.open(os.path.join('Wallpapers',file))
    resized_image = img.resize((300,450))
    img_array.append(ImageTk.PhotoImage(resized_image))

image_label = Label(root, image=img_array[counter])
image_label.pack(pady=(20,0))

nxt_btn = Button(root, text="Next",fg="black",bg='white',width=42,height=2,command=rotate_image)
nxt_btn.pack(pady=(10,15))

root.mainloop()