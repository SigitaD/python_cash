from cs50 import get_float


def main():
    # reikiama graza paimama is get_change f-cijos.
    change = get_change()
    # graza paverciama centais ir suapvalinama.
    cents = round(change * 100)

    # monetu counteris nustatomas nuliui. Kiekviena karta ivykus sekmingam loopui, monetu counteris padides +1.
    coins = 0
    # kol salyga atitinka, atliekami veiksmai. Kai pasiekiama, jog is monetu nebegalima daugiau atimti, nutraukiamas loopas.

    while cents - 25 >= 0:
        cents = cents - 25
        coins += 1
    while cents - 10 >= 0:
        cents = cents - 10
        coins += 1
    while cents - 5 >= 0:
        cents = cents - 5
        coins += 1
    while cents - 1 >= 0:
        cents = cents - 1
        coins += 1
    print(f"{coins}")


def get_change():
    while True:
        change = get_float("What is the change owned?\n")
        if change > 0:
            break
    return change


main()
