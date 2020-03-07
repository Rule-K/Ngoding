#terlihat unik juga ya.. ingat finally akan ter proses tak peduli apapun yang terjadi..
try:
    x = open("text.txt")
    print(x.read())
finally:
    x.close()
#---------------------------
with open("text.txt") as y :
    print(y.read())
"""
Dengan menggunakan #with maka bernama y misalnya
akan tercipta namun hanya pada block indent dari si #with saja
"""