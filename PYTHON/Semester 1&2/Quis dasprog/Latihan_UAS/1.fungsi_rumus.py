#====================
#Deretan Mencari Luas
#====================
#Mencari Luas segitiga
def segitiga_luas(alas,tinggi):
    luas_s = 0.5 * alas * tinggi
    return luas_s,alas,tinggi
#Mencari Luas lIngkaran
def lingkaran_luas(jari_jari):
    luas_l = 3.14 * jari_jari ** 2
    return luas_l,jari_jari
#mencari Luas Jajaran Genjang
def jajaran_genjang_luas(alas,tinggi):
    luas_jg = alas * tinggi
    return luas_jg,alas,tinggi
#Mencari Luas Layang Layang
def layang_layang_luas(diagonal1,diagonal2):
    luas_ll = 0.5 * diagonal1 * diagonal2
    return luas_ll,diagonal1,diagonal2
#Mencari Luas Trapesium
def Trapesium_luas(tinggi):
    jumlah_sisi_sejajar = 0.5
    luas_t = jumlah_sisi_sejajar * tinggi
    return luas_t,tinggi
#====================
#Deretan Mencari volume
#====================
#menghitung Volume lingkaran
def lingkaran_volume(jari_jari):
    volume_l = 3/4 * 3.14 * jari_jari
    return volume_l, jari_jari
#Menghitung Volume kerucut
def kerucut_volume(jari_jari,tinggi):
    volume_k = 1/3 * 3.14 * jari_jari ** 2 * tinggi
    return volume_k,jari_jari,tinggi
# Menghitung Volume silinder
def silinder_volume(jari_jari,tinggi):
    volume_s = 3.14 * jari_jari**2 * tinggi
    return volume_s,jari_jari,tinggi
#mengubah Ke variabel untuk luas
segitiga_luas = segitiga_luas(20,20)
lingkaran_luas = lingkaran_luas(30)
jajaran_genjang_luas = jajaran_genjang_luas(23,43)
layang_layang_luas = layang_layang_luas(65,23)
Trapesium_luas = Trapesium_luas(100)
#mengubah ke variabel untuk volume
lingkaran_volume = lingkaran_volume(1.23)
kerucut_volume = kerucut_volume(33.1,30)
silinder_volume = silinder_volume(55.4,11.2)
#Print Variabel untuk luas
print("="*60)
print("1. Luas Segitiga adalah %s, dengan alas %s dan Tinggi %s"%(segitiga_luas))
print("2. Luas lingkaran adalah %s dengan jari-jari %s"%(lingkaran_luas))
print("3. Luas jajaran Genjang adalah %s dengan alas %s dan tinggi %s"%(jajaran_genjang_luas))
print("4. Luas Layang2 adalah %s dengan diagonal1 %s dan Diangonal2 %s"%(layang_layang_luas))
print("5. Luas Trapesium adalah %s dengan tinggi %s"%(Trapesium_luas))
print("="*60)
#print ke variabel untuk volume
print("6. Volume lingkaran adalah %s dengan jari-jari %s"%(lingkaran_volume))
print("7. Volume kerucut adalah %s dengan jari-jari %s dan tinggi %s"%(kerucut_volume))
print("8. volume silinder adalah %s dengan jari-jari %s dan tinggi %s"%(silinder_volume))
print("="*60)