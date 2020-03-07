"""
None -- onject yang berarti tidak ada, sama dengan null dalam 
bahasa pemrograman lain..
gambarannya seperti #empty_Value , atau 0 atau [] dan #empty_string ("")
none akan menjadi false ketika di convert ke variable Boolean.
ketika memasuki consle python, dia menjadi #empty_string ("")
None juga bisa di dapatkan dari function yang tidak memiliki #return apapun
statement print() juga bisa berarti None
"""
print(None == None)
print(None)
print(None == True)
print(None == False)

def var():
    print("di bawah none!!")
var = var()    
print(var)
#------
# Fungsi pada dictionaries
"""
Fungsi get juga sangat berfungsi di python, sama kayak indexing
jika data yang di cari tidak ada dalam, divctionary maka get akan
me return data yang lain.. None adalah keluaran default
"""
tes = { "hi" : "Apalah dayaku","ilu" : 33 , True : False, None :"Benar"}
print()
print(tes.get("hi"))
print(tes.get(7))
print(tes.get(5,"Kok gak ada?!"))