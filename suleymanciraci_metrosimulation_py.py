# -*- coding: utf-8 -*-
"""SuleymanCiraci_MetroSimulation.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10H7dtnRZuK8b8O4hb1B-D9wn75XqjSFb
"""

from collections import defaultdict, deque
import heapq
from typing import Dict, List, Optional, Tuple

# 🚇 İstasyon sınıfı: Her istasyonun adı, hattı ve komşuları tutulur
class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []

    # Komşu eklemek için metod
    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

# 🚇 Metro ağı sınıfı: Tüm istasyonları ve hatları saklar
class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    # İstasyon ekle
    def istasyon_ekle(self, idx: str, ad: str, hat: str):
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    # İki istasyon arasında bağlantı (hat ekleme)
    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int):
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    # 🚇 BFS algoritması ile en az aktarmalı rota bulma
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        kuyruk = deque([(baslangic, [baslangic])])
        ziyaret_edilen = set()
        ziyaret_edilen.add(baslangic)

        while kuyruk:
            mevcut_istasyon, yol = kuyruk.popleft()
            if mevcut_istasyon == hedef:
                return yol

            for komsu, _ in mevcut_istasyon.komsular:
                if komsu not in ziyaret_edilen:
                    ziyaret_edilen.add(komsu)
                    kuyruk.append((komsu, yol + [komsu]))

        return None

# ⭐ A* algoritması için basit heuristic fonksiyonu
def heuristic(istasyon, hedef):
    ortalama_sure = 5
    istasyon_id = int(''.join(filter(str.isdigit, istasyon.idx)))
    hedef_id = int(''.join(filter(str.isdigit, hedef.idx)))
    return abs(hedef_id - istasyon_id) * ortalama_sure

# ⭐ A* algoritması ile en kısa süreli rota bulma
def en_hizli_rota_bul(metro_agi: MetroAgi, baslangic_id: str, hedef_id: str):
    baslangic = metro_agi.istasyonlar[baslangic_id]
    hedef = metro_agi.istasyonlar[hedef_id]

    acik_liste = [(0 + heuristic(baslangic, hedef), 0, baslangic, [])]
    ziyaret_edilen = set()

    while acik_liste:
        _, gecen_sure, mevcut, yol = heapq.heappop(acik_liste)

        if mevcut in ziyaret_edilen:
            continue
        yol = yol + [mevcut]

        if mevcut == hedef:
            return yol, gecen_sure

        ziyaret_edilen.add(mevcut)

        for komsu, sure in mevcut.komsular:
            if komsu not in ziyaret_edilen:
                tahmini_toplam = gecen_sure + sure + heuristic(komsu, hedef)
                heapq.heappush(acik_liste, (tahmini_toplam, gecen_sure + sure, komsu, yol))

    return None, None

# Örnek metro ağı oluşturma
metro = MetroAgi()
metro.istasyon_ekle("K1", "Kızılay", "Aktarma Noktası")
metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")

# İstasyonlar arası bağlantılar
metro.baglanti_ekle("K1", "K2", 4)
metro.baglanti_ekle("K2", "K3", 6)
metro.baglanti_ekle("M1", "K1", 5)
metro.baglanti_ekle("T1", "T2", 7)
metro.baglanti_ekle("K3", "T2", 3)

# BFS ile test (En az aktarmalı rota)
print("\n🚇 BFS (En az aktarmalı rota):")
bfs_rota = metro.en_az_aktarma_bul("M1", "K3")
if bfs_rota:
    print(" -> ".join(i.ad for i in bfs_rota))
else:
    print("Rota bulunamadı.")

# A* ile test (En hızlı rota)
print("\n🚇 A* (En kısa süreli rota):")
astar_rota, toplam_sure = en_hizli_rota_bul(metro, "M1", "K3")
if astar_rota:
    print(" -> ".join(i.ad for i in astar_rota))
    print(f"Toplam süre: {toplam_sure} dakika")
else:
    print("Rota bulunamadı.")

