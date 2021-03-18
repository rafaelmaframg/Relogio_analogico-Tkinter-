from datetime import datetime
from math import sin, cos, pi
from tkinter import *


class relogioAnalogico(Canvas):
    def __init__(self, root):
        Canvas.__init__(self, master=root)
        self.root = root
        self.canvas = Canvas(self.root, width=400, height=400, background="#000000")
        self.canvas.create_oval(10, 10, 390, 390, outline="white", width=2)
        self.canvas.pack()
        self.atualizar()

    def coordenadas(self, x1, y1, x2, y2):
        X = 175 * x1 + 200
        Y = 175 * -y1 + 200
        X1 = 175 * x2 + 200
        Y1 = 175 * -y2 + 200
        return (X, Y), (X1, Y1)

    def desenha_relogio(self):
        ini = pi / 2
        passo = pi / 6
        for i in range(12):
            angulo = ini - i * passo
            x, y = cos(angulo), sin(angulo)
            self.cria_circulos(x, y)
        self.desenha_ponteiros()
        self.cria_circulos(0, 0)

    def desenha_ponteiros(self):
        self.canvas.delete('ponteiro')
        horas = datetime.timetuple(datetime.now())
        h, m, s = horas[3], horas[4], horas[5]
        angulo = pi / 2 - pi / 6 * (h + m / 60.0)
        x, y = cos(angulo) * 0.70, sin(angulo) * 0.70
        ponteiro = self.canvas.create_line
        ponteiro(self.coordenadas(0, 0, x, y), tag='ponteiro', fill="#ffffff", width=25 / 3)
        angulo = pi / 2 - pi / 30 * (m + s / 60.0)
        x, y = cos(angulo) * 0.90, sin(angulo) * 0.90
        ponteiro(self.coordenadas(0, 0, x, y), tag='ponteiro', fill="#ffffff", width=25 / 5)
        angulo = pi / 2 - pi / 30 * s
        x, y = cos(angulo) * 0.95, sin(angulo) * 0.95
        ponteiro(self.coordenadas(0, 0, x, y), tag='ponteiro', fill="#ffffff", arrow='last')

    def cria_circulos(self, x, y):
        self.canvas.create_oval(self.coordenadas(-0.045 + x, -0.045 + y, 0.045 + x, 0.045 + y), fill="#808080")

    def atualizar(self):
        self.desenha_relogio()
        self.root.after(100, self.atualizar)


relogio = Tk()
relogioAnalogico(relogio)
relogio.title("Relogio")
relogio.mainloop()
