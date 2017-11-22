import tkinter

def convert(Celsius, Fahrenheit):
    """ Convert the value in Fahrenheit to Celsius and store the result."""
    f = Fahrenheit.get()
    c = '%.1f' % ((f - 32) * 5 / 9)
    Celsius.set(c)

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

Celsius = tkinter.StringVar()
Fahrenheit = tkinter.DoubleVar()

tkinter.Label(frame, text = 'Temperature in Fahrenheit:').pack()

text = tkinter.Entry(frame, textvar = Fahrenheit)
text.pack()

label = tkinter.Label(frame, textvar = Celsius)
label.pack()

button = tkinter.Button(frame, text = 'Convert', command = lambda: convert(Celsius, Fahrenheit))
button.pack()

button2 = tkinter.Button(frame, text = 'Quit', command = lambda: window.destroy())
button2.pack()

window.mainloop()
