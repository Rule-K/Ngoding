def absen(list):
    hadir = int(list[0]) * 10 /100
    ugas = int(list[1]) * 25 /100
    utse = int(list[2]) * 30 / 100
    uase = int(list[3]) *35 / 100
    #===============
    nilai = hadir + ugas + utse + uase
    
    if nilai > 80:
        print('Nilai Anda A')
    elif nilai > 70:
        print('Nilai Anda B')
    elif nilai > 60:
        print('Nilai Anda C')
    elif nilai > 50:
        print('Nilai Anda D')
    else:
        print('Maaf Anda Tidak Lulus')
        print("-"*60)
    return hadir,ugas,utse,uase,nilai

print("="*60)
Nilai_nya = input("Masukan 4 Nilai, pisah dengan Spasi: ").split()        
absensi = absen(Nilai_nya)
print("Kehadiran %s , Tugas %s, UTS %s, UAS %s, Nilai akhir %s"%(absensi))
print("="*60)