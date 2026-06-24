# ☕ BaristaBot: Philips Lattego Uzman Bilgi Asistanı
👉 [ÇALIŞAN_ÜRÜNÜN VİDEOSU'nu YouTube Üzerinden İzlemek İçin Tıklayın](https://youtu.be/TlQCE77Qipw)


Bu proje, **Manisa Celal Bayar Üniversitesi Veri Bilimi ve Analitiği Bölümü** bütünleme değerlendirmesi kapsamında geliştirilmiş, **Philips Lattego** kahve makinelerine yönelik RAG (Retrieval-Augmented Generation) tabanlı bir uzman bilgi asistanıdır.

---

## 📄 1. Problem Tanımı
Tam otomatik kahve makinelerinin kullanım, periyodik bakım (kireç çözme, filtre değişimi) ve teknik arıza süreçleri karmaşık aşamalardan oluşmaktadır. Kullanıcılar, cihazın ekranında bir hata kodu veya uyarı ışığı gördüklerinde yüzlerce sayfalık fiziksel kılavuzlarda doğru bilgiye ulaşmakta zorlanmakta, vakit kaybetmekte veya hatalı müdahalede bulunabilmektedir.

## 🎯 2. Hedef Kullanıcı
* Evinde veya ofisinde Philips Lattego tam otomatik kahve makinesi kullanan tüketiciler.
* Cihazların bakım ve arıza süreçlerini teknik servis çağırmadan, kılavuza uygun şekilde çözmek isteyen kullanıcılar.

## 💡 3. Çözüm Özeti & Ürünün Yaptığı İş
BaristaBot, cihaza ait resmi teknik dokümanları ve kılavuzları anlamsal parçalara bölerek saklar. Kullanıcı doğal dille bir soru sorduğunda (Örn: "E01 hatası nedir?"), sistem ilgili bilgi parçasını bulup manipüle edilmemiş, doğrudan resmi kaynağa dayalı nokta atışı bir çözüm adımı üretir.

## 🛠️ 4. Kullanılan Teknolojiler
* **Python 3.14+** (Ana programlama dili)
* **Streamlit** (Kullanıcı arayüzü ve web entegrasyonu)
* **OS & Re (Regex):** Veritabanı ayrıştırma, dosya yönetimi ve metin eşleştirme süreçleri.

## 🏗️ 5. Sistem Mimarisi ve İş Akışı
1. **Veri Girişi:** Resmi kılavuz verileri `kaynaklar.txt` içerisinde `=== Bölüm Başlığı ===` formatında yapılandırılmıştır.
2. **Bilgi Geri Çağırma (Retrieval):** Kullanıcı sorgusu alındığında, kelime bazlı ve akıllı filtreleme mekanizması çalışarak veritabanındaki en alakalı başlığı yakalar.
3. **Güvenlik & Kapsam Kontrolü:** Sorgu kahve makinesi dışındaysa, sistem halüsinasyon görmeyi engelleyerek kullanıcıya uyarı verir.
4. **Arayüz Sunumu:** Sonuçlar Streamlit arayüzünde kullanıcıya referans kaynağıyla birlikte gösterilir.

## 📦 6. Kurulum ve Çalıştırma Adımları
Projenin yerel sunucuda çalıştırılması için terminale sırasıyla aşağıdaki komutlar yazılır :
```bash
pip install streamlit
python -m streamlit run app.py




