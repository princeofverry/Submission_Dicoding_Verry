import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ambil data
day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')


# App title
st.title("Data Analyst")
st.text("Memvisualisasi data by Verry Kurniawan")

st.subheader("Preview Data Day")
st.write(day_df.head())

st.subheader("Preview Data Hour")
st.write(hour_df.head())


st.markdown("""
### Cleaning Data
- Eliminate columns that are not relevant or needed for the analysis.

- Rename columns to make them more descriptive and easier to understand.

- Change the data type of the `date_day` column to datetime format for time-based analysis.

- Modify the data types of specific columns to match the type of information they contain.

- Convert other data as needed to ensure consistency and readiness for further analysis.""")

# Menghapus kolom yang tidak diperlukan
day_df = day_df.drop(columns=['instant', 'atemp', 'holiday', 'workingday'])
hour_df = hour_df.drop(columns=['instant', 'atemp', 'holiday', 'workingday'])

day_df.rename(columns={
    'yr': 'year',
    'dteday': 'date_day',
    'mnth': 'month',
    'weekday': 'day',
    'weathersit': 'weather_situation',
    'windspeed': 'wind_speed',
    'cnt': 'count_total',
    'hum': 'humidity',
    'temp': 'temperature',
    'casual': 'casual_users',
    'registered': 'registered_users',
}, inplace=True)

hour_df.rename(columns={
    'yr': 'year',
    'dteday': 'date_day',
    'mnth': 'month',
    'weathersit': 'weather_situation',
    'windspeed': 'wind_speed',
    'cnt': 'count_total',
    'hum': 'humidity',
    'temp': 'temperature',
    'casual': 'casual_users',
    'registered': 'registered_users',
    'hr': 'hour',
    'weekday': 'day',
}, inplace=True)

# mengubah tipe data dari date_day menjadi datetime
day_df['date_day'] = pd.to_datetime(day_df['date_day'])
hour_df['date_day'] = pd.to_datetime(hour_df['date_day'])

# Mengubah musim menjadi tipe kategori
columns = ['season', 'month', 'day', 'weather_situation']

# konversi menjadi tipe kategori
for column in columns:
    day_df[column] = day_df[column].astype('category')
    hour_df[column] = day_df[column].astype('category')

day_df.info()

# mengubah cuaca
weather_mapping = {
    1: 'Cerah',
    2: 'Berkabut',
    3: 'Hujan_Salju_Ringan',
    4: 'Hujan_Salnju_Lebat'
}

day_df['weather_situation'] = day_df['weather_situation'].map(weather_mapping)
hour_df['weather_situation'] = hour_df['weather_situation'].map(weather_mapping)

# Konversi Musim
season_mapping = {
    1: 'Semi',
    2: 'Panas',
    3: 'Gugur',
    4: 'Salju'
}

day_df['season'] = day_df['season'].map(season_mapping)
hour_df['season'] = hour_df['season'].map(season_mapping)

#Konversi Bulan
month_mapping = {
    1: 'Januari',
    2: 'Februari',
    3: 'Maret',
    4: 'April',
    5: 'Mei',
    6: 'Juni',
    7: 'Juli',
    8: 'Agustus',
    9: 'September',
    10: 'Oktober',
    11: 'November',
    12: 'Desember'
}

day_df['month'] = day_df['month'].map(month_mapping)
hour_df['month'] = hour_df['month'].map(month_mapping)

#Konversi Hari
day_mapping = {
    0: 'Minggu',
    1: 'Senin',
    2: 'Selasa',
    3: 'Rabu',
    4: 'Kamis',
    5: 'Jumat',
    6: 'Sabtu'
}

day_df['day'] = day_df['day'].map(day_mapping)
hour_df['day'] = hour_df['day'].map(day_mapping)

#Konversi Tahun
year_mapping = {
    0: '2011',
    1: '2012'
}

day_df['year'] = day_df['year'].map(year_mapping)
hour_df['year'] = hour_df['year'].map(year_mapping)

# Mengubah kolom 'hour' menjadi format 24 jam (00:00)
hour_df['hour'] = hour_df['hour'].apply(lambda x: '{:02d}:00'.format(x))

# Menampilkan 5 baris pertama untuk memeriksa perubahan
print(hour_df[['hour']].head())

# data sudah dicleaning
st.subheader("Data setelah dicleaning")
st.text("Berikut adalah data day yang sudah dicleaning")
st.write(day_df.head())

st.text("Berikut adalah data hour yang sudah dicleaning")
st.write(hour_df.head())

# EDA
st.header("Exploratory Data Analysis (EDA)")
st.markdown("""
Exploratory Data Analysis (EDA) merupakan tahap eksplorasi data yang telah dibersihkan guna memperoleh insight dan menjawab pertanyaan analisis. Pada prosesnya, kita akan sering menggunakan berbagai teknik dan parameter dalam descriptive statistics yang bertujuan untuk menemukan pola, hubungan, serta membangun intuisi terkait data yang diolah. Selain itu, tidak jarang kita juga menggunakan visualisasi data untuk menemukan pola dan memvalidasi parameter descriptive statistics yang diperoleh.""")


# Mengelompokkan data berdasarkan hari dan agregasi untuk total dan rata-rata
weekday_loan = day_df.groupby('day', observed=True)['count_total'].agg(['sum', 'mean']).reset_index()

# Mencari hari dengan penyewaan tertinggi
most_loan_day = weekday_loan.nlargest(1, 'sum')

# Mencari hari dengan penyewaan terendah
lowest_loan_day = weekday_loan.nsmallest(1, 'sum')

# Pertanyaan 1
with st.expander("1. Pada hari apa sepeda sering dipinjam dan pada hari apa permintaan peminjaman sepeda paling sedikit?"):
    # Menampilkan hari dan total penyewaan tertinggi
    st.write("Penyewaan tertinggi pada hari ", most_loan_day.iloc[0]['day'], "dengan total penyewaan:", most_loan_day.iloc[0]['sum'])
    # Menampilkan hari dan total penyewaan terendah
    st.write("Penyewaan terendah pada hari ", lowest_loan_day.iloc[0]['day'], "dengan total penyewaan:", lowest_loan_day.iloc[0]['sum'])

with st.expander("2. Pada musim mana sepeda cenderung paling populer untuk disewakan berdasarkan volume penggunaan?"):
    # Ambil data berdasarkan musim untuk mendapatkan total penyewaan
    season_loan = day_df.groupby('season', observed=True)['count_total'].sum().reset_index()

    # Menemukan musim dengan penyewaan tertinggi
    most_loan_season = season_loan.loc[season_loan['count_total'].idxmax()]

    # Menampilkan musim dan total penyewaannya saja
    st.write(f"Musim dengan penyewaan sepeda terbanyak adalah {most_loan_season['season']} dengan total {most_loan_season['count_total']} penyewaan.")

# pertanyaan 3
with st.expander("3. Pada jam berapa penyewaan sepeda ramai digunakan?"):
    # Mengelompokkan data berdasarkan jam
    hourly_rentals = hour_df.groupby('hour', observed=True)['count_total'].sum().reset_index()

    # Menemukan jam dengan penyewaan sepeda terbanyak
    peak_hour = hourly_rentals.loc[hourly_rentals['count_total'].idxmax()]

    # Menampilkan jam dan jumlah penyewaan tertinggi
    st.write(f"Jam dengan penyewaan sepeda tertinggi adalah pukul {peak_hour['hour']} dengan total {peak_hour['count_total']} penyewaan.")

# pertanyaan 4
with st.expander("4. Pengaruh bulan terhadap penyewaan sepeda?"):
    # Mengelompokkan data berdasarkan month
    monthly_loan = day_df.groupby('month', observed=True)['count_total'].sum().reset_index()

    # Menampilkan jumlah penyewaan sepeda tiap bulan
    st.write("Jumlah penyewaan sepeda tiap bulan:")
    st.write(monthly_loan)

with st.expander("5. Lebih banyak mana user yang berlangganan dengan yang tidak berlangganan?"):
    # Menghitung jumlah total penyewaan untuk pengguna terdaftar dan non-member
    registered_rentals = day_df['registered_users'].sum()
    casual_rentals = day_df['casual_users'].sum()

    # Menampilkan jumlah total penyewaan tanpa tabel
    st.write(f"Jumlah total penyewaan sepeda untuk pengguna terdaftar: {registered_rentals}")
    st.write(f"Jumlah total penyewaan sepeda untuk pengguna non-member: {casual_rentals}")

    # Perbandingan jumlah penyewaan
    if registered_rentals > casual_rentals:
        st.write("Pengguna yang berlangganan lebih banyak dibandingkan dengan pengguna non-member.")
    else:
        st.write("Pengguna non-member lebih banyak dibandingkan dengan pengguna yang berlangganan.")

st.subheader("Visualisasi Data")
# Visualisasi penyewaan sepeda perhari
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Visualisasi penyewaan sepeda perhari
st.subheader("Penyewaan Sepeda Per Hari")
# Palet warna untuk visualisasi
sns.set_palette("husl")
# Membuat visualisasi dengan barplot horizontal
fig, ax = plt.subplots(figsize=(10, 6))  # Menyimpan figure ke dalam variabel 'fig'
barplot = sns.barplot(y='day', x='sum', data=weekday_loan, ax=ax)
# Menambahkan anotasi pada tiap bar di barplot
for p in barplot.patches:
    barplot.annotate(f'{int(p.get_width())}', 
                     (p.get_width(), p.get_y() + p.get_height() / 2), 
                     ha='left', va='center', 
                     color='black', fontsize=12)
# Menambahkan judul dan label sumbu
ax.set_title('Total Penyewaan Sepeda Berdasarkan Hari', fontsize=16)
ax.set_xlabel('Total Penyewaan Sepeda', fontsize=12)
ax.set_ylabel('Hari', fontsize=12)
# Menambahkan garis grid pada sumbu x
ax.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)

st.subheader("Total Penyewaan sepeda berdasarkan jam")
# Membuat figure dan axes untuk plot
fig, ax = plt.subplots(figsize=(12, 8))
# Membuat lineplot dengan marker 'o'
sns.lineplot(x='hour', y='count_total', data=hourly_rentals, marker="o", ax=ax)
# Menambahkan judul dan label sumbu
ax.set_title('Total Penyewaan Sepeda Berdasarkan Jam', fontsize=16)
ax.set_xlabel('Jam', fontsize=12)
ax.set_ylabel('Total Penyewaan Sepeda', fontsize=12)
# Rotasi label pada sumbu x
ax.set_xticklabels(ax.get_xticks(), rotation=45)
# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)

st.subheader("Total penyewaan sepeda berdasarkan musim")
# Misalkan 'season_rentals' adalah DataFrame yang sudah ada
# Hitung total penyewaan sepeda berdasarkan musim
season_counts = season_loan.groupby('season', observed=False)['count_total'].sum()
# Membuat figure dan axes untuk plot
fig, ax = plt.subplots(figsize=(10, 6))
# Membuat pie chart
ax.pie(season_counts, labels=season_counts.index, autopct='%1.1f%%', startangle=140)
# Menambahkan judul
ax.set_title('Total Penyewaan Sepeda Berdasarkan Musim', fontsize=16)
# Agar pie chart berbentuk lingkaran
ax.axis('equal')
# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)

st.subheader("Jumlah Penyewaan Sepeda Tiap Bulan")
# Membuat figure dan axes untuk plot
fig, ax = plt.subplots(figsize=(10, 6))
# Membuat barplot dengan warna solid
sns.barplot(x='month', y='count_total', data=monthly_loan, color='skyblue', ax=ax)
# Menambahkan judul dan label sumbu
ax.set_title('Jumlah Penyewaan Sepeda Tiap Bulan', fontsize=16)
ax.set_xlabel('Bulan', fontsize=12)
ax.set_ylabel('Jumlah Penyewaan', fontsize=12)
# Memutar label bulan agar lebih mudah dibaca
ax.set_xticklabels(ax.get_xticks(), rotation=45)
# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)


st.subheader("Jumlah Pelanggan per Bulan pada Tahun 2012")
# Membuat figure dan axes untuk plot dengan ukuran (24, 5)
fig, ax = plt.subplots(figsize=(24, 5))
# Menghitung jumlah pelanggan maksimum per bulan
monthly_counts = day_df['count_total'].groupby(day_df['date_day']).max()
# Membuat scatter plot dengan warna biru dan marker 'o'
ax.scatter(monthly_counts.index, monthly_counts.values, c="#90CAF9", s=10, marker='o')
# Membuat line plot untuk jumlah pelanggan maksimum per bulan
ax.plot(monthly_counts.index, monthly_counts.values)
# Penamaan sumbu x dan y
ax.set_xlabel('Bulan', fontsize=12)
ax.set_ylabel('Jumlah', fontsize=12)
# Menambahkan judul
ax.set_title('Grafik Jumlah Pelanggan per Bulan pada Tahun 2012', fontsize=16)
# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)

st.subheader("Perbandingan Pengguna terdaftar vs Non Member")
# Menghitung total penyewaan untuk tiap tipe pengguna
subscription_rentals = day_df[['registered_users', 'casual_users']].sum().reset_index()
# Buat perbandingan untuk tipe dan totalnya
subscription_rentals.columns = ['user_type', 'total_rentals']
# Membuat figure dan axes untuk plot dengan ukuran (10, 6)
fig, ax = plt.subplots(figsize=(10, 6))
# Membuat barplot
sns.barplot(x='user_type', y='total_rentals', data=subscription_rentals, ax=ax, legend=False)
# Menambahkan judul dan label sumbu
ax.set_title('Perbandingan Total Penyewaan: Pengguna Terdaftar vs Pengguna Non Member', fontsize=16)
ax.set_xlabel('Tipe Pengguna', fontsize=12)
ax.set_ylabel('Total Penyewaan', fontsize=12)
# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)

# Hasil Clustering
# Fungsi untuk mengategorikan durasi perjalanan
def categorize_duration(duration):
    if duration <= 10:
        return 'Perjalanan Singkat'
    elif 10 < duration <= 30:
        return 'Perjalanan Menengah'
    else:
        return 'Perjalanan Panjang'

# Simulasi data, ganti dengan data sebenarnya

# Hitung durasi dari count_total
hour_df['duration'] = hour_df['count_total'] / 60  # Asumsi 1 count = 1 menit
hour_df['duration_category'] = hour_df['duration'].apply(categorize_duration)

# Analisis hasil clustering
cluster_stats = hour_df.groupby('duration_category').agg({
    'count_total': 'count',
    'duration': ['mean', 'median'],
    'temperature': 'mean'
})

cluster_stats.columns = ['count', 'duration_mean', 'duration_median', 'temperature_mean']
cluster_stats = cluster_stats.reset_index()

# Tampilkan data dan hasil analisis di Streamlit
st.title("Clustering Analysis - Durasi Perjalanan")

# Tampilkan tabel cluster stats
st.write("Statistik Cluster Durasi Perjalanan:")
st.dataframe(cluster_stats)

# Visualisasi hasil clustering
st.write("Distribusi Kategori Durasi Perjalanan:")
plt.figure(figsize=(12, 6))
sns.barplot(x='duration_category', y='count', data=cluster_stats)
plt.title("Distribusi Kategori Durasi Perjalanan")
plt.xlabel("Kategori Durasi")
plt.ylabel("Jumlah Perjalanan")

# Tampilkan plot di Streamlit
st.pyplot(plt)

st.write("Hasil clustering")
st.markdown("""
- Kategori perjalanan yang paling umum adalah Perjalanan Singkat.
- Rata-rata durasi perjalanan terpanjang terjadi pada kategori Perjalanan Menengah.
- Kategori Perjalanan Menengah memiliki rata-rata suhu tertinggi.
""")


st.markdown("""
### Conclusion

This analysis of bike rentals reveals significant insights into user behavior and preferences throughout the year. The **most borrowed day** is **Friday**, with a remarkable **487,790** rentals, while **Sunday** records the **least** at **444,027** rentals. The **autumn season** stands out as the most popular time for bike rentals, totaling **1,061,129** rentals, showcasing a clear seasonal trend.

In terms of daily activity, the **peak hour** for rentals occurs at **17:00**, with **336,860** bikes rented, indicating a strong evening demand. Monthly data illustrates a gradual increase in rentals, peaking in **August** with **351,194** rentals, before declining towards the end of the year. Notably, there is a stark contrast between **registered and casual users**, with registered users accounting for **2,672,662** rentals compared to **620,017** for casual users, highlighting the value of user retention and engagement in boosting rental numbers.

Overall, understanding these patterns can aid in optimizing bike rental services and enhancing user experiences.
""")

st.caption("Verry 2024")