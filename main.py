from ast import arg
import tkinter as tk

class Application(tk.Tk):
    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg='black')
        self.geometry('100x100')
        
        
if __name__ == "__main__":
    app = Application()
    app.mainloop()
        
        
        
        