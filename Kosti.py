from tkinter import *
from tkinter import ttk
import random, time


#####################################
#### MODULES MODULES MODULES     ####
#####################################

def bros(key=1):
    global sum_pl, sum_opp

    x = random.choice(['b1.png', 'b2.png', 'b3.png', 'b4.png', 'b5.png', 'b6.png'])

    if key == 1:
        sum_pl += int(x[1])
    else:
        sum_opp += int(x[1])

    return x


def first_init_player_kosti():
    global labs

    labs = []
    for i in range(6):
        labs.append(Label(root))

    labs[0].place(relx=0.11, rely=0.66, anchor=CENTER)
    labs[1].place(relx=0.11, rely=0.83, anchor=CENTER)
    labs[2].place(relx=0.29, rely=0.66, anchor=CENTER)
    labs[3].place(relx=0.29, rely=0.83, anchor=CENTER)
    labs[4].place(relx=0.47, rely=0.66, anchor=CENTER)
    labs[5].place(relx=0.47, rely=0.83, anchor=CENTER)


def first_init_opponent_kosti():
    global labs2

    labs2 = []
    for i in range(6):
        labs2.append(Label(root))

    labs2[0].place(relx=0.11, rely=0.16, anchor=CENTER)
    labs2[1].place(relx=0.11, rely=0.33, anchor=CENTER)
    labs2[2].place(relx=0.29, rely=0.16, anchor=CENTER)
    labs2[3].place(relx=0.29, rely=0.33, anchor=CENTER)
    labs2[4].place(relx=0.47, rely=0.16, anchor=CENTER)
    labs2[5].place(relx=0.47, rely=0.33, anchor=CENTER)


def roll_opponent():
    global b_opp, start_btn, sum_opp

    if first_kosti_launch:
        first_init_opponent_kosti()

    Turn_lbl = Label(text='бросок оппонента', bg='blue', fg='white', font=("Courier", 12), width=20)
    Turn_lbl.place(relx=0.7, rely=0.97)

    for i in range(18):

        sum_opp = 0
        b_opp = [PhotoImage(file=bros(0)) for i in range(6)]
        for j in range(6):
            labs2[j]['image'] = b_opp[j]

        root.update()
        time.sleep(0.08)

    time.sleep(1)


def roll():
    global b, start_btn, first_kosti_launch, sum_pl, score_pl, score_ai, a

    a = PhotoImage(file=('defaul.png'))
    InfoLbl['image'] = a
    
    start_btn['state'] = 'disable'
    if first_kosti_launch:
        first_init_player_kosti()

    Score_pl['text'] = '0'
    Score_opp['text'] = '0'

    Turn_lbl = Label(text='бросок игрока', bg='blue', fg='white', font=("Courier", 12), width=20)
    Turn_lbl.place(relx=0.7, rely=0.97)

    for i in range(18):

        sum_pl = 0
        b = [PhotoImage(file=bros()) for i in range(6)]

        for j in range(6):
            labs[j]['image'] = b[j]

        root.update()
        time.sleep(0.08)

    Score_pl['text'] = f'{sum_pl}'
    time.sleep(2)

    roll_opponent()
    Score_opp['text'] = f'{sum_opp}'
    root.update()

    first_kosti_launch = False

    if sum_pl > sum_opp:
        score_pl += 1
        a = PhotoImage(file=('victory.png'))
        InfoLbl['image'] = a
    elif sum_opp > sum_pl:
        score_ai += 1
        a = PhotoImage(file=('lose.png'))
        InfoLbl['image'] = a
    else:
        a = PhotoImage(file=('draw.png'))
        InfoLbl['image'] = a

    ScoreMenu['text'] = f'{score_pl}:{score_ai}'
    start_btn['state'] = 'enable'


#####################################
#### CLIENT CLIENT CLIENT CLIENT ####
#####################################


first_kosti_launch = True
sum_pl = 0
sum_opp = 0
score_pl = 0
score_ai = 0


#Main Window
root = Tk()
root.geometry('800x700+400+50')
root.title('Игра в кости. Сделай бросок!')
root.resizable(height=False, width=False)  ### CHANGE TO FALSE!!!!!!!!!!!!!!!
root.iconphoto(True, PhotoImage(file=('iconka.png')))

# f_top = Frame(root)
font1 = PhotoImage(file=('table.png'))
Label(image=font1).pack(side=LEFT, anchor=W, padx=0)

RightMenu = Label(root, height=700, width=300, bg="blue", padx=0)
RightMenu.pack(side=TOP, anchor=E, padx=0)

ScoreMenu = Label(root, bg='black', fg='white', text='СЧЁТ: 0:0', font=('Verdana', 20))
ScoreMenu.place(x=0, y=325, width=500, height=50)

a = PhotoImage(file=('defaul.png'))
InfoLbl = Label(image=a)
InfoLbl.place(x=500, y=0)

Score_pl = Label(text=f'{sum_pl}', bg='blue', fg='white', font=("Verdana", 36))
Score_pl.place(x=625, y=500)

Score_opp = Label(text=f'{sum_opp}', bg='blue', fg='white', font=("Verdana", 36))
Score_opp.place(x=625, y=200)

start_btn = ttk.Button(text="Бросить кубики", padding=10, command=roll)
start_btn.place(relx=0.73, rely=0.47)
# root.bind('<1>', img)


root.mainloop()
