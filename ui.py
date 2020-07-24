import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

#WINDOW ATTRIBUTES
#create window and window specs
window = tk.Tk()
window.title("Word Cloud Generator")
window.geometry("600x600")
window.configure(background='white')

#EXAMPLE IMAGE
#get image to be used as example
image_path = r"C:\Users\andre\Desktop\wordcloud-master\wordcloud-master\example.jpg"

#create Tkinter image of example.jpg
tkinter_image = ImageTk.PhotoImage(Image.open(image_path))

#create label widget
exaple_lbl = tk.Label(window, image=tkinter_image)
#pack the widget
exaple_lbl.pack(side="bottom", fill="both", expand="yes")

#UPLOAD IMAGE TO BE USED IN WORDCLOUD 
#upload an image
def UploadAction():
    global filename
    filename = filedialog.askopenfile(event=None)
    
upload_btn = tk.Button(window, text='Open', command=UploadAction)
upload_btn.pack(side="top",pady=10)

print(filename)
window.mainloop()