#input
detik=int(input('Masukkan detik: '))

#proses
#86400 berasal dari dalam 1 hari terdiri 86400 detik
hari=detik//86400
#3600 berasal dari dalam 1 jam terdiri 3600 detik
jam=(detik-(hari*86400))//3600
#60 berasal dari dalam 1 menit terdiri dari 60 detik
menit=(detik-(hari*86400)-(jam*3600))//60
detikk=(detik-(hari*86400)-(jam*3600)-(menit*60))



#output
print (detik,f'detik = {hari} hari, {jam} jam, {menit} menit, {detikk} detik')