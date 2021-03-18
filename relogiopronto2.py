import tkinter as tk
from math import cos,radians,sin
import time

class RelogioAnalogio(tk.Canvas):

    def __init__(self,frame):
        tk.Canvas.__init__(self, master=frame)
        self.watch = tk.Canvas(frame, width=500, height=500, bg='black')
        self.watch.pack()
        self.atualiza()

    def desenha_ponteiro_horas(self,horas):
        self.watch.create_line((250,250,250+50*sin(radians(horas)),250-50*cos(radians(horas))),fill="green", width=4)

    def desenha_ponteiro_minuto(self,minutos):
        self.watch.create_line((250, 250, 250 + 80 * sin(radians(minutos)), 250 - 80 * cos(radians(minutos))), fill="darkblue", width=2)

    def desenha_ponteiro_segundos(self,segundos):
        self.watch.create_line((250, 250, 250 + 100 * sin(radians(segundos)), 250 - 100 * cos(radians(segundos))),
                                 fill="red", width=1)
    def time(self):

        lt = time.localtime()
        hora, minuto, segundo = lt[3], lt[4], lt[5]
        hora12 = (hora / 12) * 360
        minuto12 = (minuto / 60) * 360
        segundo12 = (segundo / 60) * 360
        return (hora12, minuto12, segundo12)

    def marcadores(self, rads, distancia, comprimento, marcador):
        x = (250 + int(cos(rads) * distancia)), (250 + int(sin(rads) * distancia))
        y = (int(cos(rads) * (distancia + comprimento)) + 250), (int(sin(rads) * (distancia + comprimento)) + 250)
        marcador(x, y)

    def chama_desenho(self):
        hora, minuto, segundo = self.time()
        self.desenha_ponteiro_horas(hora)
        self.desenha_ponteiro_minuto(minuto)
        self.desenha_ponteiro_segundos(segundo)
        self.watch.after(100, self.atualiza)

    def marcador30(self,x,y):
        self.watch.create_line(x[0],x[1],y[0],y[1],fill="red",width=3)

    def marcador6(self, x, y):
        self.watch.create_line(x[0], x[1], y[0], y[1], fill="red", width=3)

    def printa_marcador(self):
        self.watch.create_oval(100, 100, int(self.watch['width']) - 100,
                                 int(self.watch['height']) - 100, width=2,
                                 outline='white', fill='white')
        for i in range(0, 360, 30):
            self.marcadores(radians(i - 90), 120, 30, self.marcador30)
        for j in range(0, 360, 6):
            self.marcadores(radians(j - 90), 145, 5, self.marcador6)

    def atualiza(self):
        self.printa_marcador()
        self.chama_desenho()


relogio = tk.Tk()
analogico = RelogioAnalogio(relogio)
relogio.mainloop()