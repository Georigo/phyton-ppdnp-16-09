import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label1 = tkinter.Label(self.main_window, text="Witaj świecie")

        self.label1.pack(side="left")

        tkinter.mainloop()


my_gui = MyGui()
