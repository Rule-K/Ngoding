#materi Sebelumnya
"""
list = [1,2,3,4,5,6,7,8,9]
tuple = (1,2,3,4,5,6,7,8,9)
set = {1,2,3,4,5,6,7,8,9}
"""
#===================
#Dictionary
game = {'Nahrul':'Crash Bandicots',
		'Sahril':'Cewek',
		'Hery':'Moba Analog',
		'Asqolani':'Nggak main game',
		'Tommy':'Nggak tau gue',
		'Ten':'Nggak main juga',
		'Feni':'Moba Analog',
		'Sayyid':'Moba Analog'}

makan = {'Nahrul':'Tempe',
		'Sahril':'Teri',
		'Hery':'Ikan',
		'Asqolani':'Ba\'wan',
		'Tommy':'Pecel',
		'Ten':'Pindang',
		'Feni':'Tahu isi',
		'Sayyid':'Lasagna',
		}
#===============
"""YAng begini Juga Bisa Loooo"""
Member_1 = {"Nama":"Nahrul Khayattullah",
			"Kelas":"TI-D",
			"Semester":"Semester 1",
			"Prodi":"Teknik Informatika"}

Member_2 = {"Nama":"Hidayatul Aeni",
			"Kelas":"1 Sekolah Dasar",
			"Semester":"Semester 2",
			"Prodi":"Masih Anak SD"}
#===============
Member_list = {1:Member_1 ,2:Member_2}
#===============
print(game["Nahrul"])
print(game["Sahril"])
print(game.keys())
print(game.values())
print(game.items())
#==========================
print(makan["Nahrul"])
print(makan["Sahril"])
print(makan.keys())
print(makan.values())
print(makan.items())
#==================
print(Member_list[1])
print(Member_list[2])