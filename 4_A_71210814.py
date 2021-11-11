print("====MASUKAN JUMLAH MAKANAN YANG DIPESAN====")

a = int(input("IKAN BAKAR       RP 25.000,00    : "))
b = int(input("ES DOGER         RP 6.000,00     : "))
c = int(input("RUJAK CINGUR     RP 8.000,00     : "))

print("====TOTAL====")

TIB = a*25000
TED = b*6000
TRC = c*8000

print("TOTAL IKAN BAKAR         : Rp ", int(TIB))
print("TOTAL ES DOGER           : Rp ", int(TED))
print("TOTAL RUJAK CINGUR       : Rp ", int(TRC))

hasil = TIB + TED + TRC

print("Jumlah tital biaya yang harus dibayar adalah Rp ", float(hasil))
