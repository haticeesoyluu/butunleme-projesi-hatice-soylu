\# PROJE ÖNERİSİ



\### Seçilen Görev Numarası

\*\*SEÇENEK 1\*\* — RAG Tabanlı Uzman Bilgi Asistanı



\### Ürünün Adı

\*\*BaristaBot\*\*: Philips Lattego Tam Otomatik Kahve Makineleri İçin Akıllı Uzman Bilgi Asistanı



\### Çözülecek Problem

Tam otomatik kahve makinelerinin kullanım, periyodik bakım (kireç çözme, filtre değişimi) ve teknik arıza süreçleri karmaşık aşamalardan oluşmaktadır. Kullanıcılar, cihazın ekranında bir hata kodu veya uyarı ışığı gördüklerinde yüzlerce sayfalık fiziksel kılavuzlarda doğru bilgiye ulaşmakta zorlanmakta, vakit kaybetmekte veya hatalı müdahalede bulunarak cihazı garanti dışı bırakabilmektedir. Bu proje, kullanıcıların teknik dokümanlar arasında kaybolmadan, doğrudan doğal dil ile sorular sorarak resmi ve doğru yönlendirmelere anında ulaşmasını sağlamayı amaçlar.



\### Hedef Kullanıcı

\* Philips Lattego serisi tam otomatik kahve makinesi sahipleri.

\* Teknik kılavuzları okumakta zorlanan veya cihaz kurulumunu/bakımını hızlıca yapmak isteyen son kullanıcılar.

\* Cihazın temizlik ve kireç çözme gibi döngüsel süreçlerini adım adım takip etmek isteyen ev/ofis kullanıcıları.



\### Kullanılacak Veri veya Bilgi Kaynakları

Projede, doğruluğu kesin ve üretici tarafından onaylanmış en az 5 farklı resmi teknik doküman kaynak olarak kullanılacaktır:

1\. \*\*Philips Lattego Ana Kullanım Kılavuzu (PDF):\*\* Cihaz bileşenleri, ilk kurulum ve kahve çeşitlerinin hazırlanış yönergeleri.

2\. \*\*Temizlik ve Bakım Rehberi (PDF):\*\* Demleme grubu temizliği, süt sistemi (LatteGo) bakımı ve yağ temizleme tableti uygulama adımları.

3\. \*\*AquaClean Filtre Değişim Kılavuzu (PDF):\*\* Su filtresinin aktivasyonu, değiştirilmesi ve sertlik ayarlarının yapılması.

4\. \*\*Resmi Kireç Çözme (Descaling) Prosedürü (PDF):\*\* Cihazın kireç temizleme döngüsünün aşamalı teknik adımları.

5\. \*\*Hata Kodları ve Sıkça Sorulan Sorular (FAQ) Dokümanı:\*\* Dijital ekran uyarıları, ışıklı sinyallerin anlamları ve resmi sorun giderme çözümleri.



\### Kullanılması Planlanan Teknolojiler

\* \*\*Programlama Dili:\*\* Python

\* \*\*RAG Çatısı:\*\* LangChain (Doküman yükleme, metin parçalama ve zincir yapısı için)

\* \*\*Vektör Veritabanı:\*\* ChromaDB (Verilerin vektör temsillerini saklamak ve benzerlik araması yapmak için)

\* \*\*Metin Parçalama (Chunking):\*\* RecursiveCharacterTextSplitter (Anlamsal bütünlüğü korumak için)

\* \*\*Gömme (Embedding) ve LLM Modeli:\*\* OpenAI API (veya yerel kaynaklar için Ollama / Llama-3)

\* \*\*Kullanıcı Arayüzü:\*\* Streamlit (Temiz ve minimal bir web arayüzü sunmak için)



\### Beklenen Ürün Çıktısı

Kullanıcıların kahve makinesinin kullanımı, bakımı veya karşılaştıkları arızalar hakkında özgürce soru sorabildiği web tabanlı bir uygulama. Sistem, gelen sorulara yalnızca yüklenen 5 resmi dokümana sadık kalarak (hallucination/uydurma içermeden) cevap verecek ve ürettiği yanıtların altında \*\*tam olarak hangi dokümandan ve hangi bölümden beslendiğini (kaynak göstererek)\*\* listeleyecektir. Ayrıca bilgi kaynağında yer almayan alakasız sorulara karşı sistemi koruyan bir güvenlik mekanizması bulunacaktır.



\### Ürünün Diğer Çalışmalardan Ayrılan Yönü

Genel amaçlı yapay zeka modelleri (ChatGPT, Gemini vb.) teknik konularda halüsinasyon görmeye ve uydurma adımlar üretmeye eğilimlidir; bu durum hassas cihazlarda kalıcı hasarlara yol açabilir. BaristaBot, yalnızca üreticinin resmi dokümanlarını referans alarak bilgi güvenliğini %100'e çıkarır. Bilgi getirme sürecinde doküman kaynağının adını ve referans bölümünü kullanıcıya şeffaf bir şekilde sunarak akademik ve teknik doğrulanabilirlik sağlar.

