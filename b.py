maMonHoc = {"lap trinh python": 1, "he thong thong minh": 2, "khai pha du lieu": 3, "chuyen de phan tich du lieu": 4}

maNganh = {1:"Cntt", 2:"KHDL", 3:"ktpm", 4:"ttnt"}


result = {}
for key in maMonHoc:
    result[key] = maNganh[maMonHoc[key]]


print(result)


