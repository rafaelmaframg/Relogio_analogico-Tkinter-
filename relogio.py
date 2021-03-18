import tkinter
import datetime
import math

class main():

    def __init__(self):
        principal = tkinter.Tk()
        principal.geometry("250x250")
        principal.title(".::Relogio::.")
        relogio = relogioAnalogico(principal)
        principal.mainloop()

class relogioAnalogico(tkinter.Canvas):

    def __init__(self, master=None,**kwargs):
        tkinter.Canvas.__init__(self,master,**kwargs)
        self.hr = None
        self.min = None
        self.seg = None
        self.analogico = tkinter.Canvas(master, width=250, height=250)
        self.angulo = 0
        for i in range(13):
            self.analogico.create_oval(125 + int(math.cos(math.radians(self.angulo-90)) * 100),
                                    125 + int(math.sin(math.radians(self.angulo-90)) * 100),
                                    int(math.cos(math.radians(self.angulo-90)) * (100 + 1)) + 125,
                                    int(math.sin(math.radians(self.angulo-90)) * (100 + 1)) + 125,
                                    fill='black', width=4)
            self.angulo += 30
        self.analogico.pack()
        self.atualizar(self.analogico)

    def funcao(self): self.atualizar(self.analogico)

    def atualizar(self, analogico):
        if not self.min:
            self.min = analogico.create_line(0,0,0,0,fill="brown",width=2)
        if not self.hr:
            self.hr = analogico.create_line(0,0,0,0,fill="darkgreen",width=3)
        if not self.seg:
            self.seg = analogico.create_line(0,0,0,0,fill="black",width=1)
        hora = ((datetime.datetime.now().hour * 30.0) + (30.0 * (datetime.datetime.now().minute / 60.0)))
        minuto = ((datetime.datetime.now().minute * 6.0) + (6.0 * (datetime.datetime.now().second / 60.0)))
        segundo = (datetime.datetime.now().second * 6)
        self.analogico.create_oval(4, 4, 246, 246, width=2, outline='black')
        self.analogico.coords(self.hr, 120, 120,
                         int(math.cos(math.radians(hora - 90)) * 50) + 120,
                         int(math.sin(math.radians(hora - 90)) * 50) + 120)
        self.analogico.coords(self.min, 120, 120,
                         int(math.cos(math.radians(minuto - 90)) * 70) + 120,
                         int(math.sin(math.radians(minuto - 90)) * 70) + 120)
        self.analogico.coords(self.seg, 120, 120,
                         int(math.cos(math.radians(segundo - 90)) * 95) + 120,
                         int(math.sin(math.radians(segundo - 90)) * 95) + 120)
        analogico.after(100, self.funcao)


main()

