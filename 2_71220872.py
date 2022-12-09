def mantudaribapaknyaklee(mantunyadiluc):
    bapaknyadiluc=len(mantunyadiluc)
    for ketekklee in range(bapaknyadiluc):
        print(mantunyadiluc[0:ketekklee+1])
    for pantatningguang in range (bapaknyadiluc):
        print(mantunyadiluc[0:(bapaknyadiluc-pantatningguang-1)])
mantunyadiluc=input("masukkan nama : ")
mantudaribapaknyaklee(mantunyadiluc)