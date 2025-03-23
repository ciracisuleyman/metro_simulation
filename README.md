# README.md dosyasını oluşturuyoruz
readme_icerik = """
# 🚇 Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu)

## 📌 Proje Hakkında
Bu proje, Global AI Hub & Akbank Python ile Yapay Zekaya Giriş Bootcamp kapsamında geliştirilmiştir.  
Proje kapsamında:
- Bir metro ağı modellemesi yapılmıştır.
- BFS algoritması ile iki istasyon arasındaki en az aktarmalı rota bulunur.
- A* algoritması ile en hızlı (en kısa süreli) rota bulunur.

---

## 🛠 Kullanılan Teknolojiler ve Kütüphaneler
- **Python 3.10+**
- `collections`  
   - **deque**: BFS için kuyruk veri yapısı olarak kullanıldı.  
   - **defaultdict**: Hata almadan otomatik olarak liste üreten dictionary oluşturmak için kullanıldı.  
- `heapq`  
   - A* algoritmasında öncelik kuyruğu veri yapısını oluşturmak için kullanıldı.  
- `typing`  
   - Kod okunabilirliği ve tip kontrolü için `List`, `Dict`, `Optional`, `Tuple` tipleri kullanıldı.  

---

## 📖 Algoritmaların Çalışma Mantığı

### 🔎 BFS (Breadth-First Search) - En Az Aktarmalı Rota
- Kuyruk (deque) veri yapısı kullanılır.
- Başlangıç istasyonundan başlanarak katman katman tüm komşular taranır.
- En kısa yol (en az istasyon değiştirmeli) bulunur.
- Ziyaret edilen düğümler takip edilir ve daha önce ziyaret edilen istasyonlar tekrar kuyruğa alınmaz.

**Neden BFS?**  
> BFS, graf üzerinde en kısa kenar sayısına sahip rotayı bulmada idealdir. Bu da, en az aktarmalı yol demektir.

---

### 🧭 A* Algoritması - En Hızlı Rota
- Priorite (öncelik) kuyruğu (heapq) kullanılır.
- Her istasyon için `geçen_süre + tahmini kalan süre (heuristic)` değeri hesaplanır.
- En düşük toplam maliyete sahip düğüm seçilerek hedefe ulaşılır.
- `heuristic` fonksiyonu, istasyon ID farkını ve sabit ortalama geçiş süresini kullanarak tahmin yapar.

**Neden A*?**  
> A* algoritması, graf üzerinde en kısa maliyetli (en kısa süreli) yol bulmak için en etkili arama yöntemlerinden biridir.  

---

## 🚦 Örnek Kullanım

```bash
python AdSoyad_MetroSimulation.py
