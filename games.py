def money_form2(mon1):
    mon = str(mon1)
    if mon1 < 0:
        idd = 0
        txt = ""
        for i in mon:
            if idd == 0:
                pass
            else:
                txt += i
            idd += 1

        mon = txt
        print(mon)

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
    if mon1 < 0:
        rez = "-" + rez
    return rez


def kazino(People, rand, stavka, kkk):
    mention = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"
    if rand <= 20:
        price = int(stavka * 2)
        txt = f"👾{mention}, ваша ставка: \n" \
              f"💈множитель выигрыша: 2x \n" \
              f"💰итог: {money_form2(price)}₽\n"

    elif rand > 20 and rand <= 32:
        price = int(stavka + (stavka / 2))
        txt = f"👾{mention}, ваша ставка: \n" \
              f"💈множитель выигрыша: 1.5x \n" \
              f"💰итог: {money_form2(price)}₽\n"

    elif rand > 32 and rand <= 55:
        price = 0
        txt = f"👾{mention}, ваша ставка: \n" \
              f"💈множитель выигрыша: 1x \n" \
              f"💰итог: {money_form2(stavka)}₽\n"
    else:
        price = int(0 - stavka)
        txt = f"👾{mention}, ваша ставка: \n" \
              f"💈множитель выигрыша: 0x \n" \
              f"💰итог: {money_form2(price)}₽\n"
        People[kkk]['balance'] -= price

    return {"text": txt, "price": price}


def kmn(rand, prc):
    if rand <= 39:
        price = int(prc + (prc/4))
        txt = "🟢Вы победили! " \
              f"\n💰итог: {price}"
    else:
        price = 0 - int(prc + (prc/5))
        txt = "🔴Вы проиграли( " \
              f"\n💰итог: {price}"

    return {"text": txt, "price": price}
