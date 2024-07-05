from telethon.sync import TelegramClient
import time
import pyautogui as pg
import sqlite3
import requests

# print('Путь до файла')
# path = input()
print('ВВедите x координату')
x = int(input())
print('ведите y координату')
y = int(input())
api_id = 1234567
api_hash = 'your hash'
client = TelegramClient('BOTFORME', api_id,
                        api_hash)  # создаем клиент для входа нашей програмы в на аккаунт
client.start()  # запускаем клиент

dlgs = client.get_dialogs()  # получаем все наши названия каналов, групп в которых мы состоим
for dlg in dlgs:
    if dlg.title == 'LTC Click Bot':
        btc = dlg  # находим нужный диалог и записывем его данные в переменную


def get_t(s):  # функция для получения числа из строки
    l = len(s)
    integ = 30
    i = 0
    while i < l:
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            return int(s_int)


i = 0


def send_msg_to_work():  # функция отправки сообщений к ботту для посещения сайтов
    global i
    client.send_message('LTC Click Bot', '📣 Join chats')  # отправляем команду к боту
    i += 1
    time.sleep(1)  # ждем пока бот обработает наш запрос и отправит ссылку
    get_msg = client.get_messages(btc, limit=1)  # получаем сообщение которое нам отослал бот
    get_msg[0].click(0)  # нажымаем кнопку с ссылкой в сообщении бота. По ней нас отправляет на сайт
    time.sleep(2.5)  # ждем  прогрузки всех елементов сайта
    # но я решил не заморачивться и просто кликать на капчу и не проверять ее наличие на дынном сайте
    time.sleep(3.5)
    pg.click(x, y)
    # 765 705
    get_msg = client.get_messages(btc, limit=1)
    get_msg[0].click(1)
    time.sleep(1)  # задерживаем скрипт


#    pg.click(x, y)  # нажимаем на иконку телеграма


while True:  # бесконечный цикл
    send_msg_to_work()
    print('Task number - ' + str(i))

# 765 705
# 695 748
# C:\Users\User\AppData\Roaming\Mozilla\Firefox\Profiles\enpkw53a.default-release-1\places.sqlite
