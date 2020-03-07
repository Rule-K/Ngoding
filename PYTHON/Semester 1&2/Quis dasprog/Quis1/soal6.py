def fun(list):
  jml = 0
  for i in list :
    jml += i
    a = jml/len(list)
  return a

hasil = fun([12,13,13,432,43])
print("jumlah input %s dengan jumlah nila %s dengan Rata2 %s"%(hasil))