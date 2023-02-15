#input
inch=int(input('Masukkan jarak dalam inch: '))

#proses
#63360 berasal dari 1760 x 3 x 12 
mile=inch//63360
#36 berasal dari 12 x 3
yard=(inch-(mile*63360))//36
feet=(inch-(mile*63360)-(yard*36))//12
inchh=(inch-(mile*63360)-(yard*36)-(feet*12))

#output
print(inch,f'inch = {mile} mile {yard} yard {feet} feet {inchh} inch')
