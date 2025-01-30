import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
import plotly.express as px
import pandas as pd
from data_loader import get_df

df = get_df("df")
# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # menampilkan gambar di tengah
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"Sebagai: {data_list[i]['sebagai']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Program Studi: {data_list[i]['program_studi']}")
            st.write(f"Motto Hidup: {data_list[i]['motto_hidup']}")


# JANGAN DIUBAH

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>Desa Sidomukti</h1>
        <p style='font-size: 2em;'>Kecamatan Sekampung</p>
        <p style='font-size: 2em;'>Kabupaten Lampung Timur</p>
    </div>
    """,
    unsafe_allow_html=True,
)
url = "https://drive.google.com/uc?export=view&id=1KHyILfd0e2Oup-S4LFe9qvWnKzLK65dX"
url1 = "https://drive.google.com/uc?export=view&id=1W-HkJnRAfdRitGy2kqMxDy9b1s81TVcX"
def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])  # Menggunakan kolom dengan rasio 1:2:1
    with col1:
        st.write("")  # Menyisakan kolom kosong
    with col2:
        st.image(load_image(url), use_column_width="True", width=350)
    with col3:
        st.write("")  # Menyisakan kolom kosong
layout(url)
layout(url1)
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "Dashboard Desa", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected
menu = streamlit_menu()
if menu == "Home":
    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>Deskripsi Kelompok</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify;">Sebuah Desa yang terletak di wilayah Kecamatan Sekampung, Kabupaten Lampung Timur, Sidomukti bedeng 55 yang berbatasan  dengan way Sekampung adalah masyarakat yang mayoritas adalah petani persawahan.
Desa Sidomukti berdiri pada tahun 1941 yang dipimpin oleh seorang kepala desa bernama Karto Karyo hingga sekarang dipimpin oleh seorang pemimpin asli putra daerah dari Desa Sidomukti bernama Bapak Siswanto.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=19xXSKXVGA6d8Tk-BKlDrjblpSt2lc5Zs"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Kami sebagai perwakilan dari KKN PPM Itera ke-14, mendapatkan amanah untuk melaksanakan salah satu Tri Dharma perguruan tinggi, yakni pengabdian di Desa Sidomukti, Kecamatan Sekampung, Kabupaten Lampung Timur. Dashboard ini adalah salah satu hasil implementasi keilmuan yang diajarkan kepada kami, yang bertujuan untuk menciptakan dashboard interaktif sebagai dasar dari pengambilan keputusan yang akan dilaksanakan oleh perangkat desa Sidomukti.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
    home_page()

elif menu == "Dashboard Desa":
    def dashboard_page():
        df = get_df("df")  # Ambil data dari fungsi `get_df`

        if df is None:
            st.error("Data tidak ditemukan! Pastikan sumber data valid.")
            return  

        # Salin data agar df asli tidak berubah
        df_filtered = df.copy()

        # Pastikan kolom 'USIA' ada sebelum memfilternya
        if 'USIA' not in df_filtered.columns:
            st.error("Kolom 'USIA' tidak ditemukan dalam dataset.")
            return

        # Filter data berdasarkan usia
        df_filtered = df_filtered[df_filtered['USIA'] <= 90]

        if df_filtered.empty:
            st.warning("Tidak ada data setelah filter.")
            return

        # Debug: Tampilkan data pertama untuk memastikan data valid
        st.write("Contoh Data:", df_filtered.head())

        # **1. Visualisasi Jenis Kelamin**
        st.subheader("Distribusi Jenis Kelamin")
        jenis_kelamin_counts = df_filtered['JENIS KELAMIN'].value_counts(normalize=True).reset_index()
        jenis_kelamin_counts.columns = ['JENIS KELAMIN', 'Persentase']
        jenis_kelamin_counts['Persentase'] *= 100

        fig_jk = px.pie(
            jenis_kelamin_counts, 
            names='JENIS KELAMIN', 
            values='Persentase', 
            title='Persentase Jenis Kelamin',
            hover_data={'Persentase': ':.2f'}
        )
        fig_jk.update_traces(textinfo='label+percent')
        st.plotly_chart(fig_jk)

        # **2. Kelompok Usia**
        st.subheader("Distribusi Kelompok Usia")
        bins = [0, 12, 18, 35, 50, 65, 90]
        labels = ['Anak-anak (0-12)', 'Remaja (13-18)', 'Dewasa Muda (19-35)', 'Paruh Baya (36-50)', 'Lansia Awal (51-65)', 'Lansia (>65)']
        df_filtered['Kelompok Usia'] = pd.cut(df_filtered['USIA'], bins=bins, labels=labels, right=False)
        
        usia_counts = df_filtered['Kelompok Usia'].value_counts(normalize=True).reset_index()
        usia_counts.columns = ['Kelompok Usia', 'Persentase']
        usia_counts['Persentase'] *= 100
        
        fig_usia = px.bar(
            usia_counts, x='Kelompok Usia', y='Persentase', 
            text=usia_counts['Persentase'].apply(lambda x: f'{x:.2f}%'),
            labels={'Kelompok Usia': 'Kelompok Usia', 'Persentase': 'Persentase (%)'}, 
            title='Distribusi Kelompok Usia'
        )
        fig_usia.update_traces(textposition='outside')
        st.plotly_chart(fig_usia)

        # **3. Visualisasi Agama**
        st.subheader("Distribusi Agama")
        agama_counts = df_filtered['AGAMA'].value_counts(normalize=True).reset_index()
        agama_counts.columns = ['Agama', 'Persentase']
        agama_counts['Persentase'] *= 100

        fig_agama = px.bar(
            agama_counts, x='Agama', y='Persentase',
            text=agama_counts['Persentase'].apply(lambda x: f'{x:.2f}%'),
            labels={'Agama': 'Agama', 'Persentase': 'Persentase (%)'}, 
            title='Distribusi Agama'
        )
        fig_agama.update_traces(textposition='outside')
        st.plotly_chart(fig_agama)

        # **4. Visualisasi Pendidikan**
        st.subheader("Distribusi Pendidikan")
        pendidikan_counts = df_filtered['PENDIDIKAN'].value_counts(normalize=True).reset_index()
        pendidikan_counts.columns = ['Pendidikan', 'Persentase']
        pendidikan_counts['Persentase'] *= 100

        fig_pendidikan = px.bar(
            pendidikan_counts, x='Pendidikan', y='Persentase',
            text=pendidikan_counts['Persentase'].apply(lambda x: f'{x:.2f}%'),
            labels={'Pendidikan': 'Pendidikan', 'Persentase': 'Persentase (%)'}, 
            title='Distribusi Pendidikan'
        )
        fig_pendidikan.update_traces(textposition='outside')
        st.plotly_chart(fig_pendidikan)

        # **5. Visualisasi Pekerjaan**
        st.subheader("Distribusi Pekerjaan")
        pekerjaan_counts = df_filtered['PEKERJAAN'].value_counts(normalize=True).reset_index()
        pekerjaan_counts.columns = ['Pekerjaan', 'Persentase']
        pekerjaan_counts['Persentase'] *= 100

        fig_pekerjaan = px.bar(
            pekerjaan_counts, x='Pekerjaan', y='Persentase',
            text=pekerjaan_counts['Persentase'].apply(lambda x: f'{x:.2f}%'),
            labels={'Pekerjaan': 'Pekerjaan', 'Persentase': 'Persentase (%)'}, 
            title='Distribusi Pekerjaan'
        )
        fig_pekerjaan.update_traces(textposition='outside')
        st.plotly_chart(fig_pekerjaan)

    dashboard_page()

elif menu == "About Us":
    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-aWzcr_Onj6ZMetl-KwqR8P0xlqOHJ4R",
            "https://drive.google.com/uc?export=view&id=1nHszURphHgimIMw0G2EYOoOw6RSUqxN_",
            "https://drive.google.com/uc?export=view&id=1uC5cyvWEsy1nLhwArwZawd6cksOKdOL1",
            "https://drive.google.com/uc?export=view&id=1EVbVFxk4CElmqMH_ghv6LmgH5gz5viFk",
            "https://drive.google.com/uc?export=view&id=1PYmogsHVejCeJuwCPyieSK1guQWBQnnm",
            "https://drive.google.com/uc?export=view&id=1rvaS-20vDawiMEUBQi9Kdcsq_3kCocgh",
            "https://drive.google.com/uc?export=view&id=1BfJFDhZJNfgFYsYPUok3hoDvWKjlXkkg",
            "https://drive.google.com/uc?export=view&id=1iMP9OvoxUinkA1nVR40P_-o_LmMusI7T",
        ]
        data_list = [
            {
                "nama": "Anwar Muslim",
                "sebagai": "Ketua Kelompok",
                "nim": "122450117",
                "program_studi": "Sains Data",
                "motto_hidup": "Maknailah setiap pertemuan",
            },
            {
                "nama": "Andrew Diaz",
                "sebagai": "Humas",
                "nim": "121120154",
                "program_studi": "Teknik Geofisika",
                "motto_hidup": "Jika menginginkan sesuatu mulailah dari perubahan yang kecil",
            },
            {
                "nama": "Trifena Uly Octaviani Tambunan",
                "sebagai": "Sekretaris 1",
                "nim": "121470005",
                "program_studi": "Rekayasa Tata Kelola Air Terpadu",
                "motto_hidup": "Tetap bernafas",
            },
            {
                "nama": "Alfina Eriyandra",
                "sebagai": "Sekretaris 2",
                "nim": "122490022",
                "program_studi": "Rekayasa Instrumentasi dan Automasi",
                "motto_hidup": "Jangan takut gagal karena setiap kegagalan adalah langkah menuju keberhasilan yang lebih besar",
            },
            {
                "nama": "Eric Fratharias",
                "sebagai": "Operasional 1",
                "nim": "122170072",
                "program_studi": "Teknik Mesin",
                "motto_hidup": "Selesaikan apa yang sudah kamu mulai",
            },
            {
                "nama": "Daniel Manullang",
                "sebagai": "Operasional 2",
                "nim": "121460122",
                "program_studi": "Teknik Perkeretaapian",
                "motto_hidup": "Dalihan na tolu",
            },
            {
                "nama": "Khofifah Nur Islami",
                "sebagai": "Bendahara",
                "nim": "122990045",
                "program_studi": "Teknik Kimia",
                "motto_hidup": "Yang penting hidup",
            },
            {
                "nama": "Patricia Valentina",
                "sebagai": "Publikasi dan Dokumentasi",
                "nim": "122120166",
                "program_studi": "Teknik Geofisika",
                "motto_hidup": "Seberat apapun masalahmu jangan lupa berdoa",
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    about_page()