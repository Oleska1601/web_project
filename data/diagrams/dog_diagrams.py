import sqlite3
from matplotlib import pyplot as plt

con = sqlite3.connect("db/tests.db", check_same_thread=False)
cur = con.cursor()


def main_dog_diagram():
    result_dog1 = cur.execute("""SELECT dog FROM results
                        WHERE dog = ?""", ("бульдог",)).fetchall()
    result_dog2 = cur.execute("""SELECT dog FROM results
                WHERE dog = ?""", ("пудель",)).fetchall()
    result_dog3 = cur.execute("""SELECT dog FROM results
                    WHERE dog = ?""", ("гончая",)).fetchall()
    result_dog4 = cur.execute("""SELECT dog FROM results
                    WHERE dog = ?""", ("бобтейл",)).fetchall()
    vals = [len(result_dog1), len(result_dog2), len(result_dog3), len(result_dog4)]
    idx_remove = []
    for el in vals:
        if el == 0:
            idx_remove.append(vals.index(el))
            vals.remove(el)
    labels = ["бульдог", "пудель", "гончая", "бобтейл"]
    if idx_remove:
        for el in idx_remove:
            labels.remove(labels[el])
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels, autopct='%1.1f%%')
    ax.axis("equal")
    plt.savefig('static/img/main_dog_diagram.png')


def info_dog_diagram1():
    values_dog1 = {'Сангвинник': 0,
                   'Флегматик': 0,
                   'Холерик': 0,
                   'Меланхолик': 0}
    result_dog1 = cur.execute("""SELECT dog_1 FROM Results_dog""").fetchall()
    for el in result_dog1:
        values_dog1[el[0]] += 1
    vals1 = [values_dog1['Сангвинник'], values_dog1['Флегматик'], values_dog1['Холерик'], values_dog1['Меланхолик']]
    idx_remove1 = []
    for el in vals1:
        if el == 0:
            idx_remove1.append(vals1.index(el))
            vals1.remove(el)
    labels1 = ["Сангвинник", "Флегматик", "Холерик", "Меланхолик"]
    if idx_remove1:
        for el in idx_remove1:
            labels1.remove(labels1[el])
    fig1, ax1 = plt.subplots()
    ax1.pie(vals1, labels=labels1, autopct='%1.1f%%')
    ax1.axis("equal")
    plt.savefig('static/img/info_dog_diagram1.png')


def info_dog_diagram2():
    values_dog2 = {'Улун': 0,
                   'Ассам': 0,
                   'Фруктовый': 0,
                   'Нет': 0}
    result_dog2 = cur.execute("""SELECT dog_2 FROM Results_dog""").fetchall()
    for el in result_dog2:
        values_dog2[el[0]] += 1
    vals2 = [values_dog2['Улун'], values_dog2['Ассам'], values_dog2['Фруктовый'], values_dog2['Нет']]
    idx_remove2 = []
    for el in vals2:
        if el == 0:
            idx_remove2.append(vals2.index(el))
            vals2.remove(el)
    labels2 = ["Улун", "Ассам", "Фруктовый", "Нет"]
    if idx_remove2:
        for el in idx_remove2:
            labels2.remove(labels2[el])
    fig2, ax2 = plt.subplots()
    ax2.pie(vals2, labels=labels2, autopct='%1.1f%%')
    ax2.axis("equal")
    plt.savefig('static/img/info_dog_diagram2.png')


def info_dog_diagram3():
    values_dog3 = {'Кино': 0,
                   'Рисование': 0,
                   'Спорт': 0,
                   'Книги': 0}
    result_dog3 = cur.execute("""SELECT dog_3 FROM Results_dog""").fetchall()
    for el in result_dog3:
        values_dog3[el[0]] += 1
    vals3 = [values_dog3['Кино'], values_dog3['Рисование'], values_dog3['Спорт'], values_dog3['Книги']]
    idx_remove3 = []
    for el in vals3:
        if el == 0:
            idx_remove3.append(vals3.index(el))
            vals3.remove(el)
    labels3 = ["Кино", "Рисование", "Спорт", "Книги"]
    if idx_remove3:
        for el in idx_remove3:
            labels3.remove(labels3[el])
    fig3, ax3 = plt.subplots()
    ax3.pie(vals3, labels=labels3, autopct='%1.1f%%')
    ax3.axis("equal")
    plt.savefig('static/img/info_dog_diagram3.png')


def info_dog_diagram4():
    values_dog4 = {'Силы': 0,
                   'Богатство': 0,
                   'Любовь': 0,
                   'Бессмертие': 0}
    result_dog4 = cur.execute("""SELECT dog_4 FROM Results_dog""").fetchall()
    for el in result_dog4:
        values_dog4[el[0]] += 1
    vals4 = [values_dog4['Силы'], values_dog4['Богатство'], values_dog4['Любовь'], values_dog4['Бессмертие']]
    idx_remove4 = []
    for el in vals4:
        if el == 0:
            idx_remove4.append(vals4.index(el))
            vals4.remove(el)
    labels4 = ["Силы", "Богатство", "Любовь", "Бессмертие"]
    if idx_remove4:
        for el in idx_remove4:
            labels4.remove(labels4[el])
    fig4, ax4 = plt.subplots()
    ax4.pie(vals4, labels=labels4, autopct='%1.1f%%')
    ax4.axis("equal")
    plt.savefig('static/img/info_dog_diagram4.png')


def info_dog_diagram5():
    values_dog5 = {'Желтый': 0,
                   'Синий': 0,
                   'Красный': 0,
                   'Зеленый': 0}
    result_dog5 = cur.execute("""SELECT dog_5 FROM Results_dog""").fetchall()
    for el in result_dog5:
        values_dog5[el[0]] += 1
    vals5 = [values_dog5['Желтый'], values_dog5['Синий'], values_dog5['Красный'], values_dog5['Зеленый']]
    idx_remove5 = []
    for el in vals5:
        if el == 0:
            idx_remove5.append(vals5.index(el))
            vals5.remove(el)
    labels5 = ["Желтый", "Синий", "Красный", "Зеленый"]
    if idx_remove5:
        for el in idx_remove5:
            labels5.remove(labels5[el])
    fig5, ax5 = plt.subplots()
    ax5.pie(vals5, labels=labels5, autopct='%1.1f%%')
    ax5.axis("equal")
    plt.savefig('static/img/info_dog_diagram5.png')