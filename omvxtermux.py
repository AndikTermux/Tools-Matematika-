import os
os.system('clear')
print '\t>>>>> OmVx Termux <<<<<'
print 
print '1. Penjumlahan'
print '2. Pengurangan'
print '3. Perkalian'
print '4. Pembagian'
print '5. Sisa Bagi'
print '6. Pemangkatan'
print
pilih = input(' Pilih Menu : ')

if pilih == 1:
    print 
    angka_1 = input(' Angka Pertama : ')
    angka_2 = input(' Di Jumlah : ')
    total = angka_1 + angka_2
    print 'Totalnya Cuk : ' , total
    
if pilih == 2:
	print
	angka_1 = input(' Angka Pertama : ')
	angka_2 = input(' Di Kurang : ')
	total = angka_1 - angka_2
	print 'Totalnya Cuk : ' , total

if pilih == 3:
	print
	angka_1 = input(' Angka Pertama : ')
	angka_2 = input(' Di Kali : ')
	total = angka_1 * angka_2
	print 'Totalnya Cuk : ' , total 
	
if pilih == 4:
	print
	angka_1 = input(' Angka Pertama : ')
	angka_2 = input(' Di Bagi : ')
	total = angka_1 / angka_2
	print 'Totalnya Cuk : ' , total
	
if pilih == 5:
	print
	angka_1 = input(' Angka Pertama : ')
	angka_2 = input(' Angka Kedua : ')
	total = angka_1 % angka_2
	print 'Totalnya Cuk : ' , total
	
if pilih == 6:
	print
	angka_1 = input(' Angka Pertama : ')
	angka_2 = input(' Di Pangkat : ')
	total = angka_1 ** angka_2
	print 'Totalnya Cuk : ' , total
	
else:
    print
    print 'Menunya Gaada Goblok !'
    	
    
	
	
	
    
    	