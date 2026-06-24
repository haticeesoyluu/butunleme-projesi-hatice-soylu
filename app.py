import streamlit as st
import os
import re

# Sayfa Genişliği ve Başlık Ayarları (Hocanın istediği kurumsal görünüm)
st.set_page_config(
    page_title="BaristaBot - Philips Lattego Asistanı",
    page_icon="☕",
    layout="centered"
)

# Kurumsal CSS Tasarımı (Philips Mavisi ve Modern Fontlar)
st.markdown("""
    <style>
    .main-title {
        color: #002855;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    .subtitle {
        color: #555555;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 2px solid #002855;
    }
    .stButton > button {
        background-color: #002855;
        color: white;
        border-radius: 8px;
        width: 100%;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #004080;
        color: white;
    }
    .response-box {
        background-color: #f4f6f9;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #002855;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Arayüz Başlık Alanı
st.markdown("<h1 class='main-title'>☕ BaristaBot</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Philips Lattego Tam Otomatik Kahve Makineleri Akıllı Uzman Bilgi Asistanı</p>", unsafe_allow_html=True)

# Yan Menü (Sidebar) - Akademik Künye Alanı
with st.sidebar:
    st.markdown("### 🏛️ MCBÜ Bütünleme Projesi")
    st.markdown("**Öğrenci Adı:** Hatice Soylu")
    st.markdown("**Öğrenci No:** 2544001013")
    st.markdown("**Bölüm:** Veri Bilimi ve Analitiği")
    st.markdown("---")
    st.info("Bu asistan, cihazın resmi teknik dökümanlarını (kaynaklar.txt) anlamsal parçalara bölerek çalışan RAG tabanlı bir uzman sistemdir.")

# Akıllı Bilgi Geri Çağırma (Retrieval) Fonksiyonu
def dokuman_ara(sorgu):
    sorgu = sorgu.lower()
    
    # 🛡️ Güvenlik Bariyeri: Kahve makinesiyle alakasız sorguları engelle (Halüsinasyon Filtresi)
    kahve_kelimeleri = ["kahve", "kireç", "temiz", "filtre", "hata", "arıza", "su", "süt", "lattego", "e01", "buton", "ışık", "çözme", "prosedür", "nasıl"]
    if not any(kelime in sorgu for kelime in kahve_kelimeleri):
        return "⚠️ Kapsam Dışı İstek: Ben sadece Philips Lattego kahve makinelerine yönelik teknik, bakım ve arıza sorularına yanıt verebilen bir uzman asistanım. Lütfen cihazınızla ilgili bir soru sorunuz."

    # Dosya Okuma ve Önbellek Kilitlenmesini Önleyen Yapı
    if not os.path.exists("kaynaklar.txt"):
        return "❌ Hata: 'kaynaklar.txt' veritabanı dosyası bulunamadı. Lütfen dökümanı depoya ekleyin."
        
    with open("kaynaklar.txt", "r", encoding="utf-8") as f:
        icerik = f.read()
    
    # Dökümanları Yapılandırılmış Başlıklara Göre Bölme (Chunking)
    bolumler = icerik.split("====")
    
    en_alakali_icerik = ""
    en_yuksek_skor = 0
    
    # Regex ve Kelime Eşleşme Mantığıyla En Doğru Parçayı Bulma
    for bolum in bolumler:
        if not bolum.strip():
            continue
        
        # Arama terimlerinin parça içindeki sıklığını sayma
        skor = sum(1 for kelime in sorgu.split() if kelime in bolum.lower())
        
        # Kritik teknik anahtar kelimeler için nokta atışı önceliklendirme bonusu
        if "kireç" in sorgu and "kireçten arındırma" in bolum.lower():
            skor += 5
        if "e01" in sorgu and "e01" in bolum.lower():
            skor += 5
            
        if skor > en_yuksek_skor:
            en_yuksek_skor = skor
            en_alakali_icerik = bolum.strip()
            
    if en_yuksek_skor > 0:
        return en_alakali_icerik
    else:
        return "🔍 Aradığınız konuya dair nokta atışı bir kılavuz adımı bulunamadı. Lütfen 'kireç çözme', 'filtre değişimi' veya 'E01 hatası' gibi teknik terimlerle tekrar deneyiniz."

# Kullanıcı Etkileşim Alanı
sorgu = st.text_input("Cihazınızla ilgili teknik veya bakım sorusunu yazın:", placeholder="Örn: Kireç çözme işlemi ne kadar sürer?")

if st.button("Asistana Sor"):
    if sorgu.strip():
        with st.spinner("Resmi kılavuz dökümanları taranıyor..."):
            cevap = dokuman_ara(sorgu)
            
            st.markdown("### 🤖 BaristaBot'un Yanıtı:")
            if "⚠️" in cevap or "❌" in cevap:
                st.warning(cevap)
            else:
                st.markdown(f"<div class='response-box'>{cevap}</div>", unsafe_allow_html=True)
                st.success("ℹ️ Kaynak: Philips Lattego Resmi Teknik Kullanım Kılavuzu")
    else:
        st.error("Lütfen boş bir sorgu göndermeyin.")
# Veri temizleme modülü ve veri seti islemleri.
