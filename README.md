# Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu)

Bu proje, bir şehirdeki metro ağında iki farklı algoritma kullanarak, kullanıcıların en az aktarmalı ve en hızlı rotaları bulmalarını sağlar. Kullanıcılar, başlangıç ve hedef istasyonları arasında en uygun rotayı seçebilirler.

## Kullanılan Teknolojiler ve Kütüphaneler

- **heapq**: A* algoritmasında öncelikli kuyruk (priority queue) kullanmak için, her adımda en düşük maliyeti olan istasyonu seçmek amacıyla bu kütüphane kullanılmıştır.
- **collections**: Bu kütüphane, özellikle `defaultdict` ve `deque` veri yapılarını kullanarak, istasyonlar arasındaki bağlantıları yönetmek ve BFS için kuyruk oluşturmak için kullanılmıştır.
- **typing**: Python'un tip açıklama (type hinting) sistemini kullanarak fonksiyon parametrelerinin ve dönüş türlerinin daha net ve anlaşılır olmasını sağlamak için kullanılmıştır.

## Algoritmaların Çalışma Mantığı

### BFS (Breadth-First Search) Algoritması

BFS algoritması, her adımda bir seviyedeki tüm komşuları ziyaret ederek, en kısa yolu bulmaya çalışan bir algoritmadır.

- **Başlangıç**: Başlangıç istasyonundan başlar ve komşu istasyonlarını sırayla ziyaret eder.
- **Kuyruk Yapısı**: İlk başta sadece başlangıç istasyonu kuyruğa eklenir.
- **Ziyaret Edilen İstasyonlar**: Her istasyon ziyaret edildiğinde, komşu istasyonları ziyaret edilmek üzere kuyruğa eklenir.

BFS tüm olasılıkları denemez, en verimli yoldan gitmediğini anladığı gibi o yolu kuyruk dediğimiz kısımdan siler.
Burada en az aktarmayı bulmaya çalışıyor, dolayısıyla algoritma başlangıç noktasından ilk başta komşularını ziyaret eder ve en az aktarma bulma olasılığı devam ettiği sürece ziyaret ettiği istasyon ve o istasyona gelinceye kadar geçtiği istasyonların listesi deque ile oluşturulan kuyruk kısmında değiştirilemeyen yapı olan tupple içinde tutulur. BFS bu denemeleri yaparken daha önce uğradığı istasyona geri dönmez. Bu şekilde sonunda en az aktarma ile ulaşılan hedef ve bu esnada geçilen istasyonların bilgisi kuyruk kısmında kalır.

### A* (A Star) Algoritması

A* algoritması, hem **gerçek mesafe** hem de **hedefe olan tahmini mesafe** (heuristic) bilgilerini kullanarak, en hızlı rotayı bulmaya çalışır.

- **Başlangıç ve Hedef İstasyonu**: Başlangıç istasyonundan hedef istasyona olan rotayı bulmaya çalışır.
- **Öncelikli Kuyruk**: Öncelikli kuyruk kullanılır ve her istasyonun maliyeti hesaplanarak sıradaki istasyonlar belirlenir.

