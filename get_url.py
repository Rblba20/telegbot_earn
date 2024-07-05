import sqlite3
import requests

path = input('Путь до файла с истрией Firefox:')
# программа
con = sqlite3.connect(path)
cur = con.cursor()
id_select = cur.execute("""SELECT id FROM moz_historyvisits""").fetchall()
for i in range(len(id_select)):
    id_select[i] = str(id_select[i])[1:-2]
    id_select[i] = int(id_select[i])
select = max(id_select)
place_id = cur.execute("""SELECT place_id FROM moz_historyvisits WHERE id == ?""",
                       (select,)).fetchall()
place_id = str(place_id)[2:-3]
link = cur.execute("""SELECT url FROM moz_places WHERE id == ?""",
                   (place_id,)).fetchall()
link = str(link)[3:-4]
response = requests.get(link)
html_code = response.text
if 'data-timer=' in html_code:
    html_code = str(html_code)
    list_ = html_code.split()
    for i in range(len(list_)):
        if 'data-timer=' in list_[i]:
            a = str(list_[i])[12:-1]
            time = int(a)
elif 'data-timer=' not in html_code:
    time = 10
# Please wait 4 seconds...
# Plese wait 1 second...
# You earned 0.00000132 LTC!
# <h5 class="timer">You earned 0.00000132 LTC!</h5>
