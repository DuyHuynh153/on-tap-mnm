from abc import ABC, abstractmethod

class DayNS:
    def __init__(self, ten):
        self.ten = ten
        self.danhSach = []

    def them(self, nhanSu):
        self.danhSach.append(nhanSu)

    def thongtin(self):
        print(f"Day nhan su: {self.ten}")
        for ns in self.danhSach:
            ns.thongtin()


    def demBacSi(self):
        count = 0
        for ns in self.danhSach:
            if isinstance(ns, BacSi):
                count += 1
        print(f"So bac si: {count}")



    def sapXepNamSinh(self):
        self.danhSach.sort(key=lambda nhansu: nhansu.getNamSinh())
        print("Danh sach sau khi sap xep:")
        for ns in self.danhSach:
            ns.thongtin()

    def trungBinhNamSinh(self):
        count =0;
        sum = 0;
        for nhansu in self.danhSach:
            sum += nhansu.getNamSinh()
            count += 1

        result = sum/count
        print(f"Trung binh nam sinh: {result}")





class NhanSu (ABC):
    def __init__(self,ten, namsinh):
        self._ten = ten
        self._namsinh = namsinh

    def getNamSinh(self):
        return self._namsinh
    @abstractmethod
    def thongtin(self):
        pass

class SinhVien(NhanSu):
    def __init__(self,ten,namsinh,diem):
        super().__init__(ten,namsinh)
        self.diem = diem

    def thongtin(self):
        print(f"Ten sinh vien: {self._ten}, Nam sinh: {self._namsinh}, Diem: {self.diem}")

class BacSi(NhanSu):
    def __init__(self,ten,namsinh,chuyenkhoa):
        super().__init__(ten,namsinh)
        self.chuyenkhoa = chuyenkhoa

    def thongtin(self):
        print(f"Ten bac si: {self._ten}, Nam sinh: {self._namsinh}, Chuyen khoa: {self.chuyenkhoa}")

class GiangVien(NhanSu):
    def __init__(self,ten,namsinh,chuyenmon):
        super().__init__(ten,namsinh)
        self.chuyenmon = chuyenmon

    def thongtin(self):
        print(f"Ten giang vien: {self._ten}, Nam sinh: {self._namsinh}, chuyen mon: {self.chuyenmon}")


sv1 = SinhVien("Nguyen Van A", 1999, 8.5)
# sv1.thongtin()
gv1 = GiangVien("Tran Van B", 1980, "Toan")
# gv1.thongtin()
bs1 = BacSi("Le Thi C", 1970, "Nhi")
# bs1.thongtin()


gv2 = GiangVien("Tran Van D", 1980, "Ly")
bs2 = BacSi("Le Thi E", 1970, "Mat")

nhansu1 = DayNS("Khoa CNTT")
nhansu1.them(sv1)
nhansu1.them(gv1)
nhansu1.them(gv2)
nhansu1.them(bs1)
nhansu1.them(bs2)

nhansu1.thongtin()

nhansu1.demBacSi()

nhansu1.sapXepNamSinh()

nhansu1.trungBinhNamSinh()



