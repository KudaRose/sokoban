from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage

import time

"""
0-Suelo
1-Pared
2-Caja movil
3-Target
4-Caja fija
"""

# global vars

current_level = 1
total_steps = 0


def crea_matriz_num(level):
    matrix = [[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 3, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 3, 1, 0, 4, 0, 1],
            [1, 0, 4, 0, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 2, 0, 1],
            [1, 0, 2, 0, 4, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 2, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 3, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],

            [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 3, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 2, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 4, 0, 2, 0, 1],
            [1, 0, 2, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 0, 4, 0, 1],
            [1, 0, 4, 0, 1, 3, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 3, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],

            [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 3, 1, 1, 1, 1, 1],
            [1, 3, 0, 0, 2, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 4, 0, 2, 0, 1],
            [1, 0, 2, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1, 3, 0, 0, 4, 1],
            [1, 0, 2, 0, 0, 0, 0, 0, 3, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]]
    
    return matrix[level-1]


def crea_matriz_img(fi, co):
    m_i = [None] * fi
    for i in range(fi):
        m_i[i] = [None] * co

    return m_i


def crea_vector_img():
    v_i = []
    str_nom = "img_soko/soko-"
    str_ext = ".png"

    for i in range(6):
        v_i.append(PhotoImage(file=str_nom + str(i) + str_ext))

    return v_i


def crea_tablero_img(f, c, m_i, m_n, v_i):
    for i in range(f):
        for j in range(c):
            m_i[i][j] = ttk.Label(image=v_i[m_n[i][j]])
            m_i[i][j].place(x=(32 * i) + 100, y=(32 * j) + 100, width=32, height=32)
    return m_i


def movimiento_jugador(event, level_obj):    

    print(event.keysym, level_obj.l_jugador.winfo_x(), level_obj.l_jugador.winfo_y())
    """
    0-Suelo
    1-Pared
    2-Caja movil
    3-Target
    4-Caja fija
    """
    if event.keysym == "Up" and level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 1] != 1 and level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 1] != 4:
        level_obj.pasos.set(level_obj.pasos.get()+1)
        if level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 1] == 2:
            if level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 2] == 1 or level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 2] == 4 or level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 2] ==2:
                return
            else:
                if level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 2] == 0 or level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 2] == 3 or level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 2] == 1:
                    if level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 2] == 3:
                        level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 2] = 4
                        level_obj.mat_img[level_obj.iv_col.get()][level_obj.iv_fil.get() - 2].configure(image=level_obj.vec_img[4])
                        app.update()

                    elif level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 2] == 0:
                        level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 2] = 2
                        level_obj.mat_img[level_obj.iv_col.get()][level_obj.iv_fil.get() - 2].configure(image=level_obj.vec_img[2])
                        app.update()

                    elif level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 2] == 1:
                        level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 1] = 2
                        level_obj.mat_img[level_obj.iv_col.get()][level_obj.iv_fil.get() - 2].configure(image=level_obj.vec_img[level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 2]])
                        app.update()

                    level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 1] = 0
                    level_obj.mat_img[level_obj.iv_col.get()][level_obj.iv_fil.get() - 1].configure(image=level_obj.vec_img[level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() - 1]])
                    app.update()
                    
        level_obj.l_jugador.place(x=level_obj.l_jugador.winfo_x(), y=level_obj.l_jugador.winfo_y() - 32)
        level_obj.iv_fil.set(level_obj.iv_fil.get() - 1)

    elif event.keysym == "Down" and level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() + 1] != 1 and level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() + 1] != 4:
        level_obj.pasos.set(level_obj.pasos.get()+1)
        if level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() + 1] == 2:
            if level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() + 2] == 1 or level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() + 2] == 4 or level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() + 2] ==2:
                return
            else:
                if level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() + 2] == 0 or level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() + 2] == 3:

                    if level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() + 2] == 3:
                        level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() + 2] = 4
                        level_obj.mat_img[level_obj.iv_col.get()][level_obj.iv_fil.get() + 2].configure(image=level_obj.vec_img[4])
                    else:
                        level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() + 2] = 2
                        level_obj.mat_img[level_obj.iv_col.get()][level_obj.iv_fil.get() + 2].configure(image=level_obj.vec_img[level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() + 2]])

                    level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() + 1] = 0
                    level_obj.mat_img[level_obj.iv_col.get()][level_obj.iv_fil.get() + 1].configure(image=level_obj.vec_img[level_obj.mat_num[level_obj.iv_col.get()][level_obj.iv_fil.get() + 1]])
                    app.update()

        level_obj.l_jugador.place(x=level_obj.l_jugador.winfo_x(), y=level_obj.l_jugador.winfo_y() + 32)
        level_obj.iv_fil.set(level_obj.iv_fil.get() + 1)

    elif event.keysym == "Right" and level_obj.mat_num[level_obj.iv_col.get() + 1][level_obj.iv_fil.get()] != 1 and level_obj.mat_num[level_obj.iv_col.get() + 1][level_obj.iv_fil.get()] != 4:
        level_obj.pasos.set(level_obj.pasos.get()+1)
        if level_obj.mat_num[level_obj.iv_col.get() + 1][level_obj.iv_fil.get()] == 2:
            if level_obj.mat_num[level_obj.iv_col.get() +2][level_obj.iv_fil.get()] == 1 or level_obj.mat_num[level_obj.iv_col.get() +2][level_obj.iv_fil.get()] == 4 or level_obj.mat_num[level_obj.iv_col.get() +2][level_obj.iv_fil.get()] ==2:
                return
            else:    
                if level_obj.mat_num[level_obj.iv_col.get() + 2][level_obj.iv_fil.get()] == 0 or level_obj.mat_num[level_obj.iv_col.get() + 2][level_obj.iv_fil.get()] == 3:

                    if level_obj.mat_num[level_obj.iv_col.get() + 2][level_obj.iv_fil.get()] == 3:
                        level_obj.mat_num[level_obj.iv_col.get() + 2][level_obj.iv_fil.get()] = 4
                        level_obj.mat_img[level_obj.iv_col.get() + 2][level_obj.iv_fil.get()].configure(image=level_obj.vec_img[4])
                    else:
                        level_obj.mat_num[level_obj.iv_col.get() + 2][level_obj.iv_fil.get()] = 2
                        level_obj.mat_img[level_obj.iv_col.get() + 2][level_obj.iv_fil.get()].configure(image=level_obj.vec_img[level_obj.mat_num[level_obj.iv_col.get() + 2][level_obj.iv_fil.get()]])

                    level_obj.mat_num[level_obj.iv_col.get() + 1][level_obj.iv_fil.get()] = 0
                    level_obj.mat_img[level_obj.iv_col.get() + 1][level_obj.iv_fil.get()].configure(image=level_obj.vec_img[level_obj.mat_num[level_obj.iv_col.get() + 1][level_obj.iv_fil.get()]])
                    app.update()

        level_obj.l_jugador.place(x=level_obj.l_jugador.winfo_x() + 32, y=level_obj.l_jugador.winfo_y())
        level_obj.iv_col.set(level_obj.iv_col.get() + 1)

    elif event.keysym == "Left" and level_obj.mat_num[level_obj.iv_col.get() - 1][level_obj.iv_fil.get()] != 1 and level_obj.mat_num[level_obj.iv_col.get() - 1][level_obj.iv_fil.get()] != 4:
        level_obj.pasos.set(level_obj.pasos.get()+1)
        if level_obj.mat_num[level_obj.iv_col.get() - 1][level_obj.iv_fil.get()] == 2:
            if level_obj.mat_num[level_obj.iv_col.get() - 2][level_obj.iv_fil.get()] == 1 or level_obj.mat_num[level_obj.iv_col.get() - 2][level_obj.iv_fil.get()] == 4 or level_obj.mat_num[level_obj.iv_col.get() - 2][level_obj.iv_fil.get()] ==2:
                return
            else:
                if level_obj.mat_num[level_obj.iv_col.get() - 2][level_obj.iv_fil.get()] == 0 or level_obj.mat_num[level_obj.iv_col.get() - 2][level_obj.iv_fil.get()] == 3:

                    if level_obj.mat_num[level_obj.iv_col.get() - 2][level_obj.iv_fil.get()] == 3:
                        level_obj.mat_num[level_obj.iv_col.get() - 2][level_obj.iv_fil.get()] = 4
                        level_obj.mat_img[level_obj.iv_col.get() - 2][level_obj.iv_fil.get()].configure(image=level_obj.vec_img[4])
                    else:
                        level_obj.mat_num[level_obj.iv_col.get() - 2][level_obj.iv_fil.get()] = 2
                        level_obj.mat_img[level_obj.iv_col.get() - 2][level_obj.iv_fil.get()].configure(image=level_obj.vec_img[level_obj.mat_num[level_obj.iv_col.get() - 2][level_obj.iv_fil.get()]])

                    level_obj.mat_num[level_obj.iv_col.get() - 1][level_obj.iv_fil.get()] = 0
                    level_obj.mat_img[level_obj.iv_col.get() - 1][level_obj.iv_fil.get()].configure(image=level_obj.vec_img[level_obj.mat_num[level_obj.iv_col.get() - 1][level_obj.iv_fil.get()]])
                    app.update()

        level_obj.l_jugador.place(x=level_obj.l_jugador.winfo_x() - 32, y=level_obj.l_jugador.winfo_y())
        level_obj.iv_col.set(level_obj.iv_col.get() - 1)

    
    #check for winning: no values 2 or 3
    win_flag = True
    for mat_list in level_obj.mat_num:
      for mat_number in mat_list:
        if mat_number == 2 or mat_number == 3:
          win_flag = False
          break
    if win_flag:
      global current_level, total_steps
      global current_level_obj
      current_level += 1
      total_steps += level_obj.pasos.get()
      level_obj.destroy_level()

      if (current_level <= 3):
        current_level_obj = Level(current_level)
        current_level_obj.draw_level()
      else: 
        Label(app, text=f"Game finished.").pack()
        Label(app, text=f"Steps total: {total_steps}").pack()
        global reset_btn
        reset_btn.destroy()
        Button(app, text="Exit", command=lambda: app.destroy()).pack()
    else: 
      level_obj.steps_label_var.set(f"Pasos: {level_obj.pasos.get()}")

class Level:
  def __init__(self, level_number):
    self.mat_img = crea_matriz_img(10, 10)
    self.mat_num = crea_matriz_num(level_number)
    self.vec_img = crea_vector_img()

    self.iv_fil = IntVar()
    self.iv_col = IntVar()
    self.iv_col.set(4)
    self.iv_fil.set(4)

    self.pasos=IntVar()
    self.pasos.set(0)

  def draw_level(self):
    self.board = crea_tablero_img(10, 10, self.mat_img, self.mat_num, self.vec_img)

    self.l_jugador = ttk.Label(image=self.vec_img[5])
    self.l_jugador.place(x=(32 * self.iv_col.get()) + 100, y=(32 * self.iv_fil.get()) + 100, width=32, height=32)

    self.steps_label_var = StringVar()
    self.steps_label_var.set(f"Pasos: {self.pasos.get()}")
    self.steps_label = ttk.Label(textvariable=self.steps_label_var, font=('MathJax_SansSerif-Bold', 14, "bold"))
    self.steps_label.pack()


  def destroy_level(self):
    for line in self.board:
      for elem in line:
        elem.destroy()
    self.l_jugador.destroy()
    self.steps_label.destroy()

# PROGRAMA


app = Tk()
app.geometry("500x500")
app.title("Sokobahn")

current_level_obj = Level(1)

current_level_obj.draw_level()
app.bind("<Key>", lambda event: movimiento_jugador(event, current_level_obj))


def destroy_level():
  current_level_obj.destroy_level()

def draw_level():
  current_level_obj.draw_level()

def reset_level():
  global current_level_obj
  current_level_obj.destroy_level()
  current_level_obj = Level(current_level)
  current_level_obj.draw_level()

reset_btn = Button(app, text="reset level", command=lambda: reset_level())
reset_btn.place(x=350, y=10)

app.mainloop()