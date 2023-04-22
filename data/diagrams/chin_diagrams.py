import sqlite3
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('agg')
con = sqlite3.connect("db/tests.db", check_same_thread=False)
cur = con.cursor()


def main_chin_diagram():
    result_chin1 = cur.execute("""SELECT chinchilla FROM results
                        WHERE chinchilla = ?""", ("малая длиннохвостая шиншилла",)).fetchall()
    result_chin2 = cur.execute("""SELECT chinchilla FROM results
                WHERE chinchilla = ?""", ("береговая шиншилла",)).fetchall()
    result_chin3 = cur.execute("""SELECT chinchilla FROM results
                    WHERE chinchilla = ?""", ("короткохвостая шиншилла",)).fetchall()
    result_chin4 = cur.execute("""SELECT chinchilla FROM results
                    WHERE chinchilla = ?""", ("большая шиншилла",)).fetchall()
    vals = [len(result_chin1), len(result_chin2), len(result_chin3), len(result_chin4)]
    idx_remove = []
    for el in vals:
        if el == 0:
            idx_remove.append(vals.index(el))
            vals.remove(el)
    labels = ["малая длиннохвостая шиншилла", "береговая шиншилла", "короткохвостая шиншилла", "большая шиншилла"]
    if idx_remove:
        for el in idx_remove:
            labels.remove(labels[el])
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels, autopct='%1.1f%%')
    ax.axis("equal")
    plt.savefig('static/img/main_chin_diagram.png')


def info_chin_diagram1():
    values_chin1 = {'Комедия': 0,
                    'Боевик': 0,
                    'Фантастика': 0,
                    'Артхаус': 0}
    result_chin1 = cur.execute("""SELECT chin_1 FROM Results_chin""").fetchall()
    for el in result_chin1:
        values_chin1[el[0]] += 1
    vals1 = [values_chin1['Комедия'], values_chin1['Боевик'], values_chin1['Фантастика'], values_chin1['Артхаус']]
    idx_remove1 = []
    for el in vals1:
        if el == 0:
            idx_remove1.append(vals1.index(el))
            vals1.remove(el)
    labels1 = ["Комедия", "Боевик", "Фантастика", "Артхаус"]
    if idx_remove1:
        for el in idx_remove1:
            labels1.remove(labels1[el])
    fig1, ax1 = plt.subplots()
    ax1.pie(vals1, labels=labels1, autopct='%1.1f%%')
    ax1.axis("equal")
    plt.savefig('static/img/info_chin_diagram1.png')


def info_chin_diagram2():
    values_chin2 = {'Группа': 0,
                    'Семья': 0,
                    'Друг': 0,
                    'Один': 0}
    result_chin2 = cur.execute("""SELECT chin_2 FROM Results_chin""").fetchall()
    for el in result_chin2:
        values_chin2[el[0]] += 1
    vals2 = [values_chin2['Группа'], values_chin2['Семья'], values_chin2['Друг'], values_chin2['Один']]
    idx_remove2 = []
    for el in vals2:
        if el == 0:
            idx_remove2.append(vals2.index(el))
            vals2.remove(el)
    labels2 = ["Группа", "Семья", "Друг", "Один"]
    if idx_remove2:
        for el in idx_remove2:
            labels2.remove(labels2[el])
    fig2, ax2 = plt.subplots()
    ax2.pie(vals2, labels=labels2, autopct='%1.1f%%')
    ax2.axis("equal")
    plt.savefig('static/img/info_chin_diagram2.png')


def info_chin_diagram3():
    values_chin3 = {'Одиночество': 0,
                    'Смерть': 0,
                    'Высота': 0,
                    'Разочарованность': 0}
    result_chin3 = cur.execute("""SELECT chin_3 FROM Results_chin""").fetchall()
    for el in result_chin3:
        values_chin3[el[0]] += 1
    vals3 = [values_chin3['Одиночество'], values_chin3['Смерть'], values_chin3['Высота'],
             values_chin3['Разочарованность']]
    idx_remove3 = []
    for el in vals3:
        if el == 0:
            idx_remove3.append(vals3.index(el))
            vals3.remove(el)
    labels3 = ["Одиночество", "Смерть", "Высота", "Разочарованность"]
    if idx_remove3:
        for el in idx_remove3:
            labels3.remove(labels3[el])
    fig3, ax3 = plt.subplots()
    ax3.pie(vals3, labels=labels3, autopct='%1.1f%%')
    ax3.axis("equal")
    plt.savefig('static/img/info_chin_diagram3.png')


def info_chin_diagram4():
    values_chin4 = {'Ум': 0,
                    'Харизма': 0,
                    'Трудолюбие': 0,
                    'Чувственность': 0}
    result_chin4 = cur.execute("""SELECT chin_4 FROM Results_chin""").fetchall()
    for el in result_chin4:
        values_chin4[el[0]] += 1
    vals4 = [values_chin4['Ум'], values_chin4['Харизма'], values_chin4['Трудолюбие'], values_chin4['Чувственность']]
    idx_remove4 = []
    for el in vals4:
        if el == 0:
            idx_remove4.append(vals4.index(el))
            vals4.remove(el)
    labels4 = ["Ум", "Харизма", "Трудолюбие", "Чувственность"]
    if idx_remove4:
        for el in idx_remove4:
            labels4.remove(labels4[el])
    fig4, ax4 = plt.subplots()
    ax4.pie(vals4, labels=labels4, autopct='%1.1f%%')
    ax4.axis("equal")
    plt.savefig('static/img/info_chin_diagram4.png')


def info_chin_diagram5():
    values_chin5 = {'Данет': 0,
                    'Нетда': 0,
                    'Да': 0,
                    'Нет': 0}
    result_chin5 = cur.execute("""SELECT chin_5 FROM Results_chin""").fetchall()
    for el in result_chin5:
        values_chin5[el[0]] += 1
    vals5 = [values_chin5['Данет'], values_chin5['Нетда'], values_chin5['Да'], values_chin5['Нет']]
    idx_remove5 = []
    for el in vals5:
        if el == 0:
            idx_remove5.append(vals5.index(el))
            vals5.remove(el)
    labels5 = ["Данет", "Нетда", "Да", "Нет"]
    if idx_remove5:
        for el in idx_remove5:
            labels5.remove(labels5[el])
    fig5, ax5 = plt.subplots()
    ax5.pie(vals5, labels=labels5, autopct='%1.1f%%')
    ax5.axis("equal")
    plt.savefig('static/img/info_chin_diagram5.png')
