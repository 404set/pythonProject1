import datetime

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    if True:
        print("Cimbrel")
        dias_semana = {
            0: "lunes",
            1: "martes",
            2: "miércoles",
            3: "jueves",
            4: "viernes",
            5: "sábado",
            6: "domingo"
        }

        hoy = datetime.datetime.today()
        print(hoy.weekday())
        dia_semana = dias_semana[hoy.weekday()]

        print("Hoy es", dia_semana)
    else:
        # noinspection PyUnreachableCode
        print("seco")



# noinspection PyUnreachableCode
def nectar ():
    if True:
        print("Answer")
        print("True")
    else:
        print("-")
        print("False")

    # Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print_hi('PyCharm')
    nectar()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
