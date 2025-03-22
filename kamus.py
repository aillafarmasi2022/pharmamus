import streamlit as st
import pandas as pd

# Load data kamus dari CSV
df = pd.read_csv("data/kamus.csv")

# Tampilan judul aplikasi
st.title("📖 Kamus Istilah Farmasi")

# Input pencarian istilah
istilah = st.text_input("Masukkan istilah farmasi").strip().lower()

# Tombol pencarian
if st.button("Cari"):
    # Mencari istilah dalam data
    terjemahan = df[df["Istilah"].str.lower() == istilah]["Terjemahan"].values
    if len(terjemahan) > 0:
        st.success(f"**{istilah.capitalize()}**: {terjemahan[0]}")
    else:
        st.error("Istilah tidak ditemukan.")

# Menampilkan seluruh daftar istilah farmasi (opsional)
st.write("### 📌 Daftar Istilah Farmasi")
st.dataframe(df)
