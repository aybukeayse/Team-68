import streamlit as st
import pandas as pd

st.title("Eco-Cost AI 🌿")
st.subheader("Karbon Etkisi ve Maliyet Tahminleyicisi (Sprint 2)")

# SPRINT 2: Veri Seti Entegrasyonu (Yan Menü) 
st.sidebar.header("Veri Entegrasyonu")
st.sidebar.markdown("Sprint 2: Temsili veri seti (`veri_seti.csv`) sisteme entegre edildi.")

try:
    df = pd.read_csv("veri_seti.csv")
    st.sidebar.success("Veri seti başarıyla okundu!")
    if st.sidebar.checkbox("Test Veri Setini Göster"):
        st.sidebar.dataframe(df)
except FileNotFoundError:
    st.sidebar.warning("veri_seti.csv henüz yüklenmedi.")


# SPRINT 1: Mevcut Hesaplama Altyapısı 
st.write("Lütfen aylık üretim verilerinizi girin:")
elektrik = st.number_input("Aylık Elektrik Tüketimi (kWh)", min_value=0)
dogalgaz = st.number_input("Aylık Doğalgaz Tüketimi (m3)", min_value=0)

if st.button("Karbon Emisyonunu Hesapla"):
    # MVP için basit ve sembolik bir emisyon hesaplaması
    emisyon = (elektrik * 0.43) + (dogalgaz * 2.0)
    
    st.success(f"Tahmini Karbon Ayak İziniz: {emisyon:.2f} kg CO2")
    
    if emisyon > 1000:
        st.warning("Uyarı: Emisyon değeriniz yüksek. İlerleyen sprintlerde karbon vergisi maliyeti de bu panele eklenecektir.")
    else:
        st.info("Harika! Üretim kaynaklı emisyon değeriniz güvenli sınırlar içerisinde.")
