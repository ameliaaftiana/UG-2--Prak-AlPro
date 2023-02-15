#input
x1=int(input('x1: '))
y1=int(input('y1: '))
x2=int(input('x2: '))
y2=int(input('y2: '))

#proses
jarak=(((x2-x1)**2)+((y2-y1)**2))**0.5
jarak1=jarak*10
jarak2=int(jarak1)*0.100

#output
print(f'Titik ({x1},{y1}) dan ({x2},{y2}) jaraknya adalah', round(jarak2, 1))