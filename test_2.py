from telethon.sync import TelegramClient
import time
import pyautogui as pg

api_id = 1234567
api_hash = 'your hash'
client = TelegramClient('BOTFORME', api_id,
                        api_hash)  # создаем клиент для входа нашей програмы в на аккаунт
client.start()  # запускаем клиент

dlgs = client.get_dialogs()  # получаем все наши названия каналов, групп в которых мы состоим
for dlg in dlgs:
    if dlg.title == 'LTC Click Bot':
        btc = dlg  # находим нужный диалог и записывем его данные в переменную



i = 0


def send_msg_to_work():  # функция отправки сообщений к ботту для посещения сайтов
    global i
    client.send_message('LTC Click Bot', '📣 Join chats')  # отправляем команду к боту
    i += 1
    time.sleep(1)  # ждем пока бот обработает наш запрос и отправит ссылку
    get_msg = client.get_messages(btc, limit=1)  # получаем сообщение которое нам отослал бот
    get_msg[0].click(0)  # нажымаем кнопку с ссылкой в сообщении бота. По ней нас отправляет на сайт
    time.sleep(5)  # ждем  прогрузки всех елементов сайта
    # но я решил не заморачивться и просто кликать на капчу и не проверять ее наличие на дынном сайте
    # time.sleep(3.5)
    pg.click(720, 229)
    # 720 229
    pg.click(502, 745)
    # 502 745
    time.sleep(1)
    pg.click(949, 700)
    # 949 700
    get_msg = client.get_messages(btc, limit=1)
    get_msg[0].click(1)
    time.sleep(1)  # задерживаем скрипт


while True:  # бесконечный цикл
    send_msg_to_work()
    print('Task number - ' + str(i))
