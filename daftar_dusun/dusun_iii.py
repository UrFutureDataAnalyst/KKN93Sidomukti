import streamlit as st
from data_loader import get_df
import pandas as pd
import plotly.express as px

# Memuat dataframe sesuai RT
rt_dfs = {
    "RT XIII RW V": get_df("df13"),
    "RT XIV RW V": get_df("df14"),
    "RT XV RW V": get_df("df15"),
    "RT XVI RW VI": get_df("df16"),
    "RT XVII RW VI": get_df("df17"),
    "RT XVIII RW VI": get_df("df18"),
}

# Pilih menu RT
selected_menu = st.selectbox("Pilih RT", list(rt_dfs.keys()))

# Ambil data dari dataframe berdasarkan RT
df = rt_dfs[selected_menu].copy()

# Abaikan data dengan usia > 90
df = df[df['USIA'] <= 90]

# Dashboard
st.markdown(f"## Dashboard Warga - {selected_menu}")

if not df.empty:
    # Visualisasi Jenis Kelamin
    st.subheader("Distribusi Jenis Kelamin")
    fig_jk = px.pie(df, names='JENIS KELAMIN', title='Persentase Jenis Kelamin')
    st.plotly_chart(fig_jk)

    # Kelompok Usia
    st.subheader("Distribusi Kelompok Usia")
    bins = [0, 12, 18, 35, 50, 65, 90]
    labels = ['Anak-anak (0-12)', 'Remaja (13-18)', 'Dewasa Muda (19-35)', 'Paruh Baya (36-50)', 'Lansia Awal (51-65)', 'Lansia (>65)']
    df['Kelompok Usia'] = pd.cut(df['USIA'], bins=bins, labels=labels, right=False)
    usia_counts = df['Kelompok Usia'].value_counts(normalize=True).reset_index()
    usia_counts.columns = ['Kelompok Usia', 'Persentase']
    usia_counts['Persentase'] *= 100
    fig_usia = px.bar(usia_counts, x='Kelompok Usia', y='Persentase', labels={'Kelompok Usia': 'Kelompok Usia', 'Persentase': 'Persentase (%)'}, title='Distribusi Kelompok Usia')
    st.plotly_chart(fig_usia)

    # Visualisasi Agama
    st.subheader("Distribusi Agama")
    agama_counts = df['AGAMA'].value_counts(normalize=True).reset_index()
    agama_counts.columns = ['Agama', 'Persentase']
    agama_counts['Persentase'] *= 100
    fig_agama = px.bar(agama_counts, x='Agama', y='Persentase', labels={'Agama': 'Agama', 'Persentase': 'Persentase (%)'}, title='Distribusi Agama')
    st.plotly_chart(fig_agama)

    # Visualisasi Pendidikan
    st.subheader("Distribusi Pendidikan")
    pendidikan_counts = df['PENDIDIKAN'].value_counts(normalize=True).reset_index()
    pendidikan_counts.columns = ['Pendidikan', 'Persentase']
    pendidikan_counts['Persentase'] *= 100
    fig_pendidikan = px.bar(pendidikan_counts, x='Pendidikan', y='Persentase', labels={'Pendidikan': 'Pendidikan', 'Persentase': 'Persentase (%)'}, title='Distribusi Pendidikan')
    st.plotly_chart(fig_pendidikan)

    # Visualisasi Pekerjaan
    st.subheader("Distribusi Pekerjaan")
    pekerjaan_counts = df['PEKERJAAN'].value_counts(normalize=True).reset_index()
    pekerjaan_counts.columns = ['Pekerjaan', 'Persentase']
    pekerjaan_counts['Persentase'] *= 100
    fig_pekerjaan = px.bar(pekerjaan_counts, x='Pekerjaan', y='Persentase', labels={'Pekerjaan': 'Pekerjaan', 'Persentase': 'Persentase (%)'}, title='Distribusi Pekerjaan')
    st.plotly_chart(fig_pekerjaan)
else:
    st.warning("Tidak ada data untuk RT yang dipilih.")