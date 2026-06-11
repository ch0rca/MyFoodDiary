from tkinter import *
import tkinter.font as tkFont
import getUser
import tkinter.messagebox as msgbox
import mainScreen
import os

# database_id = " "
# token = " "
# calandar_address =" "

global count
def show_failed(id, reason):
    show_text = str
    global count
    if(count == 5):
        msgbox.showinfo("로그인 실패", "비밀번호 5회 오류!")
        exit(0)
    if(reason == "No ID in Database"):
        show_text = f"{count}회 오류\n{id}는 존재하지 않는 ID입니다.\n5회 오류시 프로그램이 종료됩니다."
    else:
        show_text = f"{count}회 오류\n비밀번호가 틀렸습니다.\n5회 오류시 프로그램이 종료됩니다."
    msgbox.showinfo("로그인 실패",show_text)
    return



def start_login_view():
    global count
    count = 0
    win = Tk()
    win.title("My Food Diary")
    win.geometry("900x600+100+100")
    win.config(bg='ivory')

    lab_d = Label(win)
    img = PhotoImage(file = "./photo/MyFoodDiaryImage.png", master = win)
    img = img.subsample(1)
    lab_d.config(image = img)
    lab_d.pack()

    lab = Label(win)
    lab.config(text = "My Food Diary", bg="ivory", fg="black", font=("배달의민족 한나는 열한살", 40,"bold"))

    lab.pack(pady=10)

    lab1 = Label(win)
    lab1.config(text = "ID", bg="ivory", fg="black", font=("배달의민족 한나는 열한살",25 ,"bold"))
    lab1.pack()

    ent1 = Entry(win)
    ent1.config(font=('배달의민족 한나는 열한살', 15),)
    ent1.pack()

    lab2 = Label(win)
    lab2.config(text = "Password", bg="ivory", fg="black", font=("배달의민족 한나는 열한살",25 ,"bold"))
    lab2.pack(pady=5)

    ent2 = Entry(win)
    ent2.config(show = "*")
    ent2.config(font=('배달의민족 한나는 열한살', 15),)
    ent2.pack()

    btn = Button(win)
    btn.config(font=('배달의민족 한나는 열한살', 15),bg="#DADAFC")
    btn.config(text = "Log in")
    def login():
        user_id = ent1.get()        #input ID
        user_pw = ent2.get()        #input PW
        request_body = getUser.checkIdandPW(user_id, user_pw, database_id, token)
        if(request_body["Request"] == "Failed"):
            global count
            count += 1
            show_failed(user_id, request_body["Reason"])
            return
        win.destroy()
        mainScreen.start_main_view(request_body["user_info"]["NAME"])
        
        
        
        
    #main view 이동
    btn.config(command = login)
    btn.pack(pady=10)
    win.mainloop()
    os.system("pause")
    
if __name__=="__main__":
    
    
    start_login_view()
    
