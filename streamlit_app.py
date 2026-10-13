import pandas as pd

# 1. Khởi tạo dữ liệu cho 10 sinh viên
data = {
    'Ho_va_ten': [
        'Nguyễn Văn A', 'Trần Thị B', 'Lê Hoàng C', 'Phạm Minh D', 'Vũ Thị E',
        'Hoàng Văn F', 'Đỗ Thị G', 'Bùi Minh H', 'Phan Thanh I', 'Ngô Thị K'
    ],
    'Chuyen_can': [9.0, 10.0, 7.0, 9.0, 9.0, 10.0, 7.0, 7.0, 9.0, 8.0],
    'Giua_ky': [5.8, 5.3, 9.3, 8.0, 8.5, 5.1, 9.8, 9.2, 6.1, 5.9],
    'Cuoi_ky': [5.1, 5.8, 7.1, 6.6, 5.7, 7.7, 4.8, 5.8, 6.2, 6.7]
}

# 2. Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# 3. Tính điểm tổng kết (20% Chuyên cần + 30% Giữa kỳ + 50% Cuối kỳ) và làm tròn 2 chữ số
df['Tong_ket'] = (0.2 * df['Chuyen_can'] + 0.3 * df['Giua_ky'] + 0.5 * df['Cuoi_ky']).round(2)

# 4. Định nghĩa hàm xếp loại sinh viên dựa trên điểm tổng kết
def phan_loai(diem):
    if diem >= 8.5:
        return 'Giỏi'
    elif diem >= 7.0:
        return 'Khá'
    elif diem >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

# 5. Tạo thêm cột Xep_loai bằng cách áp dụng hàm phan_loai vào cột Tong_ket
df['Xep_loai'] = df['Tong_ket'].apply(phan_loai)

# 6. Hiển thị bảng dữ liệu sinh viên
print("--- DANH SÁCH SINH VIÊN ---")
print(df)
print("\n" + "="*50 + "\n")

# 7. THỰC HIỆN YÊU CẦU 4: THỐNG KÊ
print("--- KẾT QUẢ THỐNG KÊ ---")

# 8: Tính điểm tổng kết trung bình của lớp
diem_tb_lop = df['Tong_ket'].mean()
print(f"- Điểm tổng kết trung bình của lớp: {diem_tb_lop:.2f}")

# 9: Tìm sinh viên có điểm tổng kết cao nhất
sv_cao_nhat = df[df['Tong_ket'] == df['Tong_ket'].max()]
print("- Sinh viên có điểm tổng kết cao nhất:")
for index, row in sv_cao_nhat.iterrows():
    print(f"  + {row['Ho_va_ten']} ({row['Tong_ket']} điểm)")

# 10: Tìm sinh viên có điểm tổng kết thấp nhất
sv_thap_nhat = df[df['Tong_ket'] == df['Tong_ket'].min()]
print("- Sinh viên có điểm tổng kết thấp nhất:")
for index, row in sv_thap_nhat.iterrows():
    print(f"  + {row['Ho_va_ten']} ({row['Tong_ket']} điểm)")

# 11: Đếm số sinh viên đạt (điểm tổng kết >= 5)
so_sv_dat = df[df['Tong_ket'] >= 5.0].shape[0]
print(f"- Số sinh viên đạt (Tổng kết >= 5): {so_sv_dat} sinh viên")
