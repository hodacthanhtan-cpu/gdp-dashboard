import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Cấu hình trang Streamlit
st.set_page_config(page_title="Quản lý điểm sinh viên", layout="wide")

# 1. Hiển thị tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Khởi tạo dữ liệu 10 sinh viên
data = {
    "MSSV": [
        "SV001",
        "SV002",
        "SV003",
        "SV004",
        "SV005",
        "SV006",
        "SV007",
        "SV008",
        "SV009",
        "SV010",
    ],
    "Họ tên": [
        "An",
        "Bình",
        "Chi",
        "Dũng",
        "Hà",
        "Lan",
        "Minh",
        "Nam",
        "Phúc",
        "Trang",
    ],
    "Chuyên cần": [8, 9, 7, 10, 8, 6, 9, 7, 8, 10],
    "Giữa kỳ": [7, 8, 6, 9, 7, 5, 8, 6, 7, 9],
    "Cuối kỳ": [9, 8, 7, 10, 6, 7, 9, 8, 7, 10],
}

df = pd.DataFrame(data)

# Tính điểm Tổng kết
df["Tổng kết"] = (
    0.2 * df["Chuyên cần"] + 0.3 * df["Giữa kỳ"] + 0.5 * df["Cuối kỳ"]
).round(2)


# Hàm xếp loại
def xep_loai(diem):
  if diem >= 8.5:
    return "Giỏi"
  elif diem >= 7.0:
    return "Khá"
  elif diem >= 5.0:
    return "Trung bình"
  else:
    return "Yếu"


df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# 2. Hiển thị bảng điểm của 10 sinh viên
st.subheader("📋 Bảng điểm tổng kết của 10 sinh viên")
st.dataframe(df, use_container_width=True)

# 3. Hiển thị thống kê chung
st.subheader("📊 Thống kê chung")
diem_tb_lop = df["Tổng kết"].mean()
st.write(f"- **Điểm trung bình của lớp:** {diem_tb_lop:.2f}")

sv_max = df.loc[df["Tổng kết"].idxmax()]
sv_min = df.loc[df["Tổng kết"].idxmin()]
st.write(
    f"- **Sinh viên có điểm tổng kết cao nhất:** {sv_max['Họ tên']} ({sv_max['MSSV']}) –"
    f" {sv_max['Tổng kết']}"
)
st.write(
    f"- **Sinh viên có điểm tổng kết thấp nhất:** {sv_min['Họ tên']} ({sv_min['MSSV']}) –"
    f" {sv_min['Tổng kết']}"
)

so_sv_dat = len(df[df["Tổng kết"] >= 5.0])
st.write(f"- **Số sinh viên đạt (>= 5.0):** {so_sv_dat}/10")

# 4. Tạo danh sách xổ xuống (Selectbox) tra cứu sinh viên
st.subheader("🔍 Tra cứu chi tiết sinh viên")
selected_name = st.selectbox(
    "Chọn tên sinh viên để xem chi tiết:", df["Họ tên"].tolist()
)
sv_info = df[df["Họ tên"] == selected_name].iloc[0]

st.info(f"""
- **Họ tên:** {sv_info['Họ tên']}
- **MSSV:** {sv_info['MSSV']}
- **Điểm Chuyên cần:** {sv_info['Chuyên cần']}
- **Điểm Giữa kỳ:** {sv_info['Giữa kỳ']}
- **Điểm Cuối kỳ:** {sv_info['Cuối kỳ']}
- **Điểm Tổng kết:** {sv_info['Tổng kết']}
- **Xếp loại:** {sv_info['Xếp loại']}
""")

# 5. Hiển thị biểu đồ cột điểm tổng kết
st.subheader("📈 Biểu đồ điểm tổng kết của 10 sinh viên")
chart_data = df.set_index("Họ tên")["Tổng kết"]
st.bar_chart(chart_data)

# 6. Thông tin người tạo ứng dụng ở cuối trang Web App (chữ nhỏ)
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: small; color: gray;'>Họ tên:"
    " [Tên của bạn] - MSSV: [Mã số sinh viên của bạn]</p>",
    unsafe_allow_html=True,
)
