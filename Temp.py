# use sunken radio buttons 
import tkinter

master = tkinter.Tk()


v = tkinter.IntVar()

tkinter.Radiobutton(master, text="One", indicatoron=0, variable=v, value=1,font=('Calibri', 14, 'bold')).pack()
tkinter.Radiobutton(master, text="Two", indicatoron=0, variable=v, value=2,font=('Calibri', 14, 'bold')).pack()
tkinter.Radiobutton(master, text="Three", indicatoron=0, variable=v, value=3,font=('Calibri', 14, 'bold')).pack()
mainloop()
