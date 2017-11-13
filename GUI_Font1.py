# GUI_Font1.py
import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text='Hello', font=('Courier', 14, 'bold italic'))
button.pack()
window.mainloop()

### NOTE:
#'bold italic underline overstrike'  - can be in any order

#Normal text: 
#font=('Courier', 14) OR font=('Courier', 14, '') OR font=('Courier', 14, 'normal')
