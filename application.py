import tinker as tk

class Application(tk.Tk):
    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg='black')
        self.geometry('100x100')
        