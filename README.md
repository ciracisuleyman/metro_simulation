class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx  # İstasyonun benzersiz kimliği
        self.ad = ad    # İstasyonun adı
        self.hat = hat  # İstasyonun bulunduğu hat
        self.baglanti = []  # Bu istasyonla bağlantılı diğer istasyonlar

    def baglanti_ekle(self, istasyon):
        """Bu istasyon ile başka bir istasyon arasında bağlantı ekler."""
        if istasyon not in self.baglanti:
            self.baglanti.append(istasyon)

    def istasyon_bilgisi(self):
        print(f"İstasyon: {self.ad}, Hat: {self.hat}")


class MetroAgaci:
    def __init__(self):
        self.istasyonlar = {}  # İstasyonların listesi (idx -> Istasyon)

    def istasyon_ekle(self, idx: str, ad: str, hat: str):
        """Yeni bir istasyon ekler."""
        if idx not in self.istasyonlar:
            yeni_istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = yeni_istasyon

    def baglanti_ekle(self, idx1: str, idx2: str, mesafe: int):
        """İki istasyon arasına bağlantı ekler."""
        if idx1 in self.istasyonlar and idx2 in self.istasyonlar:
            istasyon1 = self.istasyonlar[idx1]
            istasyon2 = self.istasyonlar[idx2]
            istasyon1.baglanti_ekle(istasyon2)
            istasyon2.baglanti_ekle(istasyon1)
            print(f"{istasyon1.ad} ve {istasyon2.ad} arasında {mesafe} dakikalık mesafe eklendi.")
        else:
            print("Geçersiz istasyonlar!")

    def bfs(self, baslangic_idx: str, hedef_idx: str):
        """BFS algoritması ile bir istasyondan hedef istasyona ulaşma."""
        if baslangic_idx not in self.istasyonlar or hedef_idx not in self.istasyonlar:
            print("Geçersiz başlangıç veya hedef istasyonu!")
            return

        baslangic_istasyon = self.istasyonlar[baslangic_idx]
        hedef_istasyon = self.istasyonlar[hedef_idx]

        # BFS için gerekli yapılar
        ziyaret_edilen = set()  # Ziyaret edilen istasyonlar
        queue = [(baslangic_istasyon, [baslangic_istasyon.ad])]  # Kuyruk (istasyon, yol)

        while queue:
            istasyon, yol = queue.pop(0)  # Kuyruktan bir istasyon al

            if istasyon == hedef_istasyon:
                print("BFS ile hedefe ulaşıldı! Yol:", " -> ".join(yol))
                return

            if istasyon.idx not in ziyaret_edilen:
                ziyaret_edilen.add(istasyon.idx)
                for baglanti in istasyon.baglanti:
                    if baglanti.idx not in ziyaret_edilen:
                        queue.append((baglanti, yol + [baglanti.ad]))

        print("BFS ile hedefe ulaşılamadı.")

    def a_star(self, baslangic_idx: str, hedef_idx: str):
        """A* algoritması ile bir istasyondan hedef istasyona ulaşma."""
        if baslangic_idx not in self.istasyonlar or hedef_idx not in self.istasyonlar:
            print("Geçersiz başlangıç veya hedef istasyonu!")
            return

        # A* algoritmasının varsayılan heuristik fonksiyonu: Hedefe ulaşana kadar en kısa yolu bulmak.
        def heuristik(istasyon, hedef_istasyon):
            return abs(len(istasyon.baglanti) - len(hedef_istasyon.baglanti))

        baslangic_istasyon = self.istasyonlar[baslangic_idx]
        hedef_istasyon = self.istasyonlar[hedef_idx]

        # A* için gerekli yapılar
        open_list = [(baslangic_istasyon, 0, [baslangic_istasyon.ad])]  # (istasyon, maliyet, yol)
        closed_list = set()

        while open_list:
            open_list.sort(key=lambda x: x[1])  # Maliyeti en düşük olanı al
            istasyon, maliyet, yol = open_list.pop(0)

            if istasyon == hedef_istasyon:
                print("A* ile hedefe ulaşıldı! Yol:", " -> ".join(yol))
                return

            if istasyon.idx not in closed_list:
                closed_list.add(istasyon.idx)
                for baglanti in istasyon.baglanti:
                    if baglanti.idx not in closed_list:
                        open_list.append((baglanti, maliyet + 1 + heuristik(baglanti, hedef_istasyon), yol + [baglanti.ad]))

        print("A* ile hedefe ulaşılamadı.")


# Uygulama kısmı
metro_agaci = MetroAgaci()

# İstasyonlar ekleniyor
metro_agaci.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
metro_agaci.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
metro_agaci.istasyon_ekle("K3", "TCDD", "Mavi Hat")
metro_agaci.istasyon_ekle("K4", "Çıkrıkçılar", "Mavi Hat")

# Bağlantılar ekleniyor
metro_agaci.baglanti_ekle("K1", "K2", 2)  # Kızılay ile Ulus arasındaki bağlantı
metro_agaci.baglanti_ekle("K2", "K3", 3)  # Ulus ile TCDD arasındaki bağlantı
metro_agaci.baglanti_ekle("K3", "K4", 5)  # TCDD ile Çıkrıkçılar arasındaki bağlantı

# Algoritmalar çalıştırılıyor
metro_agaci.bfs("K1", "K4")  # Kızılay'dan Çıkrıkçılar'a BFS ile yol bulma
metro_agaci.a_star("K1", "K4")  # Kızılay'dan Çıkrıkçılar'a A* ile yol bulma
