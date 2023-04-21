import sqlite3
from matplotlib import pyplot as plt

con = sqlite3.connect("db/tests.db", check_same_thread=False)
cur = con.cursor()


def main_cat_diagram():
    result_cat1 = cur.execute("""SELECT cat FROM results
                        WHERE cat = ?""", ("мейн-кун",)).fetchall()
    result_cat2 = cur.execute("""SELECT cat FROM results
                WHERE cat = ?""", ("сиамская кошка",)).fetchall()
    result_cat3 = cur.execute("""SELECT cat FROM results
                    WHERE cat = ?""", ("русская голубая",)).fetchall()
    result_cat4 = cur.execute("""SELECT cat FROM results
                    WHERE cat = ?""", ("сфинкс",)).fetchall()
    vals = [len(result_cat1), len(result_cat2), len(result_cat3), len(result_cat4)]
    idx_remove = []
    for el in vals:
        if el == 0:
            idx_remove.append(vals.index(el))
            vals.remove(el)
    labels = ["мейн-кун", "сиамская кошка", "русская голубая", "сфинкс"]
    if idx_remove:
        for el in idx_remove:
            labels.remove(labels[el])
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels, autopct='%1.1f%%')
    ax.axis("equal")
    plt.savefig('static/img/main_cat_diagram.png')


def info_cat_diagram1():
    values_cat1 = {'Математика': 0,
                   'Гуманитарные науки': 0,
                   'Биология': 0,
                   'Искусство': 0}
    result_cat1 = cur.execute("""SELECT cat_1 FROM Results_cat""").fetchall()
    for el in result_cat1:
        values_cat1[el[0]] += 1
    vals1 = [values_cat1['Математика'], values_cat1['Гуманитарные науки'], values_cat1['Биология'], values_cat1['Искусство']]
    idx_remove1 = []
    for el in vals1:
        if el == 0:
            idx_remove1.append(vals1.index(el))
            vals1.remove(el)
    labels1 = ["Математика", "Гуманитарные науки", "Биология", "Искусство"]
    if idx_remove1:
        for el in idx_remove1:
            labels1.remove(labels1[el])
    fig1, ax1 = plt.subplots()
    ax1.pie(vals1, labels=labels1, autopct='%1.1f%%')
    ax1.axis("equal")
    plt.savefig('static/img/info_cat_diagram1.png')


def info_cat_diagram2():
    values_cat2 = {'Амбиверт': 0,
                   'Экстраверт': 0,
                   'Интроверт': 0,
                   'Незнаю': 0}
    result_cat2 = cur.execute("""SELECT cat_2 FROM Results_cat""").fetchall()
    for el in result_cat2:
        values_cat2[el[0]] += 1
    vals2 = [values_cat2['Амбиверт'], values_cat2['Экстраверт'], values_cat2['Интроверт'], values_cat2['Незнаю']]
    idx_remove2 = []
    for el in vals2:
        if el == 0:
            idx_remove2.append(vals2.index(el))
            vals2.remove(el)
    labels2 = ["Амбиверт", "Экстраверт", "Интроверт", "Незнаю"]
    if idx_remove2:
        for el in idx_remove2:
            labels2.remove(labels2[el])
    fig2, ax2 = plt.subplots()
    ax2.pie(vals2, labels=labels2, autopct='%1.1f%%')
    ax2.axis("equal")
    plt.savefig('static/img/info_cat_diagram2.png')


def info_cat_diagram3():
    values_cat3 = {'Рок': 0,
                   'Рэп': 0,
                   'Поп': 0,
                   'Инди': 0}
    result_cat3 = cur.execute("""SELECT cat_3 FROM Results_cat""").fetchall()
    for el in result_cat3:
        values_cat3[el[0]] += 1
    vals3 = [values_cat3['Рок'], values_cat3['Рэп'], values_cat3['Поп'], values_cat3['Инди']]
    idx_remove3 = []
    for el in vals3:
        if el == 0:
            idx_remove3.append(vals3.index(el))
            vals3.remove(el)
    labels3 = ["Рок", "Рэп", "Поп", "Инди"]
    if idx_remove3:
        for el in idx_remove3:
            labels3.remove(labels3[el])
    fig3, ax3 = plt.subplots()
    ax3.pie(vals3, labels=labels3, autopct='%1.1f%%')
    ax3.axis("equal")
    plt.savefig('static/img/info_cat_diagram3.png')


def info_cat_diagram4():
    values_cat4 = {'Фейсбук': 0,
                   'Твиттер': 0,
                   'Инстаграм': 0,
                   'ВК': 0}
    result_cat4 = cur.execute("""SELECT cat_4 FROM Results_cat""").fetchall()
    for el in result_cat4:
        values_cat4[el[0]] += 1
    vals4 = [values_cat4['Фейсбук'], values_cat4['Твиттер'], values_cat4['Инстаграм'], values_cat4['ВК']]
    idx_remove4 = []
    for el in vals4:
        if el == 0:
            idx_remove4.append(vals4.index(el))
            vals4.remove(el)
    labels4 = ["Фейсбук", "Твиттер", "Инстаграм", "ВК"]
    if idx_remove4:
        for el in idx_remove4:
            labels4.remove(labels4[el])
    fig4, ax4 = plt.subplots()
    ax4.pie(vals4, labels=labels4, autopct='%1.1f%%')
    ax4.axis("equal")
    plt.savefig('static/img/info_cat_diagram4.png')


def info_cat_diagram5():
    values_cat5 = {'Нет': 0,
                   'Да': 0,
                   'Иногда': 0,
                   'Неиспытывал': 0}
    result_cat5 = cur.execute("""SELECT cat_5 FROM Results_cat""").fetchall()
    for el in result_cat5:
        values_cat5[el[0]] += 1
    vals5 = [values_cat5['Нет'], values_cat5['Да'], values_cat5['Иногда'], values_cat5['Неиспытывал']]
    idx_remove5 = []
    for el in vals5:
        if el == 0:
            idx_remove5.append(vals5.index(el))
            vals5.remove(el)
    labels5 = ["Нет", "Да", "Иногда", "Неиспытывал"]
    if idx_remove5:
        for el in idx_remove5:
            labels5.remove(labels5[el])
    fig5, ax5 = plt.subplots()
    ax5.pie(vals5, labels=labels5, autopct='%1.1f%%')
    ax5.axis("equal")
    plt.savefig('static/img/info_cat_diagram5.png')