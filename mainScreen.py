from tkinter import *
from PIL import ImageTk, Image
import random
import os
import showCalendar 
import FoodWorldCup

calandar_address ="https://piquant-beanie-c1b.notion.site/1eaa55f6df2842e8a7118be81ba1fdb3?v=060be0ea1bd04520a077457781038930"

#def FoodWorldcup() :

    
#def FoodCalendar() :


path = './data'
lst = os.listdir(path)
random.shuffle(lst)
global store_user_name



def rand_food(win):
    global img_r
    
    img_r = PhotoImage(file = f"./data/{lst[0]}", master=win)      #Get photo from food photos directory
    lab_r = Label(win, width=350, height=350)
    lab_r.config(image = img_r)
    lab_r.place(x=270, y=240)

    foodName = lst[0].replace('.png', '')                                       #Get food name from file name 
    lab_n = Label(win, text = foodName, font=("배달의민족 한나는 열한살", 20), bg = '#FFD6AA')
    lab_n.place(x=650, y=560)
    #lab_r.pack()

def start_main_view(user_name):
    global store_user_name
    store_user_name = user_name
    win = Tk()
    win.title("MyFoodDiary Main")
    win.geometry("900x600+100+100")
    win.config(bg='ivory')
    


    lab_i = Label(win)
    img = PhotoImage(file = "./photo/MFD.png", master=win)            #MyFoodDiary title photo
    img = img.subsample(2)
    lab_i.config(image = img)
    lab_i.pack()
    
    def launch_food_world_cup():
        win.destroy()
        FoodWorldCup.load_food_world_cup(store_user_name)
        start_main_view(store_user_name)
        

    def launch_calendar():
        showCalendar.openWeb(calandar_address)

    bt1 = Button(win, text="Food\nWorldcup", command=launch_food_world_cup) #, command=FoodWorldcup)       add command to run FoodWorldcup
    bt1.config(width=400, height=450, font=('배달의민족 한나는 열한살', 30),)
    bt1.config(bg='#D18063')
    
     
        
    bt2 = Button(win, text="Food\nCalendar",command=launch_calendar) # add command to run FoodCalendar
    bt2.config(width=400, height=450, font=('배달의민족 한나는 열한살', 30),)
    bt2.config(bg='#F9D9CA')


    bt1.place(x=50, y=60, width=370, height=150)
    bt2.place(x=480, y=60, width=370, height=150)


    lab_fr = Label(text = "Today's Menu", font=("배달의민족 한나는 열한살", 20), bg = '#FFD6AA')
    lab_fr.place(x=0, y=220)
    rand_food(win)
    win.mainloop()

if __name__=="__main__":
    start_main_view("hello")




