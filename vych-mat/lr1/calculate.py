from tkinter import *
import math

def f(x):
    f = x**2
    return f

def defparaboly():
    global dana, danb, dann
    windowparabol = Tk()
    windowparabol.title("Метод парабол")
    windowparabol.geometry('1500x1000')
    windowparabol.configure(bg='#D3D3D3')
    lblparabol = Label(windowparabol, text="Введите данные для метода парабол", font=("Cambria", 45), bg='#D3D3D3')
    lblparabol.place(relx=.500, rely=.1, anchor=CENTER)

    lbldana = Label(windowparabol, text='Введите нижнюю границу:', font=("Consolas", 20), bg='#D3D3D3')
    lbldana.place(relx=.400, rely=.3, anchor=CENTER)
    dana = Entry(windowparabol, width=30)
    dana.place(relx=.650, rely=.3, anchor=CENTER)

    lbldanb = Label(windowparabol, text='Введите верхнюю границу:', font=("Consolas", 20), bg='#D3D3D3')
    lbldanb.place(relx=.400, rely=.4, anchor=CENTER)
    danb = Entry(windowparabol, width=30)
    danb.place(relx=.650, rely=.4, anchor=CENTER)

    lbldann = Label(windowparabol, text='Введите количество разбиений:', font=("Consolas", 20), bg='#D3D3D3')
    lbldann.place(relx=.400, rely=.5, anchor=CENTER)
    dann = Entry(windowparabol, width=30)
    dann.place(relx=.650, rely=.5, anchor=CENTER)

    reshparabolbut = Button(windowparabol, text='Получить ответ', font=("Consolas", 13), bg='#A9A9A9', command=reshparabol)
    reshparabolbut.place(relx=.500, rely=.7, anchor=CENTER)

    windowparabol.mainloop()

def reshparabol():
    a = float(dana.get())
    b = float(danb.get())
    n = int(dann.get())
    #r = 0
    h = (b - a) / n
    r0 = f(a)
    rmax = f(b)
    x = a + h
    s1 = 0
    s2 = 0
    while x <= (b-h):
        s1 = s1 + f(x)
        x = x + 2*h
    x = a + 2*h
    while x <= (b-2*h):
        s2 = s2 + f(x)
        x = x + 2*h
    r = (h/3) * (r0 + 4*s1 + 2*s1 + rmax)
    print(f"Разбиений: {n}. Постоянный шаг. Метод парабол. Ответ: ", r)

def deftrapecy():
    global dana, danb, dann
    windowtrapecy = Tk()
    windowtrapecy.title("Метод трапеций")
    windowtrapecy.geometry('1500x1000')
    windowtrapecy.configure(bg='#D3D3D3')
    lbltrapecy = Label(windowtrapecy, text="Введите данные для метода трапеций", font=("Cambria", 45), bg='#D3D3D3')
    lbltrapecy.place(relx=.500, rely=.1, anchor=CENTER)

    lbldana = Label(windowtrapecy, text='Введите нижнюю границу:', font=("Consolas", 20), bg='#D3D3D3')
    lbldana.place(relx=.400, rely=.3, anchor=CENTER)
    dana = Entry(windowtrapecy, width=30)
    dana.place(relx=.650, rely=.3, anchor=CENTER)

    lbldanb = Label(windowtrapecy, text='Введите верхнюю границу:', font=("Consolas", 20), bg='#D3D3D3')
    lbldanb.place(relx=.400, rely=.4, anchor=CENTER)
    danb = Entry(windowtrapecy, width=30)
    danb.place(relx=.650, rely=.4, anchor=CENTER)

    lbldann = Label(windowtrapecy, text='Введите количество разбиений:', font=("Consolas", 20), bg='#D3D3D3')
    lbldann.place(relx=.400, rely=.5, anchor=CENTER)
    dann = Entry(windowtrapecy, width=30)
    dann.place(relx=.650, rely=.5, anchor=CENTER)

    reshtrapecybut = Button(windowtrapecy, text='Получить ответ', font=("Consolas", 13), bg='#A9A9A9', command=reshtrapecy)
    reshtrapecybut.place(relx=.500, rely=.7, anchor=CENTER)

    windowtrapecy.mainloop()

def reshtrapecy():
    a = float(dana.get())
    b = float(danb.get())
    n = int(dann.get())
    r = 0
    h = (b - a) / n
    x = a + h
    while x < (b-h):
        r = r + ((f(x) + f(x+h))/2)
        x = x + h
    r = h * (((f(a) + f(b))/2) + r)
    print(f"Разбиений: {n}. Постоянный шаг. Метод трапеций. Ответ: ", r)

def defpramprav():
    global dana, danb, dann
    windowpramprav = Tk()
    windowpramprav.title("Метод прямоугольников правых частей")
    windowpramprav.geometry('1500x1000')
    windowpramprav.configure(bg='#D3D3D3')
    lblpramprav = Label(windowpramprav, text="Введите данные для метода прямоугольников правых частей", font=("Cambria", 40), bg='#D3D3D3')
    lblpramprav.place(relx=.500, rely=.1, anchor=CENTER)

    lbldana = Label(windowpramprav, text='Введите нижнюю границу:', font=("Consolas", 20), bg='#D3D3D3')
    lbldana.place(relx=.400, rely=.3, anchor=CENTER)
    dana = Entry(windowpramprav, width=30)
    dana.place(relx=.650, rely=.3, anchor=CENTER)

    lbldanb = Label(windowpramprav, text='Введите верхнюю границу:', font=("Consolas", 20), bg='#D3D3D3')
    lbldanb.place(relx=.400, rely=.4, anchor=CENTER)
    danb = Entry(windowpramprav, width=30)
    danb.place(relx=.650, rely=.4, anchor=CENTER)

    lbldann = Label(windowpramprav, text='Введите количество разбиений:', font=("Consolas", 20), bg='#D3D3D3')
    lbldann.place(relx=.400, rely=.5, anchor=CENTER)
    dann = Entry(windowpramprav, width=30)
    dann.place(relx=.650, rely=.5, anchor=CENTER)

    reshprampravbut = Button(windowpramprav, text='Получить ответ', font=("Consolas", 13), bg='#A9A9A9', command=reshpramprav)
    reshprampravbut.place(relx=.500, rely=.7, anchor=CENTER)

    windowpramprav.mainloop()

def reshpramprav():
    a = float(dana.get())
    b = float(danb.get())
    n = int(dann.get())
    r = 0
    h = (b - a) / n
    x = a + h
    while x < b:
        r = r + f(x)
        x = x + h
    m = h * r
    print(f"Разбиений: {n}. Постоянный шаг. Метод прямоугольников правых частей. Ответ: ", m)

def defpramlev():
    global dana, danb, dann
    windowpramlev = Tk()
    windowpramlev.title("Метод прямоугольников левых частей")
    windowpramlev.geometry('1500x1000')
    windowpramlev.configure(bg='#D3D3D3')
    lblpramlev = Label(windowpramlev, text="Введите данные для метода прямоугольников левых частей", font=("Cambria", 40), bg='#D3D3D3')
    lblpramlev.place(relx=.500, rely=.1, anchor=CENTER)

    lbldana = Label(windowpramlev, text='Введите нижнюю границу:', font=("Consolas", 20), bg='#D3D3D3')
    lbldana.place(relx=.400, rely=.3, anchor=CENTER)
    dana = Entry(windowpramlev, width=30)
    dana.place(relx=.650, rely=.3, anchor=CENTER)

    lbldanb = Label(windowpramlev, text='Введите верхнюю границу:', font=("Consolas", 20), bg='#D3D3D3')
    lbldanb.place(relx=.400, rely=.4, anchor=CENTER)
    danb = Entry(windowpramlev, width=30)
    danb.place(relx=.650, rely=.4, anchor=CENTER)

    lbldann = Label(windowpramlev, text='Введите количество разбиений:', font=("Consolas", 20), bg='#D3D3D3')
    lbldann.place(relx=.400, rely=.5, anchor=CENTER)
    dann = Entry(windowpramlev, width=30)
    dann.place(relx=.650, rely=.5, anchor=CENTER)

    reshpramlevbut = Button(windowpramlev, text='Получить ответ', font=("Consolas", 13), bg='#A9A9A9', command=reshpramlev)
    reshpramlevbut.place(relx=.500, rely=.7, anchor=CENTER)

    windowpramlev.mainloop()

def reshpramlev():
    a = float(dana.get())
    b = float(danb.get())
    n = int(dann.get())
    r = 0
    h = (b - a) / n
    x = a
    while x < (b - h):
        r = r + f(x)
        x = x + h
    m = h * r
    print(f"Разбиений: {n}. Постоянный шаг. Метод прямоугольников левых частей. Ответ: ", m)

def metody():
    windowmetody = Tk()
    windowmetody.title("Методы интегрирования")
    windowmetody.geometry('1500x1000')
    windowmetody.configure(bg='#D3D3D3')
    lblmetody = Label(windowmetody, text="Выберите метод интегрирования", font=("Cambria", 45), bg='#D3D3D3')
    lblmetody.place(relx=.500, rely=.1, anchor=CENTER)

    pramlevbut = Button(windowmetody, text="Метод прямоугольника левых частей", font=("Consolas", 13), bg='#A9A9A9', command=defpramlev)
    pramlevbut.place(relx=.500, rely=.3, anchor=CENTER)

    prampravbut = Button(windowmetody, text="Метод прямоуголька правых частей", font=("Consolas", 13), bg='#A9A9A9', command=defpramprav)
    prampravbut.place(relx=.500, rely=.4, anchor=CENTER)

    trapecybut = Button(windowmetody, text="Метод трапеций", font=("Consolas", 13), bg='#A9A9A9', command=deftrapecy)
    trapecybut.place(relx=.500, rely=.5, anchor=CENTER)

    parabolybut = Button(windowmetody, text="Метод парабол", font=("Consolas", 13), bg='#A9A9A9', command=defparaboly)
    parabolybut.place(relx=.500, rely=.6, anchor=CENTER)

    windowmetody.mainloop()

def peremenshagy():
    windowperemshagy = Tk()
    windowperemshagy.title("Интегрирование с переменным шагом")
    windowperemshagy.geometry('1500x1000')
    windowperemshagy.configure(bg='#D3D3D3')
    lblperemshagy = Label(windowperemshagy, text="Выберите алгоритм", font=("Cambria", 45), bg='#D3D3D3')
    lblperemshagy.place(relx=.500, rely=.1, anchor=CENTER)

    peremshagybut1 = Button(windowperemshagy, text="1 алгоритм", font=("Consolas", 13), bg='#A9A9A9', command=danperemshagy1)
    peremshagybut1.place(relx=.500, rely=.3, anchor=CENTER)
    peremshagybut2 = Button(windowperemshagy, text="2 алгоритм", font=("Consolas", 13), bg='#A9A9A9', command=danperemshagy2)
    peremshagybut2.place(relx=.500, rely=.4, anchor=CENTER)

    windowperemshagy.mainloop()

def danperemshagy1():
    global dana, danb, dann
    danperemshagy1window = Tk()
    danperemshagy1window.title("Данные для переменного шага. Алгоритм №1")
    danperemshagy1window.geometry('1500x1000')
    danperemshagy1window.configure(bg='#D3D3D3')
    lbldanperemshagy1 = Label(danperemshagy1window, text="Введите данные для интеграла с переменным шагом", font=("Cambria", 45), bg='#D3D3D3')
    lbldanperemshagy1.place(relx=.500, rely=.1, anchor=CENTER)

    lbldana = Label(danperemshagy1window, text="Введите нижний предел:", font=("Consolas", 20), bg='#D3D3D3')
    lbldana.place(relx=.400, rely=.3, anchor=CENTER)
    dana = Entry(danperemshagy1window, width=30)
    dana.place(relx=.650, rely=.3, anchor=CENTER)

    lbldanb = Label(danperemshagy1window, text="Введите верхний предел:", font=("Consolas", 20), bg='#D3D3D3')
    lbldanb.place(relx=.400, rely=.4, anchor=CENTER)
    danb = Entry(danperemshagy1window, width=30)
    danb.place(relx=.650, rely=.4, anchor=CENTER)

    lbldann = Label(danperemshagy1window, text="Введите количество разбиений:", font=("Consolas", 20), bg='#D3D3D3')
    lbldann.place(relx=.400, rely=.5, anchor=CENTER)
    dann = Entry(danperemshagy1window, width=30)
    dann.place(relx=.650, rely=.5, anchor=CENTER)

    reshperemshagybut1 = Button(danperemshagy1window, text="Получить ответ", font=("Consolas", 13), bg='#A9A9A9', command=reshpershagy1)
    reshperemshagybut1.place(relx=.500, rely=.7, anchor=CENTER)

    danperemshagy1window.mainloop()

def reshpershagy1():
    a = float(dana.get())
    b = float(danb.get())
    n = int(dann.get())
    E = 0.001
    h = (b - a) / n
    IN = 0
    S2 = 0
    x = a
    S2 = S2 + f(x)
    x = x + h
    while x <= b - h:
        S2 = S2 + f(x)
        x = x + h
    ans = h * S2
    cur = abs(ans - IN)
    IN = ans
    h = h / 2
    while cur > E:
        ans = 0
        x = a + h / 2
        while x <= b - h:
            ans = ans + f(x)
            x = x + h
        ans = h / 2 * (S2 + 2 * ans)
        cur = abs(ans - IN)
        IN = ans
        h = h / 2
    print("Переменный шаг. 1 алгоритм. Ответ: ", ans)

def danperemshagy2():
    global dana, danb, dann
    danperemshagy2window = Tk()
    danperemshagy2window.title("Данные для переменного шага. Алгоритм №2")
    danperemshagy2window.geometry('1500x1000')
    danperemshagy2window.configure(bg='#D3D3D3')
    lbldanperemshagy2 = Label(danperemshagy2window, text="Введите данные для интеграла с переменным шагом", font=("Cambria", 45), bg='#D3D3D3')
    lbldanperemshagy2.place(relx=.500, rely=.1, anchor=CENTER)

    lbldana = Label(danperemshagy2window, text = "Введите нижний предел:", font=("Consolas", 20), bg='#D3D3D3')
    lbldana.place(relx=.400, rely=.3, anchor=CENTER)
    dana = Entry(danperemshagy2window, width=30)
    dana.place(relx=.650, rely=.3, anchor=CENTER)

    lbldanb = Label(danperemshagy2window, text="Введите верхний предел:", font=("Consolas", 20), bg='#D3D3D3')
    lbldanb.place(relx=.400, rely=.4, anchor=CENTER)
    danb = Entry(danperemshagy2window, width=30)
    danb.place(relx=.650, rely=.4, anchor=CENTER)

    lbldann = Label(danperemshagy2window, text="Введите количество разбиений:", font=("Consolas", 20), bg='#D3D3D3')
    lbldann.place(relx=.400, rely=.5, anchor=CENTER)
    dann = Entry(danperemshagy2window, width=30)
    dann.place(relx=.650, rely=.5, anchor=CENTER)

    reshperemshagybut2 = Button(danperemshagy2window, text="Получить ответ", font=("Consolas", 13), bg='#A9A9A9', command=reshpershagy2)
    reshperemshagybut2.place(relx=.500, rely=.7, anchor=CENTER)

    danperemshagy2window.mainloop()

def reshpershagy2():
    a = float(dana.get())
    b = float(danb.get())
    n = int(dann.get())
    E = 0.001
    h = (b-a) / n
    hv = h
    integral = 0
    r = 1000
    s1 = 0
    s = 0
    h1 = 0
    while r > E:
        x = a + h1
        while x <= (b - h):
            s = s + f(x)
            x = x + hv
        s1 = s * h
        r = abs(s1 - integral)
        integral = s1
        hv = h
        h = h / 2
        h1 = h
    print(f'Ответ: {s1} при шаге {2 * hv}')

def kratny():
    global dana, danb, danc, dand, dannx, danny
    windowkratny = Tk()
    windowkratny.title("Кратный интеграл")
    windowkratny.geometry('1500x1000')
    windowkratny.configure(bg='#D3D3D3')
    lblkratny = Label(windowkratny, text="Введите данные для кратного интеграла", font=("Cambria", 50), bg='#D3D3D3')
    lblkratny.place(relx=.500, rely=.1, anchor=CENTER)

    lbldana = Label(windowkratny, text="Введите первый нижний предел:", font=("Consolas", 20), bg='#D3D3D3')
    lbldana.place(relx=.400, rely=.2, anchor=CENTER)
    dana = Entry(windowkratny, width=30)
    dana.place(relx=.650, rely=.2, anchor=CENTER)

    lbldanb = Label(windowkratny, text="Введите первый верхний предел:", font=("Consolas", 20), bg='#D3D3D3')
    lbldanb.place(relx=.400, rely=.3, anchor=CENTER)
    danb = Entry(windowkratny, width=30)
    danb.place(relx=.650, rely=.3, anchor=CENTER)

    lbldanc = Label(windowkratny, text="Введите первый нижний предел:", font=("Consolas", 20), bg='#D3D3D3')
    lbldanc.place(relx=.400, rely=.4, anchor=CENTER)
    danc = Entry(windowkratny, width=30)
    danc.place(relx=.650, rely=.4, anchor=CENTER)

    lbldand = Label(windowkratny, text="Введите первый верхний предел:", font=("Consolas", 20), bg='#D3D3D3')
    lbldand.place(relx=.400, rely=.5, anchor=CENTER)
    dand = Entry(windowkratny, width=30)
    dand.place(relx=.650, rely=.5, anchor=CENTER)

    lbldannx = Label(windowkratny, text="Введите количество разбиений по х:", font=("Consolas", 20), bg='#D3D3D3')
    lbldannx.place(relx=.400, rely=.6, anchor=CENTER)
    dannx = Entry(windowkratny, width=30)
    dannx.place(relx=.650, rely=.6, anchor=CENTER)

    lbldanny = Label(windowkratny, text="Введите количество разбиений по у:", font=("Consolas", 20), bg='#D3D3D3')
    lbldanny.place(relx=.400, rely=.7, anchor=CENTER)
    danny = Entry(windowkratny, width=30)
    danny.place(relx=.650, rely=.7, anchor=CENTER)

    reshkratbut = Button(windowkratny, text="Получить ответ", font=("Consolas", 13), bg='#A9A9A9', command=reshkrat)
    reshkratbut.place(relx=.500, rely=.8, anchor=CENTER)

    windowkratny.mainloop()

def reshkrat():
    def ff(x, y):
        #return math.sin(x + y)
        return x**2+y**2

    def com_integral(a, b, c, d, nx, ny):
        hx = (b - a) / nx
        hy = (d - c) / ny
        SX = 0
        for i in range(nx):
            x_i = a + i * hx
            for j in range(ny):
                y_j = c + j * hy
                f_ij = ff(x_i, y_j)
                SX += f_ij * hx * hy
        print("Значение кратного интеграла = ", SX)
    a = float(dana.get())
    b = float(danb.get())
    c = float(danc.get())
    d = float(dand.get())
    nx = int(dannx.get())
    ny = int(danny.get())
    # a = 0
    # b = math.pi / 2
    # c = 0
    # d = math.pi / 4
    #nx = 10000
    #ny = 10000
    com_integral(a, b, c, d, nx, ny)

def shagy():
    windowshagy = Tk()
    windowshagy.title("Шаги интегрирования")
    windowshagy.geometry('1500x1000')
    windowshagy.configure(bg='#D3D3D3')
    lbl1 = Label(windowshagy, text="Выберите какой вид интегрирования", font=("Cambria", 50), bg='#D3D3D3')
    lbl1.place(relx=.500, rely=.1, anchor=CENTER)
    postshagbut = Button(windowshagy, text="С постоянным шагом", font=("Bahnschrift Light", 13), bg='#A9A9A9', command=metody)
    postshagbut.place(relx=.500, rely=.3, anchor=CENTER)
    permshagbut = Button(windowshagy, text="C переменным шагом", font=("Bahnschrift Light", 13), bg='#A9A9A9', command=peremenshagy)
    permshagbut.place(relx=.500, rely=.4, anchor=CENTER)
    kratnyintegralbut = Button(windowshagy, text='Кратный интеграл', font=("Bahnschrift Light", 13), bg='#A9A9A9', command=kratny)
    kratnyintegralbut.place(relx=.500, rely=.5, anchor=CENTER)
    windowshagy.mainloop()

windowglavnoe = Tk()
windowglavnoe.title("Добро пожаловать в калькулятор!")
windowglavnoe.geometry('1500x1000')
windowglavnoe.configure(bg='#D3D3D3')
lbl = Label(windowglavnoe, text="Выберите тип задачи", font=("Cambria", 50), bg='#D3D3D3')
lbl.place(relx=.500, rely=.1, anchor=CENTER)
chislinbut = Button(windowglavnoe, text="Численное интегрирование", font=("Bahnschrift Light", 13), bg='#A9A9A9', command=shagy)
chislinbut.place(relx=.500, rely=.3, anchor=CENTER)
nelinuravbut = Button(windowglavnoe, text="Нелинейное уравнение", font=("Bahnschrift Light", 13), bg='#A9A9A9')
nelinuravbut.place(relx=.500, rely=.4, anchor=CENTER)
linuravbut = Button(windowglavnoe, text="Линейное уравнение", font=("Bahnschrift Light", 13), bg='#A9A9A9')
linuravbut.place(relx=.500, rely=.5, anchor=CENTER)

windowglavnoe.mainloop()