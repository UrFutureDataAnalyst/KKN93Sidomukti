import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="Profil Desa",
    default=True)

Mahasiswa1 = st.Page(
    "Daftar Dusun/Dusun I.py",
    title="Dusun I",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Daftar Dusun/Dusun II.py",
    title="Dusun II",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Daftar Dusun/Dusun III.py",
    title="Dusun III",
    icon=":material/person:",
)

#Perlu diperhatikan perubahannya
KREASI = st.Page("tools/KREASI.py", title="Mengenal Lebih Dekat Program Studi Sains Data", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="Coming Soon!!!", icon=":material/search:")

#Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Data Dusun": [Mahasiswa1, Mahasiswa2, Mahasiswa3],
            "Konten": [KREASI,KREASII,]
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()