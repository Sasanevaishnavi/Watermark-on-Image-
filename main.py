import tkinter
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont


img = None
img_display = None
img_path = None

window = tkinter.Tk()
window.title("Watermark")
window.geometry("600x600")

def upload_image():
    global img, img_display, img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if img_path:
        img = Image.open(img_path)
        img.thumbnail((400, 400))
        img_display = ImageTk.PhotoImage(img)
        canvas.create_image(200,200, image = img_display)
def add_text():
    global img, img_display, img_path
    if not img_path:
        messagebox.showwarning("Warning", "Upload image First")
        return

    watermark_text = text_entry.get()
    if not text_entry:
        messagebox.showwarning("Warning", "enter text first")
        return

    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    text_position = (10,10)
    draw.text(text_position,watermark_text,(255, 255, 255), font=font)

    img_display = ImageTk.PhotoImage(img)
    canvas.create_image(200, 200, image=img_display)

    messagebox.showinfo("Success", "Watermark added successfully")




my_label = tkinter.Label(text="Watermark", font=("Arial", 30, "bold"))
my_label.pack(pady=10)
my_label = tkinter.Label(text="Hello!!! Wellcome on my page to add watermark on your photos ", font=("Arial", 10, "bold"), bg="#f7f5dd")
my_label.pack(pady=10)


button = Button(text=" Upload  Image here", command=upload_image)
button.pack()

canvas = Canvas(width=400, height=400)
canvas.pack()


text_entry = Entry(width=35)
text_entry.pack()
text_button = Button(text="Add text on Image ", command=add_text)
text_button.pack()


# canvas.create_image(100, 112, image=img_path)
# text_on_img = canvas.create_text(100, 130, text="00:00", fill="white", font=("Courier", 5))


window.mainloop()

