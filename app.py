from telethon.sync import TelegramClient
import time
import pyautogui as pg
import sqlite3
import requests
import cloudscraper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import cfscrape
import requests
from collections import OrderedDict
from requests import Session
import socket
import cloudscraper


print('Путь до файла')
path = input()
# print('ВВедите x координату')
# x = int(input())
# print('ведите y координату')
# y = int(input())
api_id = 1234567
api_hash = 'your hash'
client = TelegramClient('BOTFORME', api_id,
                        api_hash)  # создаем клиент для входа нашей програмы в на аккаунт
client.start()  # запускаем клиент

dlgs = client.get_dialogs()  # получаем все наши названия каналов, групп в которых мы состоим
for dlg in dlgs:
    if dlg.title == 'BCH Click Bot':
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


# def get_webdriver():
#   option = webdriver.FirefoxOptions()
#   option.set_preference('dom.webdriver.enabled', False)
#   driver = webdriver.Firefox(options=option)
#   return driver


def send_msg_to_work():  # функция отправки сообщений к ботту для посещения сайтов
    global i
    client.send_message('BCH Click Bot', '🖥 Visit sites')  # отправляем команду к боту
    i += 1
    time.sleep(1)  # ждем пока бот обработает наш запрос и отправит ссылку
    get_msg = client.get_messages(btc, limit=1)  # получаем сообщение которое нам отослал бот
    get_msg[0].click(0)  # нажымаем кнопку с ссылкой в сообщении бота. По ней нас отправляет на сайт
    time.sleep(2.5)  # ждем  прогрузки всех елементов сайта
    pg.click(665, 286)  # нажымаем не рекапчу, которая может быть на сайте. Возможна жоработка с машшыным зрением,
    # но я решил не заморачивться и просто кликать на капчу и не проверять ее наличие на дынном сайте
    time.sleep(2.5)

    con = sqlite3.connect(path)
    cur = con.cursor()
    id_select = cur.execute("""SELECT id FROM moz_historyvisits""").fetchall()
    for j in range(len(id_select)):
        id_select[j] = str(id_select[j])[1:-2]
        id_select[j] = int(id_select[j])
    select = max(id_select)
    place_id = cur.execute("""SELECT place_id FROM moz_historyvisits WHERE id == ?""",
                           (select,)).fetchall()
    place_id = str(place_id)[2:-3]
    link = cur.execute("""SELECT url FROM moz_places WHERE id == ?""",
                       (place_id,)).fetchall()
    link = str(link)[3:-4]
#  s = Session()
 #   headers = OrderedDict({
  #      'Accept-Encoding': 'gzip, deflate, br',
  #      'Host': "grimaldis.myguestaccount.com",
  #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'
  #  })
  #  s.headers = headers
 #   html_code = s.get(link, headers=headers, verify=False).text
   # print(html_code)
    scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
    # Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
    html_code = scraper.get(link).text
    print(html_code)  # => "<!DOCTYPE html><html><head>..."

    # scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
    # Or: scraper = cfscrape.CloudflareScraper()  # CloudflareScraper inherits from requests.Session
    # html_code = str(scraper.get(link).content)  # => "<!DOCTYPE html><html><head>..."
    #    driver = get_webdriver()
    #   html_code = driver.get(link)
    # scraper = cloudscraper.create_scraper()
    #  header = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                    'Chrome/75.0.3770.100 Safari/537.36'}
    # response = requests.get(link, headers=header)
    # response = requests.get(link)
    # html_code = response.text
    # html_code = scraper.get(link).text
    # print(html_code)
    if 'data-timer=' in html_code:
        print('yes')
        html_code = str(html_code)
        list_ = html_code.split()
        for g in range(len(list_)):
            if 'data-timer=' in list_[g]:
                a = str(list_[g])[12:-1]
                print(a)
                integ = int(a) + 1.5
    elif 'data-timer=' not in html_code:
        print('no')
        time_msg = client.get_messages(btc,
                                       limit=1)  # при переходе на сайт боот автоматически отправляет нам сообщение в
        # котором написано сколько я должен бцде провести времени на сайте
        st = time_msg[0].message  # переменая в которой содержиться текст последнего сообщения
        s = st
        integ = 10  # количесво секунд для задержки скрипта
        if get_t(st) is None:  # проверяем если функция не нашла число в строке тогда ничего не делаем
            pass
        else:
            integ = get_t(st)  # если нашла то присваиваем переменой времени то число которае нам возвратила функция
        if integ > 60:
            integ = 20
        elif integ < 10:
            integ = 10
    print('sleep - ' + str(integ))
    time.sleep(integ)  # задерживаем скрипт
    pg.click(665, 286)
    pg.hotkey('ctrl', 'w')  # закрывем вкладку в хроме


#    pg.click(x, y)  # нажимаем на иконку телеграма


while True:  # бесконечный цикл
    send_msg_to_work()
    print('Task number - ' + str(i))

# 695 748 C:\Users\User\AppData\Roaming\Mozilla\Firefox\Profiles\enpkw53a.default-release-1\places.sqlite <div
# class="cf-alert cf-alert-error cf-cookie-error hidden" id="cookie-alert" data-translate="enable_cookies">Please
# enable cookies.</div> <div id="cf-error-details" class="p-0">
