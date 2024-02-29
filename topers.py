from operator import itemgetter

def money_form(mon):
    mon = str(mon)
    idd = -1
    ctr = 1
    rez = ""
    for i in range(len(mon)):
        if ctr == 4:
            ctr = 1
            rez += " "
        rez += mon[idd]
        ctr += 1
        idd -= 1

    rez = rez[::-1]
    return rez

def top_do1(kkk, People, idd_cool, name):
    idd = 0
    dc = {}
    for i, y in People.items():
        if idd == 0:
            pass
        else:
            if name not in y.keys():
                pass
            else:
                dc[i]=y[name]

        idd+=1

    sorted_tuple = dict(sorted(dc.items(), key=itemgetter(1)))
    sorted_tuple = dict(reversed(sorted_tuple.items()))

    ufff = ""
    if name == "balance":
        ufff = "балансу"
    if name == "boss_hp":
        ufff = "нанесённому урону боссу"
    if name == "bitcoin":
        ufff = "фиткоину"
    if name == "promo":
        ufff = "промокодам"
    if name == "icecream":
        ufff = "мороженому"

    txt = f"топ лист по {ufff}:\n\n"
    idd = 1
    for i,y in sorted_tuple.items():
        if idd_cool == -1001806713364:
            mention = "<a href='https://t.me/True_gb_bot'>" + People[i]['name'] + "</>"
        else:
            mention = "<a href='tg://user?id=" + i + "'>" + People[i]['name'] + "</>"
            mention = "<a href='https://t.me/True_gb_bot'>" + People[i]['name'] + "</>"

        txt_let1 = ""
        txt_let2 = ""
        if People[i]['state_prem']['true'] == 1:
            if People[i]['state_prem']['name'] == "Флэш":
                txt_let1 = "<b>"
                txt_let2 = "</b>"
        if idd == 1:
            txt += f"① {txt_let1}{mention}{txt_let2} - {money_form(y)} \n"
        if idd == 2:
            txt += f"② {txt_let1}{mention}{txt_let2} - {money_form(y)} \n"
        if idd == 3:
            txt += f"③ {txt_let1}{mention}{txt_let2} - {money_form(y)} \n"
        if idd == 4:
            txt += f"④ {txt_let1}{mention}{txt_let2} - {money_form(y)} \n"
        if idd == 5:
            txt += f"⑤ {txt_let1}{mention}{txt_let2} - {money_form(y)} \n"
        if idd == 6:
            txt += f"⑥ {txt_let1}{mention}{txt_let2} - {money_form(y)} \n"
        if idd == 7:
            txt += f"⑦ {txt_let1}{mention}{txt_let2} - {money_form(y)} \n"
        if idd == 8:
            txt += f"⑧ {txt_let1}{mention}{txt_let2} - {money_form(y)} \n"
        if idd == 9:
            txt += f"⑨ {txt_let1}{mention}{txt_let2} - {money_form(y)} \n"
        if idd == 10:
            txt += f"⑩ {txt_let1}{mention}{txt_let2} - {money_form(y)} "

        if kkk == i:
            txt_num = ""
            for i in str(idd):
                if i == "1":
                    txt_num += "①"
                if i == "2":
                    txt_num += "②"
                if i == "3":
                    txt_num += "③"
                if i == "4":
                    txt_num += "④"
                if i == "5":
                    txt_num += "⑤"
                if i == "6":
                    txt_num += "⑥"
                if i == "7":
                    txt_num += "⑦"
                if i == "8":
                    txt_num += "⑧"
                if i == "9":
                    txt_num += "⑨"
                if i == "0":
                    txt_num += "ⓞ"
            tp = f"\n\n{txt_num}.{txt_let1}{mention}{txt_let2} - {money_form(y)}"
        idd+= 1


    txt += tp
    return txt
