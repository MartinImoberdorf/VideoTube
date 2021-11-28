from pytube import YouTube
from tkinter import *
from tkinter import messagebox

def descargar():
    url=miLink.get()
    if url !='':
        miLink.set("")
        messagebox.showinfo(title=None, message="Descargando...")
        YouTube(url).streams.get_highest_resolution().download('Videos')
        messagebox.showinfo(title=None, message="Descarga completa!")
    else:
        messagebox.showwarning(title=None, message="Por favor ingresar el link del video a descargar.")

def main():
    root=Tk()

    ancho_ventana =500
    alto_ventana=350

    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

    root.geometry(posicion)
    root.configure(background="white")
    root.title("VideoTube")
    root.resizable(width=False,height=False)
    root.iconbitmap('Img/Logo.ico')

    global miLink
    miLink=StringVar()

    logo=PhotoImage(file="Img/Logo.png")
    btnLogo=Label(root,image=logo,height=225,width=430,background="white").place(x=245,y=145,anchor=CENTER)

    link=Entry(root,width=30,background="white",textvariable=miLink,fg="black",font=("Bahnschrift SemiBold SemiConden",15)).place(x=180,y=305,anchor=CENTER,height=40)

    buscar=Button(root,text="Descargar",width=10,background="white",fg="black",font=("Bahnschrift SemiBold SemiConden",15),command=descargar).place(x=410,y=305,anchor=CENTER,height=40)


    root.mainloop()


if __name__ == '__main__':
    main()