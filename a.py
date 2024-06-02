

lista = ["lap trinh truc quan","cau truc du lieu python", "khai pha du lieu","chuyen de phan tich du lieu"]
listb = [101,102,103,104]

listc = [[itema, listb[lista.index(itema)]] for itema in lista]


listh = [f"{itema} , {listb[lista.index(itema)]}" for itema in lista]
for item in listc:
	print(item)

for item in listh:
	print(item)
