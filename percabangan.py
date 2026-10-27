# variabel dan tipe data

nama = input("Masukan Nama Mahasiswa :")
kelas = input ("kelas: ")

nalgoritma = int (input("Masukan Nilai Algoritma :"))
npraktek = int (input("Masukan Nilai Praktek :"))
nbhs_inggris = int (input("Masukan Nilai bhs_inggris :"))
nagama = int(input("Masukan Nilai Agama :"))
nseni_tari = int(input("Masukan Nilai Seni_tari :"))
nbudaya = int(input("Masukan Nilai Budaya :"))
nbasis_data =int(input("Masukan Nilai Basis_data :"))
nilai_rata_rata = (nalgoritma + npraktek + nbhs_inggris + nagama + nseni_tari + nbudaya + nbasis_data ) / 7
print (nilai_rata_rata)


#penentuan lulus atau tidak
if nilai_rata_rata >=90 and nilai_rata_rata<=100:
   # kondisi jika terpenuhi 
   # maka
   print("Nilai: A")
elif nilai_rata_rata >=80 and nilai_rata_rata<=90:
   print("Nilai: B")
elif nilai_rata_rata >=70 and nilai_rata_rata<=80:
   print("Nilai: C")
elif nilai_rata_rata >=60 and nilai_rata_rata <=70:
   print("nilai: D")
else:
   print("Nilai: E")
