import sqlite3
from matplotlib import pyplot as plt

con = sqlite3.connect("db/tests.db", check_same_thread=False)
cur = con.cursor()


def main_drink_diagram():
    result_drink1 = cur.execute("""SELECT drink FROM results
                        WHERE drink = ?""", ("кофе",)).fetchall()
    result_drink2 = cur.execute("""SELECT drink FROM results
                WHERE drink = ?""", ("сок",)).fetchall()
    result_drink3 = cur.execute("""SELECT drink FROM results
                    WHERE drink = ?""", ("молочный коктейль",)).fetchall()
    result_drink4 = cur.execute("""SELECT drink FROM results
                    WHERE drink = ?""", ("чай",)).fetchall()
    vals = [len(result_drink1), len(result_drink2), len(result_drink3), len(result_drink4)]
    idx_remove = []
    for el in vals:
        if el == 0:
            idx_remove.append(vals.index(el))
            vals.remove(el)
    labels = ["кофе", "сок", "молочный коктейль", "чай"]
    if idx_remove:
        for el in idx_remove:
            labels.remove(labels[el])
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels, autopct='%1.1f%%')
    ax.axis("equal")
    plt.savefig('static/img/main_drink_diagram.png')


def info_drink_diagram1():
    values_drink1 = {'Волнение': 0,
                     'Жизнерадостный': 0,
                     'Мечтательный': 0,
                     'Задумчивый': 0}
    result_drink1 = cur.execute("""SELECT drink_1 FROM Results_drink""").fetchall()
    for el in result_drink1:
        values_drink1[el[0]] += 1
    vals1 = [values_drink1['Волнение'], values_drink1['Жизнерадостный'], values_drink1['Мечтательный'],
             values_drink1['Задумчивый']]
    idx_remove1 = []
    for el in vals1:
        if el == 0:
            idx_remove1.append(vals1.index(el))
            vals1.remove(el)
    labels1 = ["Волнение", "Жизнерадостный", "Мечтательный", "Задумчивый"]
    if idx_remove1:
        for el in idx_remove1:
            labels1.remove(labels1[el])
    fig1, ax1 = plt.subplots()
    ax1.pie(vals1, labels=labels1, autopct='%1.1f%%')
    ax1.axis("equal")
    plt.savefig('static/img/info_drink_diagram1.png')


def info_drink_diagram2():
    values_drink2 = {'Дождь': 0,
                     'Солнце': 0,
                     'Снег': 0,
                     'Облачно': 0}
    result_drink2 = cur.execute("""SELECT drink_2 FROM Results_drink""").fetchall()
    for el in result_drink2:
        values_drink2[el[0]] += 1
    vals2 = [values_drink2['Дождь'], values_drink2['Солнце'], values_drink2['Снег'], values_drink2['Облачно']]
    idx_remove2 = []
    for el in vals2:
        if el == 0:
            idx_remove2.append(vals2.index(el))
            vals2.remove(el)
    labels2 = ["Дождь", "Солнце", "Снег", "Облачно"]
    if idx_remove2:
        for el in idx_remove2:
            labels2.remove(labels2[el])
    fig2, ax2 = plt.subplots()
    ax2.pie(vals2, labels=labels2, autopct='%1.1f%%')
    ax2.axis("equal")
    plt.savefig('static/img/info_drink_diagram2.png')


def info_drink_diagram3():
    values_drink3 = {'Осень': 0,
                     'Лето': 0,
                     'Зима': 0,
                     'Весна': 0}
    result_drink3 = cur.execute("""SELECT drink_3 FROM Results_drink""").fetchall()
    for el in result_drink3:
        values_drink3[el[0]] += 1
    vals3 = [values_drink3['Осень'], values_drink3['Лето'], values_drink3['Зима'], values_drink3['Весна']]
    idx_remove3 = []
    for el in vals3:
        if el == 0:
            idx_remove3.append(vals3.index(el))
            vals3.remove(el)
    labels3 = ["Осень", "Лето", "Зима", "Весна"]
    if idx_remove3:
        for el in idx_remove3:
            labels3.remove(labels3[el])
    fig3, ax3 = plt.subplots()
    ax3.pie(vals3, labels=labels3, autopct='%1.1f%%')
    ax3.axis("equal")
    plt.savefig('static/img/info_drink_diagram3.png')


def info_drink_diagram4():
    values_drink4 = {'Детектив': 0,
                     'Роман': 0,
                     'Фэнтези': 0,
                     'Фантастика': 0}
    result_drink4 = cur.execute("""SELECT drink_4 FROM Results_drink""").fetchall()
    for el in result_drink4:
        values_drink4[el[0]] += 1
    vals4 = [values_drink4['Детектив'], values_drink4['Роман'], values_drink4['Фэнтези'], values_drink4['Фантастика']]
    idx_remove4 = []
    for el in vals4:
        if el == 0:
            idx_remove4.append(vals4.index(el))
            vals4.remove(el)
    labels4 = ["Детектив", "Роман", "Фэнтези", "Фантастика"]
    if idx_remove4:
        for el in idx_remove4:
            labels4.remove(labels4[el])
    fig4, ax4 = plt.subplots()
    ax4.pie(vals4, labels=labels4, autopct='%1.1f%%')
    ax4.axis("equal")
    plt.savefig('static/img/info_drink_diagram4.png')


def info_drink_diagram5():
    values_drink5 = {'Заранее': 0,
                     'Ничего': 0,
                     'Умею': 0,
                     'Прокрастинирую': 0}
    result_drink5 = cur.execute("""SELECT drink_5 FROM Results_drink""").fetchall()
    for el in result_drink5:
        values_drink5[el[0]] += 1
    vals5 = [values_drink5['Заранее'], values_drink5['Ничего'], values_drink5['Умею'], values_drink5['Прокрастинирую']]
    idx_remove5 = []
    for el in vals5:
        if el == 0:
            idx_remove5.append(vals5.index(el))
            vals5.remove(el)
    labels5 = ["Заранее", "Ничего", "Умею", "Прокрастинирую"]
    if idx_remove5:
        for el in idx_remove5:
            labels5.remove(labels5[el])
    fig5, ax5 = plt.subplots()
    ax5.pie(vals5, labels=labels5, autopct='%1.1f%%')
    ax5.axis("equal")
    plt.savefig('static/img/info_drink_diagram5.png')
