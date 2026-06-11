import random
import os
from PIL import ImageTk
from tkinter import *
import loadHistory as loadHis

# database_id = " "
# token = " "
# calandar_address = " "
global store_user_name

class FoodWorldCup:
    c0 = []
    c1 = -1
    c2 = []
    c4 = []
    c8 = []
    c16 = []
    c32 = []
    food_db = []
    f_cup = {}
    fname = []  # Food name
    rounds_num = {3: 32}

    list = os.listdir('./data')

    # Get the picture file name and mix it randomly
    def setting_db(self):
        for names in self.list:
            self.fname.append(names)
            random.shuffle(self.fname)

    # Initialize Values
    def setting_value(self):
        self.c1 = -1
        self.c2.clear()
        self.c4.clear()
        self.c8.clear()
        self.c16.clear()
        self.c32.clear()
        self.c0.clear()
        self.food_db.clear()
        self.fname.clear()
        self.f_cup = {1: self.c1, 2: self.c2, 4: self.c4, 8: self.c8, 16: self.c16, 32: self.c32}

    def final_view(self, round, original_db_number):
        get_name = lambda x: x.split('.')[0]  # Only file names
        self.f_cup[int(round / 2)] = original_db_number
        # Final Winner Display
        n = Tk()
        n.geometry("900x600+500+500")
        n.title("PhotoButton")
        n.config(bg="ivory")

        # Text
        label = Label(n, text='Food WorldCup', font=('Arial', 30), bg="ivory")
        label.place(x=310, y=20)
        winning_food = get_name(self.fname[self.f_cup[int(round / 2)]])
        label = Label(n, text=('The Winning Food : ' +  winning_food), font=('Arial', 15), fg='red', bg="ivory")
        label.place(x=330, y=65)

        # Picture
        food1 = './data/' + self.fname[self.f_cup[int(round / 2)]]

        self.photo2 = ImageTk.PhotoImage(file=food1, master=n)
        label2 = Label(n, image=self.photo2, width=400, height=400)
        label2.place(x=250, y=100)

        # Input (restaurant name)
        restaurant_label = Label(n, text='위 음식을 드신 식당 이름 입력',bg="ivory")
        restaurant_label.place(x=250, y=520)
        restaurant_name_entry = Entry(n, width=23)
        restaurant_name_entry.place(x=430, y=520)

        # Input (count star)
        star_label = Label(n, text='주고 싶은 별점 개수 입력                         예) 3 ',bg="ivory")
        star_label.place(x=250, y=548)
        count_star_entry = Entry(n, width=7)
        count_star_entry.place(x=540, y=548)

        def save_button():
            my_history = loadHis.HistoryFormat(food_name=winning_food, restaurant_name=restaurant_name_entry.get(), user_name=store_user_name,star_count=int(count_star_entry.get()))
            loadHis.addHistory(databaseID=calandar_database_id, token=token, history_info=my_history)
            n.destroy()
            #여기서는 메인뷰 띄우기

        # Button (save user input)
        savebutton = Button(n, text='Save', width=5, height=2, bg='green', fg='white', command=save_button)
        savebutton.place(x=603, y=521)
        return
        
    # Running WorldCup
    def select_items(self, round):
        get_name = lambda x: x.split('.')[0]  # Only file names
        random.shuffle(self.f_cup[round])  # Mix the values of the list randomly
        for i in range(0, round, 2):

            def btnpress():  # Functions executed by pressing the left button

                original_db_number = self.f_cup[round][i]  # User selects left picture

                if round == 2:  # In final
                    self.final_view(round, original_db_number)
                else:  # Not final
                    # Append the results selected in the current round to the list in the next round
                    self.f_cup[int(round / 2)].append(original_db_number)

                w.destroy()


            def btnpress2():  # Functions executed by pressing the right button

                original_db_number = self.f_cup[round][i + 1]  # User selects right picture

                if round == 2:  # Final
                    self.final_view(round, original_db_number)
                else:  # Not Final
                    # Append the results selected in the current round to the list in the next round
                    self.f_cup[int(round / 2)].append(original_db_number)

                w.destroy()

            # Food WorldCup Display
            w = Tk()
            w.geometry("900x600+500+500")
            w.title("Food WorldCup")
            w.config(bg="ivory")

            # Text
            label = Label(w, text='Food World Cup', font=('Arial', 30), bg="ivory",fg="black")
            label.place(x=310, y=20)
            label = Label(w, text=("{}강".format(round)), font=('Arial', 15), bg="ivory",fg="black")
            label.place(x=430, y=280)

            # Left Picture
            food1 = './data/' + self.fname[self.f_cup[round][i]]

            photo = PhotoImage(file=food1)
            photo = photo.subsample(10)
            btn = Button(w, image=photo, text=get_name(self.fname[self.f_cup[round][i]]), compound="top",bg="ivory")
            btn.config(width=400, height=450, font=('Arial', 30),)
            btn.pack(side="left")
            btn.config(command=btnpress)

            # Right Picture
            food2 = './data/' + self.fname[self.f_cup[round][i + 1]]

            photo2 = PhotoImage(file=food2)
            photo2 = photo2.subsample(10)
            btn2 = Button(w, image=photo2, text=get_name(self.fname[self.f_cup[round][i+1]]), font=('Arial', 30), compound="top",bg="ivory")
            btn2.config(width=400, height=450)
            btn2.pack(side="right")
            btn2.config(command=btnpress2)

            w.mainloop()

        if round != 2:
            round = int(round / 2)
            self.select_items(round)

    # Round setting
    def setting(self):  # Initialization
        self.setting_value()  # Initialize values
        self.setting_db()  # Initialize Food_DB
        rounds = self.rounds_num[3]
        for round in range(rounds):
            self.c0.append(round)
        self.f_cup[rounds] = self.c0  # Initialized values
        self.select_items(rounds)

    # Start
    def start(self):
        self.setting()
        
        
def load_food_world_cup(user_name):
    food_world_cup = FoodWorldCup()
    global store_user_name
    store_user_name = user_name
    food_world_cup.start()
    
if __name__=="__main__":
    a = FoodWorldCup()
    a.start()

