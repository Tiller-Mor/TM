from imports import *
from PIL import Image, ImageTk
from HOME.login import login
from HOME.about import about


def homed():
    root = Tk()
    root.resizable(True, False)
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.geometry(f'{w}x{h}')
    root.minsize(width=int(w/1.35), height=h)
    root.title('MoSave')
    icon = PhotoImage(file='images/icon.png')
    root.iconphoto(False, icon)
    # root.configure(bg='#ffd')
    im_b = Image.open('images/bg.jpg')
    img_b = im_b.resize((w, h))
    bg_image = ImageTk.PhotoImage(img_b)
    bg = Label(root, image=bg_image)
    bg.place(x=0, y=0)
    Label(root, text='MoSave', font=f'arial {int(w/68.3)} bold', padx=20).place(relx=0.5, y=int(h/15.4))
    everyday = 'Everyday saving made simple'
    other = 'All your future plans secured, being prepared to take care of your family'
    Label(root, text=everyday, font=f'arial {int(w/68.3)} bold', padx=20).place(relx=0.1, y=int(h/1.6))
    Label(root, text=other, font=f'arial {int(w/68.3)}', padx=20).place(relx=0.1, y=int(h / 1.436))

    def signin():
        root.destroy()
        login()

    def about_m():
        root.destroy()
        about()

    im_a = Image.open('images/arrow.jpg')
    img_a = im_a.resize((int(w/34.15), int(h/19.2)))
    a_image = ImageTk.PhotoImage(img_a)
    Button(root, image=a_image, command=signin, cursor='hand2').place(relx=0.9, y=int(h/1.28))
    Button(root, text='About', font=f'arial {int(w/68.3)}', cursor='hand2', command=about_m).\
        place(relx=0.5, y=int(h/1.32))
    root.mainloop()


homed()
