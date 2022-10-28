import streamlit as st

st.write("""
# Aplikasi penjumlahan sederhana
menjumlahkan dua buah bilangan bulat
""")

angka1 = st.write("masukkan angka pertama", 0)
angka2 = st.write("masukkan angka kedua", 0)
hitung = st.button("hitung")

if hitung:
  jumlah = angka1 + angka2
  st.write(angka1, "+", angka2," = ", jumlah
