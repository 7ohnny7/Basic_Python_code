# widgets:
from tkinter import *

window = Tk()
window.title('Button Example')

btn_end = Button( window, text = 'Close' , command=exit )
def tog():
    if window.cget( 'bg' ) == 'yelloe' :
        window.configure( bg = 'gray')
    else:
        window.configure( bg = 'yellow')

btn_tog = Button(window, text = 'switch' , command=tog)

btn_tog.pack( padx = 150 , pady = 20)
btn_end.pack( padx = 150 , pady = 20)


#sustain window:
window.mainloop()
