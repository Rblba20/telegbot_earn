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


def get_t(s):  # функция для получения числа из строки
    l = len(s)
    integ = 10
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
    client.send_message('LTC Click Bot', '🖥 Visit sites')  # отправляем команду к боту
    i += 1
    time.sleep(1)  # ждем пока бот обработает наш запрос и отправит ссылку
    get_msg = client.get_messages(btc, limit=1)  # получаем сообщение которое нам отослал бот
    get_msg[0].click(0)  # нажымаем кнопку с ссылкой в сообщении бота. По ней нас отправляет на сайт

    time.sleep(2)  # ждем  прогрузки всех елементов сайта
    # pg.click(587, 371)  # нажымаем не рекапчу, которая может быть на сайте. Возможна жоработка с машшыным зрением,
    # но я решил не заморачивться и просто кликать на капчу и не проверять ее наличие на дынном сайте
    time.sleep(2)

    time_msg = client.get_messages(btc,
                                   limit=1)  # при переходе на сайт боот автоматически отправляет нам сообщение в
    # котором написано сколько я должен бцде провести времени на сайте
    st = time_msg[0].message  # переменая в которой содержиться текст последнего сообщения

    last_m = st
    print(last_m)
    integ = 10  # количесво секунд для задержки скрипта
    # if get_t(st) is None:  # проверяем если функция не нашла число в строке тогда ничего не делаем
    time.sleep(integ)
    x = 0
    while True:
        x += 1
        time_msg = client.get_messages(btc,
                                       limit=1)  # при переходе на сайт боот автоматически отправляет нам сообщение в котором написано сколько я должен бцде провести времени на сайте
        st = time_msg[0].message  # переменая в которой содержиться текст последнего сообщения
        print(st)
        print(x)
        # pr = time_msg[1].message
        if last_m != st:
            print('КОНЕЦ', x)
            integ = 1
            break
    # else:
    #   integ = get_t(st)  # если нашла то присваиваем переменой времени то число которае нам возвратила функция
    #  if integ > 60:
    #     integ = 20
    #  elif integ < 10:
    #     integ = 10

    print('sleep - ' + str(integ))
    time.sleep(integ)  # задерживаем скрипт

    pg.hotkey('ctrl', 'w')  # закрывем вкладку в хроме
    pg.click(499, 747)  # нажимаем на иконку телеграма
    # x = 499 y = 747
    # pg.click(1328, 644)
    # x = 1328 y = 644
    time.sleep(1)


while True:  # бесконечный цикл
    send_msg_to_work()
    print('Task number - ' + str(i))
