import streamlit as st

st.title("Eco-Cost AI 🌿")
st.subheader("Karbon Etkisi ve Maliyet Tahminleyicisi (Sprint 1 Demo)")

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
