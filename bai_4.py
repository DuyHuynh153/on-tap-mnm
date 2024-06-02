class CONGTY:
    def __init__(self,maCongTy, maKhuVuc):
        self.maCongTy = maCongTy
        self.maKhuVuc = maKhuVuc

    def mota(self):
        print("Ma cong ty: ", self.maCongTy)
        print("Ma khu vuc: ", self.maKhuVuc)


class NHANVIEN(CONGTY):
    def __init__(self,tenNhanVien,tuoiNhanVien, maCongTy, maKhuVuc):
        self.tenNhanVien = tenNhanVien
        self.tuoiNhanVien = tuoiNhanVien
        super().__init__(maCongTy, maKhuVuc)

    def mota(self):
        print("Ten nhan vien: ", self.tenNhanVien)
        print("Tuoi nhan vien: ", self.tuoiNhanVien)
        super().mota()

nhanVien = NHANVIEN("tran Van A", 24, 9257, "VIETNAM")

nhanVien.mota()

