from tkinter import *
import license
import about
#Label(etiqueta)
 
root = Tk() # Tk initialize
 
root.title("Taller GIT") 
root.minsize(800,800) 
root.maxsize(800,800)
 
#Label con texto
#etiquetatexto = Label(WidgetContenedor, text=Contenido, font = (Tipo,Tamanno), bg=ColorDeFondo, fg=ColorDeLetra, width, height)
welcome_lbl = Label(root, text = "Bienvenidos al taller de GIT", font = ("calibri","18"), fg = "#000b98", width= 28, height = 1)
welcome_lbl.place(x = 20, y = 20)

def fetchLicenceView():
    display_about_view()

about_btn = Button(root, text="Licencia", command=fetchLicenceView, bg = "#000000", fg = "#ffffff", width = 50, height = 5)
about_btn.place(x=35,y=180)

root.mainloop()
