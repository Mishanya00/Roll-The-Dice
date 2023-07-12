from tkinter import *
from tkinter import ttk
import random, time


class Game(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.set_vars()
        self.geometry('800x700+400+50')
        self.title('Игра в кости. Сделай бросок!')
        self.resizable(height=False, width=False)
        self.iconphoto(True, PhotoImage(file=('iconka.png')))
        
        self.set_main_interface()

    def set_vars(self):
        self.first_kosti_launch = True
        self.sum_pl = 0
        self.sum_opp = 0
        self.score_pl = 0
        self.score_ai = 0

    def bros(self, key=1):
        x = random.choice(['b1.png', 'b2.png', 'b3.png', 'b4.png', 'b5.png', 'b6.png'])

        if key == 1:
            self.sum_pl += int(x[1])
        else:
            self.sum_opp += int(x[1])

        return x
    
    def first_init_player_kosti(self):

        self.labs = []
        for i in range(12):
            self.labs.append(Label(self))

        self.labs[0].place(relx=0.11, rely=0.66, anchor=CENTER)
        self.labs[1].place(relx=0.11, rely=0.83, anchor=CENTER)
        self.labs[2].place(relx=0.29, rely=0.66, anchor=CENTER)
        self.labs[3].place(relx=0.29, rely=0.83, anchor=CENTER)
        self.labs[4].place(relx=0.47, rely=0.66, anchor=CENTER)
        self.labs[5].place(relx=0.47, rely=0.83, anchor=CENTER)
        self.labs[6].place(relx=0.11, rely=0.16, anchor=CENTER)
        self.labs[7].place(relx=0.11, rely=0.33, anchor=CENTER)
        self.labs[8].place(relx=0.29, rely=0.16, anchor=CENTER)
        self.labs[9].place(relx=0.29, rely=0.33, anchor=CENTER)
        self.labs[10].place(relx=0.47, rely=0.16, anchor=CENTER)
        self.labs[11].place(relx=0.47, rely=0.33, anchor=CENTER)

    def roll_opponent(self):
        self.Turn_lbl = Label(text='бросок оппонента', bg='blue', fg='white', font=("Courier", 12), width=20)
        self.Turn_lbl.place(relx=0.7, rely=0.97)

        for i in range(18):

            self.sum_opp = 0
            self.b_opp = [PhotoImage(file=self.bros(0)) for i in range(6)]

            for j in range(6,12):                                   # [6;12] 12 - 6 = 6 cubics
                self.labs[j]['image'] = self.b_opp[j-6]

            self.update()
            time.sleep(0.08)

        time.sleep(1)

    def roll(self):
        self.a = PhotoImage(file=('defaul.png'))
        self.InfoLbl['image'] = self.a
        
        self.start_btn['state'] = 'disable'
        if self.first_kosti_launch:
            self.first_init_player_kosti()

        self.Score_pl['text'] = '0'
        self.Score_opp['text'] = '0'

        self.Turn_lbl = Label(text='бросок игрока', bg='blue', fg='white', font=("Courier", 12), width=20)
        self.Turn_lbl.place(relx=0.7, rely=0.97)

        for i in range(18):

            self.sum_pl = 0
            self.b = [PhotoImage(file=self.bros()) for i in range(6)]

            for j in range(6):
                self.labs[j]['image'] = self.b[j]

            self.update()
            time.sleep(0.08)

        self.Score_pl['text'] = f'{self.sum_pl}'
        time.sleep(2)

        self.roll_opponent()
        self.Score_opp['text'] = f'{self.sum_opp}'
        self.update()

        self.first_kosti_launch = False

        if self.sum_pl > self.sum_opp:
            self.score_pl += 1
            self.a = PhotoImage(file=('victory.png'))
            self.InfoLbl['image'] = self.a
        elif self.sum_opp > self.sum_pl:
            self.score_ai += 1
            self.a = PhotoImage(file=('lose.png'))
            self.InfoLbl['image'] = self.a
        else:
            self.a = PhotoImage(file=('draw.png'))
            self.InfoLbl['image'] = self.a

        self.ScoreMenu['text'] = f'{self.score_pl}:{self.score_ai}'
        self.start_btn['state'] = 'enable'

    def set_main_interface(self):
        self.font1 = PhotoImage(file=('table.png'))
        self.field = Label(self, image=self.font1)
        self.field.pack(side='left', fill='both', expand=True)

        self.RightMenu = Frame(bg='blue')
        self.RightMenu.pack(side=RIGHT, fill='both')

        self.ScoreMenu = Label(self.field, bg='black', fg='white', text='СЧЁТ: 0:0', font=('Verdana', 20), padx=20)
        self.ScoreMenu.pack(expand=True)

        self.a = PhotoImage(file=('defaul.png'))
        self.InfoLbl = Label(self.RightMenu, image=self.a)
        self.InfoLbl.pack(side=TOP)

        self.Score_opp = Label(self.RightMenu, text=f'{self.sum_opp}', bg='blue', fg='white', font=("Verdana", 36))
        self.Score_opp.pack(expand=True)

        self.Score_pl = Label(self.RightMenu, text=f'{self.sum_pl}', bg='blue', fg='white', font=("Verdana", 36))
        self.Score_pl.pack(side='bottom', expand=True)

        self.start_btn = ttk.Button(self.RightMenu, text="Бросить кубики", padding=10, command=self.roll)
        self.start_btn.pack(anchor=CENTER, expand=True)

root = Game()
root.mainloop()