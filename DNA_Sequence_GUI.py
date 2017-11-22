import tkinter

def count(text, total):
    """Update total with the total number of As, Ts, Cs, and Gs found."""

    data = text.get('0.0', tkinter.END)
    counts = {}
    for letter in 'ATCG':
        counts[letter] = data.count(letter)
    total.set('Num As: {0} Num Ts: {1} Num Cs: {2} Num Gs: {3}'.format(
        counts['A'], counts['T'], counts['C'], counts['G']))

window = tkinter.Tk()
text = tkinter.Text(window, height = 10, width = 40)
text.pack()

total = tkinter.StringVar()

button = tkinter.Button(window, text = 'Count', command = lambda: count(text, total))
button.pack()

label = tkinter.Label(window, textvar = total)
label.pack()
window.mainloop()
