import streamlit as st

st.write("""
# aplikasi menghitung luas sederhana 
""")

alas = st.write("masukkan alas = ", 0)
tinggi = st.write("masukkan tinggi = ", 0)
panjang = st.write("masukkan panjang = ", 0)
hitung = st.button("luas")

if hitung:
  luas = panjang * alas * tinggi
  st.write("luas = ", luas)
