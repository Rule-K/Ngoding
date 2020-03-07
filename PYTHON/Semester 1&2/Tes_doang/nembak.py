my_heart = (input("Aku Cinta Dia atau Tidak.?, Jawab  YA/TIDAK : "))
your_heart = (input("Kamu Cinta Aku atau Tidak.?, Jawab YA/TIDAK : "))

if my_heart != your_heart :
	print("=="*20)
	print("KETIKA CINTA BERTEPUK SEBELAH TANGAN")
elif my_heart and your_heart == "YA" :
	print("=="*20)
	print("MUDAHAN JODOH YA")
elif my_heart and your_heart == "TIDAK":
	print("=="*20)
	print("SABAR MUNGKIN DIA BUKAN JODOH-MU")