from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage

"""
0-Suelo
1-Pared
2-Caja movil
3-Target
4-Caja fija
"""

def crea_matriz_num():
    m_n1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 3, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 3, 1, 0, 4, 0, 1],
           [1, 0, 4, 0, 1, 1, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 2, 0, 1],
           [1, 0, 2, 0, 4, 0, 0, 1, 1, 1],
           [1, 0, 0, 0, 0, 2, 0, 0, 0, 1],
           [1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 3, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    m_n2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 3, 1, 1, 1, 1, 1],
           [1, 0, 0, 0, 2, 0, 0, 0, 0, 1],
           [1, 1, 1, 0, 0, 4, 0, 2, 0, 1],
           [1, 0, 2, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 1, 1, 0, 4, 0, 1],
           [1, 0, 4, 0, 1, 3, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 3, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    m_n3 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 0, 3, 1, 1, 1, 1, 1],
           [1, 3, 0, 0, 2, 0, 0, 0, 0, 1],
           [1, 1, 1, 0, 0, 4, 0, 2, 0, 1],
           [1, 0, 2, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
           [1, 0, 0, 0, 1, 3, 0, 0, 4, 1],
           [1, 0, 2, 0, 0, 0, 0, 0, 3, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    return m_n3


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


def movimiento_jugador(event):
    print(event.keysym, l_jugador.winfo_x(), l_jugador.winfo_y())
    """
    0-Suelo
    1-Pared
    2-Caja movil
    3-Target
    4-Caja fija
    """
    if event.keysym == "Up" and mat_num[iv_col.get()][iv_fil.get() - 1] != 1 and mat_num[iv_col.get()][iv_fil.get() - 1] != 4:
        pasos.set(pasos.get()+1)
        if mat_num[iv_col.get()][iv_fil.get() - 1] == 2:
            if mat_num[iv_col.get()][iv_fil.get() - 2] == 1 or mat_num[iv_col.get()][iv_fil.get() - 2] == 4 or mat_num[iv_col.get()][iv_fil.get() - 2] ==2:
                return
            else:
                if mat_num[iv_col.get()][iv_fil.get() - 2] == 0 or mat_num[iv_col.get()][iv_fil.get() - 2] == 3 or mat_num[iv_col.get()][iv_fil.get() - 2] == 1:
                    if mat_num[iv_col.get()][iv_fil.get() - 2] == 3:
                        mat_num[iv_col.get()][iv_fil.get() - 2] = 4
                        mat_img[iv_col.get()][iv_fil.get() - 2].configure(image=vec_img[4])
                        app.update()

                    elif mat_num[iv_col.get()][iv_fil.get() - 2] == 0:
                        mat_num[iv_col.get()][iv_fil.get() - 2] = 2
                        mat_img[iv_col.get()][iv_fil.get() - 2].configure(image=vec_img[2])
                        app.update()

                    elif mat_num[iv_col.get()][iv_fil.get() - 2] == 1:
                        mat_num[iv_col.get()][iv_fil.get() - 1] = 2
                        mat_img[iv_col.get()][iv_fil.get() - 2].configure(image=vec_img[mat_num[iv_col.get()][iv_fil.get() - 2]])
                        app.update()

                    mat_num[iv_col.get()][iv_fil.get() - 1] = 0
                    mat_img[iv_col.get()][iv_fil.get() - 1].configure(image=vec_img[mat_num[iv_col.get()][iv_fil.get() - 1]])
                    app.update()
                    
        l_jugador.place(x=l_jugador.winfo_x(), y=l_jugador.winfo_y() - 32)
        iv_fil.set(iv_fil.get() - 1)

    elif event.keysym == "Down" and mat_num[iv_col.get()][iv_fil.get() + 1] != 1 and mat_num[iv_col.get()][iv_fil.get() + 1] != 4:
        pasos.set(pasos.get()+1)
        if mat_num[iv_col.get()][iv_fil.get() + 1] == 2:
            if mat_num[iv_col.get()][iv_fil.get() + 2] == 1 or mat_num[iv_col.get()][iv_fil.get() + 2] == 4 or mat_num[iv_col.get()][iv_fil.get() + 2] ==2:
                return
            else:
                if mat_num[iv_col.get()][iv_fil.get() + 2] == 0 or mat_num[iv_col.get()][iv_fil.get() + 2] == 3:

                    if mat_num[iv_col.get()][iv_fil.get() + 2] == 3:
                        mat_num[iv_col.get()][iv_fil.get() + 2] = 4
                        mat_img[iv_col.get()][iv_fil.get() + 2].configure(image=vec_img[4])
                    else:
                        mat_num[iv_col.get()][iv_fil.get() + 2] = 2
                        mat_img[iv_col.get()][iv_fil.get() + 2].configure(image=vec_img[mat_num[iv_col.get()][iv_fil.get() + 2]])

                    mat_num[iv_col.get()][iv_fil.get() + 1] = 0
                    mat_img[iv_col.get()][iv_fil.get() + 1].configure(image=vec_img[mat_num[iv_col.get()][iv_fil.get() + 1]])
                    app.update()

        l_jugador.place(x=l_jugador.winfo_x(), y=l_jugador.winfo_y() + 32)
        iv_fil.set(iv_fil.get() + 1)

    elif event.keysym == "Right" and mat_num[iv_col.get() + 1][iv_fil.get()] != 1 and mat_num[iv_col.get() + 1][iv_fil.get()] != 4:
        pasos.set(pasos.get()+1)
        if mat_num[iv_col.get() + 1][iv_fil.get()] == 2:
            if mat_num[iv_col.get() +2][iv_fil.get()] == 1 or mat_num[iv_col.get() +2][iv_fil.get()] == 4 or mat_num[iv_col.get() +2][iv_fil.get()] ==2:
                return
            else:    
                if mat_num[iv_col.get() + 2][iv_fil.get()] == 0 or mat_num[iv_col.get() + 2][iv_fil.get()] == 3:

                    if mat_num[iv_col.get() + 2][iv_fil.get()] == 3:
                        mat_num[iv_col.get() + 2][iv_fil.get()] = 4
                        mat_img[iv_col.get() + 2][iv_fil.get()].configure(image=vec_img[4])
                    else:
                        mat_num[iv_col.get() + 2][iv_fil.get()] = 2
                        mat_img[iv_col.get() + 2][iv_fil.get()].configure(image=vec_img[mat_num[iv_col.get() + 2][iv_fil.get()]])

                    mat_num[iv_col.get() + 1][iv_fil.get()] = 0
                    mat_img[iv_col.get() + 1][iv_fil.get()].configure(image=vec_img[mat_num[iv_col.get() + 1][iv_fil.get()]])
                    app.update()

        l_jugador.place(x=l_jugador.winfo_x() + 32, y=l_jugador.winfo_y())
        iv_col.set(iv_col.get() + 1)

    elif event.keysym == "Left" and mat_num[iv_col.get() - 1][iv_fil.get()] != 1 and mat_num[iv_col.get() - 1][iv_fil.get()] != 4:
        pasos.set(pasos.get()+1)
        if mat_num[iv_col.get() - 1][iv_fil.get()] == 2:
            if mat_num[iv_col.get() - 2][iv_fil.get()] == 1 or mat_num[iv_col.get() - 2][iv_fil.get()] == 4 or mat_num[iv_col.get() - 2][iv_fil.get()] ==2:
                return
            else:
                if mat_num[iv_col.get() - 2][iv_fil.get()] == 0 or mat_num[iv_col.get() - 2][iv_fil.get()] == 3:

                    if mat_num[iv_col.get() - 2][iv_fil.get()] == 3:
                        mat_num[iv_col.get() - 2][iv_fil.get()] = 4
                        mat_img[iv_col.get() - 2][iv_fil.get()].configure(image=vec_img[4])
                    else:
                        mat_num[iv_col.get() - 2][iv_fil.get()] = 2
                        mat_img[iv_col.get() - 2][iv_fil.get()].configure(image=vec_img[mat_num[iv_col.get() - 2][iv_fil.get()]])

                    mat_num[iv_col.get() - 1][iv_fil.get()] = 0
                    mat_img[iv_col.get() - 1][iv_fil.get()].configure(image=vec_img[mat_num[iv_col.get() - 1][iv_fil.get()]])
                    app.update()

        l_jugador.place(x=l_jugador.winfo_x() - 32, y=l_jugador.winfo_y())
        iv_col.set(iv_col.get() - 1)

    steps_label_var.set(f"Pasos: {pasos.get()}")
    
# PROGRAMA


app = Tk()
app.geometry("500x500")
app.title("Sokobahn")

iv_fil = IntVar()
iv_col = IntVar()
iv_col.set(4)
iv_fil.set(4)

mat_img = crea_matriz_img(10, 10)
mat_num = crea_matriz_num()
vec_img = crea_vector_img()


pasos=IntVar()
pasos.set(0)



crea_tablero_img(10, 10, mat_img, mat_num, vec_img)

l_jugador = ttk.Label(image=vec_img[5])
l_jugador.place(x=(32 * iv_col.get()) + 100, y=(32 * iv_fil.get()) + 100, width=32, height=32)

steps_label_var = StringVar()
steps_label_var.set(f"Pasos: {pasos.get()}")
steps_label = ttk.Label(textvariable=steps_label_var, font=('MathJax_SansSerif-Bold', 14, "bold")).pack()

app.bind("<Key>", movimiento_jugador)

app.mainloop()
