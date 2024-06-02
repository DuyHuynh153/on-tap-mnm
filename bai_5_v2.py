# bai 3 -----------

# lista = ["mon a", "mon b", "mon c", "mon d"]
# listb = [ 1,2,3,4]

# listc = [f"{item}, {listb[lista.index(item)]}" for item in lista]

# for r in listc:
# 	print(r)


# maMonHoc = {"lap trinh python":1, "he thong":2, "nguyen li":3, "hoc may":4}
# maNganh = {1:"cntt", 2:"ktmm", 3:"httt",4:"hhhh"}


# result ={}
# for monHoc in maMonHoc:
# 	result[monHoc] = maNganh[maMonHoc[monHoc]]


# print(result)

# -------------------xong------------


# bai 4

from abc import ABC, abstractmethod

class CongTy:
	def __init__(self,maCongTy, maKhuVuc):
		self.maCongTy = maCongTy
		self.maKhuVuc = maKhuVuc

	def mota(self):
		print(f"ma cong ty: {self.maCongTy} - ma khu vuc: {self.maKhuVuc}")

class NhanVien(CongTy):
	def __init__(self, tenNhanVien, tuoiNhanVien, maCongTy, maKhuVuc):
		self.tenNhanVien = tenNhanVien
		self.tuoiNhanVien = tuoiNhanVien
		super().__init__(maCongTy,maKhuVuc)


	def mota(self):
		print(f"ten nha vien: {self.tenNhanVien} - tuoi nhan vien: {self.tuoiNhanVien}")
		super().mota()

# nv = NhanVien("tran van a", 24, 9752, "vietnam")
# nv.mota()

# bai 4b

class DayNS:
	def __init__(self,ten):
		self.ten = ten
		self.danhSach = []

	def themNhanSu(self, nhansu):
		self.danhSach.append(nhansu)

	def thongtin(self):
		print(f"ten nhan su: {self.ten}")

		for ns in self.danhSach:
			ns.thongtin()

	def demBacSi(self):
		count = 0;
		for ns in self.danhSach:
			if isinstance(ns, BacSi):
				count += 1

		print(f"so nhan su la ba si: {count}")

	def sapXepNamSinh(self):
		self.danhSach.sort(key=lambda nhansu: nhansu.getNamSinh())

		print("danh sach sau khi sap xep theo nam sinh:")
		for ns in self.danhSach:
			ns.thongtin()

	def trungBinhNamSinh(self):
		count = 0
		sum = 0
		for ns in self.danhSach:
			if isinstance(ns,GiangVien):
				sum += ns.getNamSinh()
				count += 1

		print(f"nam sinh trung binh cua giang vien: {sum/count}")



class NhanSu(ABC):
	def __init__(self,ten,namsinh):
		self._ten = ten
		self._namsinh = namsinh

	def getNamSinh(self):
		return self._namsinh


	@abstractmethod
	def thongtin(self):
		pass

class SinhVien(NhanSu):
	def __init__(self, ten, namsinh, diem):
		super().__init__(ten, namsinh)
		self.diem = diem

	def thongtin(self):
		print(f"Sinh vien ten: {self._ten} - nam sinh: {self._namsinh} - diem: {self.diem}")

class GiangVien(NhanSu):
	def __init__(self, ten, namsinh, chuyenmon):
		super().__init__(ten, namsinh)
		self.chuyenmon = chuyenmon

	def thongtin(self):
		print(f"giang vien ten: {self._ten} - nam sinh: {self._namsinh} - chuyen mon: {self.chuyenmon}")

class BacSi(NhanSu):
	def __init__(self, ten, namsinh, chuyenkhoa):
		super().__init__(ten, namsinh)
		self.chuyenkhoa = chuyenkhoa

	def thongtin(self):
		print(f"bac si ten: {self._ten} - nam sinh: {self._namsinh} - chuyen khoa: {self.chuyenkhoa}")


sv = SinhVien("lam duy", 2002, 9.7)
# sv.thongtin()

gv = GiangVien("le van b", 1970, "toan")
# gv.thongtin()
gv2 = GiangVien("giang vien 2", 1995, "toan")

bs = BacSi("nguyen thi aa", 1950,"phau thuat")
bs2 = BacSi("bac si 2", 1975,"hoi suc")

# bs.thongtin()

ns = DayNS("nhan su 1")
ns.themNhanSu(sv)
ns.themNhanSu(gv)
ns.themNhanSu(gv2)
ns.themNhanSu(bs)
ns.themNhanSu(bs2)
ns.thongtin()

ns.demBacSi()

ns.sapXepNamSinh()

ns.trungBinhNamSinh()