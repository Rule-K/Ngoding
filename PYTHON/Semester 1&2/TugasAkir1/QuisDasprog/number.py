nomor  = "00-44 48 5555 8361"
jarak  = len(nomor)
index = 0
baru   = ""
convert = ""

for i in range(len(nomor)) :
	if nomor[i] == "-" or nomor[i] == " " :
		continue
	else :
		baru = baru+nomor[i]
for x in range(len(baru)) :
	if x != 0 :
		if x % 3 == 0 :
			convert = convert + "-"
	
	convert = convert + baru[x]

print("Sebelum: ",nomor)
print("Sesudah: ",convert)
#print(@COPYRIGHT UZIX_CODE")