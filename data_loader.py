import pandas as pd

file_path = r"C:\Users\User\Documents\0. Project\Proyek Kecil\KKN PPM 93 - Sidomukti\df.csv"

# Load data
df = pd.read_csv(file_path)
# Load data

# Cek NaN dan perbaiki format
df['ALAMAT'] = df['ALAMAT'].fillna('').str.strip().str.upper()

# Dictionary untuk menyimpan data berdasarkan RT/RW
df_dict = {
    "df": df,
    "df01": df[df['ALAMAT'].str.contains(r'RT 01 RW 01', na=False, case=False)],
    "df02": df[df['ALAMAT'].str.contains(r'RT 02 RW 01', na=False, case=False)],
    "df03": df[df['ALAMAT'].str.contains(r'RT 03 RW 01', na=False, case=False)],
    "df04": df[df['ALAMAT'].str.contains(r'RT 04 RW 02', na=False, case=False)],
    "df05": df[df['ALAMAT'].str.contains(r'RT 05 RW 02', na=False, case=False)],
    "df06": df[df['ALAMAT'].str.contains(r'RT 06 RW 02', na=False, case=False)],
    "df07": df[df['ALAMAT'].str.contains(r'RT 07 RW 03', na=False, case=False)],
    "df08": df[df['ALAMAT'].str.contains(r'RT 08 RW 03', na=False, case=False)],
    "df09": df[df['ALAMAT'].str.contains(r'RT 09 RW 03', na=False, case=False)],
    "df10": df[df['ALAMAT'].str.contains(r'RT 10 RW 04', na=False, case=False)],
    "df11": df[df['ALAMAT'].str.contains(r'RT 11 RW 04', na=False, case=False)],
    "df12": df[df['ALAMAT'].str.contains(r'RT 12 RW 04', na=False, case=False)],
    "df13": df[df['ALAMAT'].str.contains(r'RT 13 RW 05', na=False, case=False)],
    "df14": df[df['ALAMAT'].str.contains(r'RT 14 RW 05', na=False, case=False)],
    "df15": df[df['ALAMAT'].str.contains(r'RT 15 RW 05', na=False, case=False)],
    "df16": df[df['ALAMAT'].str.contains(r'RT 16 RW 06', na=False, case=False)],
    "df17": df[df['ALAMAT'].str.contains(r'RT 17 RW 06', na=False, case=False)],
    "df18": df[df['ALAMAT'].str.contains(r'RT 18 RW 06', na=False, case=False)],
}

# Cek apakah sub-dataset ada isinya
for key, sub_df in df_dict.items():
    print(f"{key}: {len(sub_df)} baris")

# Fungsi untuk mengambil sub-data
def get_df(name):
    return df_dict.get(name, pd.DataFrame())  # Hindari NoneType error