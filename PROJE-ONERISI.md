### Seçilen Görev Numarası
**SEÇENEK 1** — RAG Tabanlı Uzman Bilgi Asistanı

### Ürünün Adı
**BaristaBot**: Philips Lattego Tam Otomatik Kahve Makineleri İçin Akıllı Uzman Bilgi Asistanı

### Çözülecek Problem
Tam otomatik kahve makinelerinin kullanım, periyodik bakım (kireç çözme, filtre değişimi) ve teknik arıza süreçleri karmaşık aşamalardan oluşmaktadır. Kullanıcılar, cihazın ekranında bir hata kodu veya uyarı ışığı gördüklerinde yüzlerce sayfalık fiziksel kılavuzlarda doğru bilgiye ulaşmakta zorlanmakta, vakit kaybetmekte veya hatalı müdahalelerde bulunabilmektedir.

### Hedef Kullanıcı
Evinde veya ofisinde Philips Lattego tam otomatik kahve makinesi kullanan ve teknik servis çağırmadan sorunları resmi kılavuz adımlarıyla hızlıca çözmek isteyen tüketiciler.

### Kullanılacak Veri veya Bilgi Kaynakları
Philips Lattego resmi kullanım kılavuzları, temizlik/bakım dökümanları ve hata kodları listesini içeren `kaynaklar.txt` metin dökümanı.

### Kullanılması Planlanan Teknolojiler
* Python (Ana Programlama Dili)
* Streamlit (Responsive Web Arayüzü)
* OS & Re Modülleri (Metin ayrıştırma ve akıllı regex filtreleme)

### Beklenen Ürün Çıktısı
Kullanıcının doğal dille yazdığı arıza veya bakım sorgularını anlamsal olarak analiz eden, veritabanından nokta atışı doğru çözümü bulan ve manipüle edilmemiş resmi yönergeleri Streamlit arayüzü üzerinden kullanıcıya sunan RAG tabanlı bir uzman web asistanı.

### Ürünün Diğer Çalışmalardan Ayrılan Yönü
Geleneksel anahtar kelime aramalarının ötesine geçerek kireç çözme veya kritik hata kodları (E01 gibi) için özel önceliklendirme filtreleri içermesi, Streamlit önbellek kilitlenmelerini önleyen dinamik dosya okuma mimarisi ve kapsam dışı alakasız soruları engelleyen güçlü bir halüsinasyon bariyerine sahip olmasıdır.
