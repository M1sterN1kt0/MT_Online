from bs4 import BeautifulSoup
import requests
from tkinter import *


def lists():
    global servers, online_players, summa
    response = requests.get('https://kttc.ru/wot/ru/info/servers-online/')
    soup = BeautifulSoup(response.content, 'lxml')
    classfound = soup.find_all(class_='w50')
    classfoundR = classfound[1]

    for div in classfoundR.find_all('div'):
        if 'Количество игроков онлайн:' in div.text:
            if int(div.find('b').text) != 0:
                online_players.append(int(div.find('b').text))
            else:
                online_players.append('Сервер отключен!')
        elif 'Сервер:' in div.text:
            servers.append(div.find('b').text)
            
    summa = sum(online_players)


def place():
    global servers, online_players, summa
    lists()
    for i in range(len(servers)):
        serv_widget = Message(text=f'Сервер: {servers[i]}', font=('Arial', 14),width=200, bg='#17191a', fg='#c4c4c4') 
        serv_widget.place(x=20,y=110+70*(i-1))
        online_widget = Message(text=f'Онлайн: {online_players[i]}', font=('Arial', 14),width=200, bg='#17191a', fg='#c4c4c4')
        online_widget.place(x=20,y=140+70*(i-1))
    S_online = Label(text=f'Общий онлайн на серверах:\n\n {summa}', font=('Arial', 24), bg='#17191a', fg='#c4c4c4')
    S_online.place(x=270,y=220)
    servers = []
    online_players = []
    summa = 0
    timer()
    window.after(10000,place)

def timer():
    global time
    time_widget = Label(text=f'Информация будет обновленна через {time} сек.  ', font=('Arial', 14), bg='#17191a', fg='#c4c4c4')
    waiting_widget = Label(text='Информация обновляется', font=('Arial', 16), bg='#17191a', fg='#c4c4c4')
    time_widget.place(x=270,y=440)
    waiting_widget.place(x=300,y=440)
    waiting_widget.place_forget()
    if time > 0:
        time-=1
        window.after(1000,timer)
    else:
        time = 10
        time_widget.place_forget()
        waiting_widget.place(x=300,y=440)


servers = []
online_players = []
summa = 0
time = 10


window = Tk()
window.geometry('800x600')
window.title('Онлайн Мира Танков')
window.config(bg='#17191a')
window.resizable(width=False, height=False)


headline = Label(text='Онлайн "Мира Танков"', font=('Arial', 30), bg='#17191a', fg='#c4c4c4', justify=CENTER)
headline.pack()

place()


window.mainloop()