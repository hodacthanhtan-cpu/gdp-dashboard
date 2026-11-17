import streamlit as st
import pandas as pd
import numpy as np

# Cấu hình trang
st.set_page_config(
    page_title='Bảng dữ liệu Giá nhà',
    page_icon='🏠',
    layout='wide'
)

# 1. Tạo hoặc tải dữ liệu giá nhà
@st.cache_data
def load_housing_data():
    # Thay thế phần này bằng pd.read_csv('du_lieu_gia_nha.csv') nếu bạn có file riêng
    years = list(range(2015, 2026))
    cities = ['TP. Hồ Chí Minh', 'Hà Nội', 'Đà Nẵng', 'Bình Dương', 'Hải Phòng']
    
    np.random.seed(42)
    data = []
    base_prices = {'TP. Hồ Chí Minh': 35, 'Hà Nội': 32, 'Đà Nẵng': 20, 'Bình Dương': 15, 'Hải Phòng': 16}
    
    for city in cities:
        price = base_prices[city]
        for year in years:
            # Mô phỏng mức tăng giá trung bình hàng năm (triệu VNĐ/m2)
            growth = np.random.uniform(1.05, 1.18)
            price = round(price * growth, 1)
            data.append({
                'Khu vực': city,
                'Năm': year,
                'Giá trung bình (Triệu VNĐ/m²)': price
            })
            
    return pd.DataFrame(data)

df = load_housing_data()

# 2. Tiêu đề và mô tả
st.title('🏠 Bảng Dữ Liệu & Biến Động Giá Nhà')
st.markdown('Theo dõi xu hướng giá bất động sản trung bình (Triệu VNĐ/m²) qua các năm theo từng khu vực.')

# 3. Bộ lọc tương tác (giống giao diện GDP Dashboard)
col1, col2 = st.columns([1, 2])

with col1:
    min_year = int(df['Năm'].min())
    max_year = int(df['Năm'].max())
    from_year, to_year = st.slider(
        'Chọn khoảng thời gian:',
        min_value=min_year,
        max_value=max_year,
        value=[2018, max_year]
    )

with col2:
    cities = df['Khu vực'].unique()
    selected_cities = st.multiselect(
        'Chọn khu vực muốn so sánh:',
        cities,
        default=['TP. Hồ Chí Minh', 'Hà Nội', 'Đà Nẵng']
    )

if not selected_cities:
    st.warning("Vui lòng chọn ít nhất một khu vực để hiển thị dữ liệu.")
    st.stop()

# Lọc dữ liệu theo lựa chọn
filtered_df = df[
    (df['Khu vực'].isin(selected_cities)) &
    (df['Năm'] >= from_year) &
    (df['Năm'] <= to_year)
]

# 4. Hiển thị chỉ số tăng trưởng (KPI Cards)
st.subheader(f'Mức giá trung bình năm {to_year} (so với {from_year})')
cols = st.columns(len(selected_cities))

for i, city in enumerate(selected_cities):
    city_data = filtered_df[filtered_df['Khu vực'] == city]
    first_price = city_data[city_data['Năm'] == from_year]['Giá trung bình (Triệu VNĐ/m²)'].values[0]
    last_price = city_data[city_data['Năm'] == to_year]['Giá trung bình (Triệu VNĐ/m²)'].values[0]
    
    growth_pct = ((last_price - first_price) / first_price) * 100
    
    with cols[i]:
        st.metric(
            label=city,
            value=f"{last_price} tr/m²",
            delta=f"{growth_pct:.1f}%"
        )

# 5. Biểu đồ đường trực quan hóa xu hướng
st.subheader('Biểu đồ biến động giá nhà')
chart_data = filtered_df.pivot(index='Năm', columns='Khu vực', values='Giá trung bình (Triệu VNĐ/m²)')
st.line_chart(chart_data)

# 6. Bảng dữ liệu chi tiết
st.subheader('Bảng dữ liệu chi tiết')
st.dataframe(
    chart_data.style.format("{:.1f} tr/m²"),
    use_container_width=True
)
