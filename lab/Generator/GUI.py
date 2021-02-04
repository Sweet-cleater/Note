import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "click me!"
        self.hi_there["command"] = self.but
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
    
    #ランダムに学問分野を表示する関数
    def content(self):
        import random

        with open('out.txt') as f:
            l = f.readlines()

        l = [s for s in l if s != '\n']

        while(1):
            content1 = random.randrange(len(l))
            content2 = random.randrange(len(l))
            if content1 != content2:
                break
        
        return str(l[content1])
    
    def but(self):
        cont1 = self.content()
        Static1 = tk.Label(text=str(cont1))
        Static1.pack()

root = tk.Tk()
app = Application(master=root)
app.mainloop()