def ilovenahida(udelnilou,susuganyu):
    for pahahutao in range(int(udelnilou),int(susuganyu)):
        if pahahutao%3 == 0 or pahahutao%2 == 0:
            continue
        print(str(pahahutao), end=' ')
udelnilou = input("Masukkan awal deret : ")
susuganyu = input("Masukkan akhir deret : ")
ilovenahida(udelnilou,susuganyu)