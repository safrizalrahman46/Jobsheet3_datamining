# # import seaborn as sns
# # import matplotlib.pyplot as plt  # Add this
# # df = sns.load_dataset('titanic')
# # df.head()
# # # df.info()
# # # df.describe()
# # # df['age'].fillna(df['age'].mean(), inplace=True)

# # # df['age' ] = df.groupby('sex') ['age'].transform(lambda x: x. fillna(x.mean()))


# # # sns.histplot(df['age'].dropna(), kde=True)

# # plt.figure(figsize=(8,6))
# # sns.countplot(x='class', data=df, palette='Set1')
# # plt.title('Distribusi Kelas Tiket Titanic', fontsize=16)
# # plt.xlabel('Kelas Tiket', fontsize=14)
# # plt.ylabel('Jumlah Penumpang', fontsize=14)
# # # plt.show()

# # # Hitung jumlah penumpang di setiap kelas
# # class_counts = df['class'].value_counts()

# # # Tampilkan hasil dalam bentuk teks
# # print("Jumlah Penumpang di Setiap Kelas Tiket:")
# # print(class_counts)

# # # umlah Donumpang di Cotian Velac Tiket.
# # plt.show()  # Add this line

# # import seaborn as sns

# # # Melihat dataset yang tersedia
# # print(sns.get_dataset_names())

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load dataset penguins
# df = sns.load_dataset("penguins")

# # Menampilkan 5 data pertama
# print(df.head())

# # Informasi dataset
# print(df.info())

# # Statistik deskriptif
# print(df.describe())
# # Mengisi nilai NaN dengan mean dari setiap kolom numerik
# df.fillna(df.mean(numeric_only=True), inplace=True)

# # Mengecek kembali apakah masih ada data kosong
# print(df.isnull().sum())

# # Grafik distribusi berat badan penguin
# sns.histplot(df['body_mass_g'], kde=True)
# plt.show()

# # Grafik sebaran panjang paruh vs berat badan
# sns.scatterplot(x=df['bill_length_mm'], y=df['body_mass_g'], hue=df['species'])
# plt.show()

# # Grafik boxplot per spesies
# sns.boxplot(x=df['species'], y=df['body_mass_g'])
# plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df_teman = pd.read_excel("teman_sekelas.xlsx")

# Mengecek apakah ada data kosong
missing_values = df_teman.isnull().sum()

# Mengisi data kosong dengan mean (hanya untuk kolom numerik)
df_teman.fillna(df_teman.mean(numeric_only=True), inplace=True)

# Statistik deskriptif
stats_summary = df_teman.describe()

# Visualisasi Pengeluaran BBM per Bulan
plt.figure(figsize=(8,5))
sns.histplot(df_teman['Pengeluaran BBM (per bulan)'], kde=True, bins=10)
plt.title("Distribusi Pengeluaran BBM per Bulan")
plt.xlabel("Pengeluaran BBM (IDR)")
plt.ylabel("Frekuensi")
plt.show()

# Scatterplot antara IPK dan Pendapatan Bulanan
plt.figure(figsize=(8,5))
sns.scatterplot(x=df_teman['IPK'], y=df_teman['Pendapatan Bulanan (IDR)'], hue=df_teman['Jenis Kelamin'])
plt.title("Hubungan antara IPK dan Pendapatan Bulanan")
plt.xlabel("IPK")
plt.ylabel("Pendapatan Bulanan (IDR)")
plt.show()

# Boxplot tinggi badan berdasarkan jenis kelamin
plt.figure(figsize=(8,5))
sns.boxplot(x=df_teman['Jenis Kelamin'], y=df_teman['Tinggi Badan (cm)'])
plt.title("Distribusi Tinggi Badan berdasarkan Jenis Kelamin")
plt.xlabel("Jenis Kelamin")
plt.ylabel("Tinggi Badan (cm)")
plt.show()

# Menampilkan informasi data kosong dan statistik deskriptif
missing_values, stats_summary
