import sys

# ==========================================
# 1. ÖZEL HATA SINIFLARI
# ==========================================
class KitapZatenOduncVerildiError(Exception):
    """Bir kitap zaten başkasındaysa fırlatılacak özel hata."""
    pass

class KitapBulunamadiError(Exception):
    """Sistemde olmayan bir kitap arandığında fırlatılacak hata."""
    pass

class UyeBulunamadiError(Exception):
    """Sistemde olmayan bir üye işlem yapmaya çalıştığında fırlatılacak hata."""
    pass

# ==========================================
# 2. KİTAP VE TÜRLERİ (OOP)
# ==========================================
class Kitap:
    def __init__(self, isbn, baslik, yazar, yil):
        self.__isbn = str(isbn) 
        self.baslik = baslik
        self.yazar = yazar
        self.yil = str(yil)
        self.__odunc_alan = None 

    @property
    def isbn(self):
        return self.__isbn

    @property
    def durum(self):
        if self.__odunc_alan is None:
            return "Müsait"
        return f"Ödünç Verildi ({self.__odunc_alan.ad} {self.__odunc_alan.soyad})"

    def odunc_ver(self, uye_nesnesi):
        if self.__odunc_alan is not None:
            raise KitapZatenOduncVerildiError(f"HATA: '{self.baslik}' kitabı şu an müsait değil!")
        self.__odunc_alan = uye_nesnesi

    def iade_al(self):
        self.__odunc_alan = None

    def __str__(self):
        return f"📘 {self.baslik} - {self.yazar} ({self.yil}) [{self.durum}]"

class Roman(Kitap):
    def __init__(self, isbn, baslik, yazar, yil, tur):
        super().__init__(isbn, baslik, yazar, yil)
        self.tur = tur

class Dergi(Kitap):
    def __init__(self, isbn, baslik, yazar, yil, sayi):
        super().__init__(isbn, baslik, yazar, yil)
        self.sayi = sayi
    
    def __str__(self):
        return f"📑 [Dergi] {self.baslik} (Sayı: {self.sayi}) - {self.yazar} [{self.durum}]"

class CizgiRoman(Kitap):
    def __init__(self, isbn, baslik, yazar, yil, cizer):
        super().__init__(isbn, baslik, yazar, yil)
        self.cizer = cizer

# ==========================================
# 3. ÜYE SINIFI
# ==========================================
class Uye:
    def __init__(self, uye_no, ad, soyad, telefon):
        self.uye_no = uye_no
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon
        self.odunc_aldiklari = [] 

    def __str__(self):
        return f"👤 Üye {self.uye_no}: {self.ad} {self.soyad} ({self.telefon})"

# ==========================================
# 4. KÜTÜPHANE YÖNETİM MERKEZİ
# ==========================================
class Kutuphane:
    def __init__(self):
        self.kitaplar = []
        self.uyeler = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print(f"\n✅ BAŞARILI: '{kitap.baslik}' kütüphaneye eklendi.")

    def uye_ekle(self, uye):
        self.uyeler.append(uye)
        print(f"\n✅ BAŞARILI: {uye.ad} {uye.soyad} aramıza katıldı.")

    def kitap_bul(self, veri):
        for k in self.kitaplar:
            if veri == k.isbn or veri.lower() in k.baslik.lower():
                return k
        raise KitapBulunamadiError("Aradığınız kriterlere uygun kitap bulunamadı.")

    def uye_bul(self, u_no):
        for u in self.uyeler:
            if u.uye_no == u_no:
                return u
        raise UyeBulunamadiError("Bu numaraya sahip üye yok.")

    def kitap_ara(self, arama_metni):
        """İsmi veya ISBN'i aranan metni içeren kitapları listeler."""
        bulunanlar = []
        for kitap in self.kitaplar:
            if arama_metni in kitap.isbn or arama_metni.lower() in kitap.baslik.lower():
                bulunanlar.append(kitap)
        
        if not bulunanlar:
            print("\n❌ Sonuç bulunamadı.")
        else:
            print(f"\n🔎 --- Arama Sonuçları ({len(bulunanlar)}) ---")
            for k in bulunanlar:
                print(k)

    def odunc_ver_islemi(self, kitap_bilgi, uye_no):
        kitap = self.kitap_bul(kitap_bilgi)
        uye = self.uye_bul(uye_no)
        kitap.odunc_ver(uye)
        uye.odunc_aldiklari.append(kitap)
        print(f"\n✅ İŞLEM TAMAM: '{kitap.baslik}' kitabı {uye.ad}'a verildi.")

    def iade_al_islemi(self, kitap_bilgi):
        kitap = self.kitap_bul(kitap_bilgi)
        if kitap.durum == "Müsait":
            print("⚠️ UYARI: Bu kitap zaten rafta.")
            return

        odunc_alan_uye = None
        for uye in self.uyeler:
            if kitap in uye.odunc_aldiklari:
                odunc_alan_uye = uye
                break
        
        kitap.iade_al()
        if odunc_alan_uye:
            odunc_alan_uye.odunc_aldiklari.remove(kitap)
            print(f"\n✅ İADE ALINDI: '{kitap.baslik}' rafa kondu.")

    def tumunu_listele(self):
        print("\n📚 --- KÜTÜPHANE ENVANTERİ ---")
        if not self.kitaplar:
            print("Liste boş.")
        for k in self.kitaplar:
            print(k)

# ==========================================
# 5. ANA PROGRAM
# ==========================================
def main():
    kutuphane = Kutuphane()
    # Test verisi
    kutuphane.kitap_ekle(Roman("978123", "Sefiller", "Victor Hugo", "1862", "Klasik"))
    kutuphane.uye_ekle(Uye("101", "Ali", "Yılmaz", "0555-1234"))

    while True:
        print("\n" + "="*40)
        print("=== 🏛️  KÜTÜPHANE OTOMASYON SİSTEMİ v4 ===")
        print("1. Kitap Ekle")
        print("2. Üye Ekle")
        print("3. Kitap Ödünç Ver")
        print("4. Kitap İade Al")
        print("5. Kitap Ara")
        print("6. Tüm Kitapları Listele")
        print("7. Çıkış")
        print("="*40)
        
        secim = input("Seçiminiz: ")

        try:
            # --- SEÇENEK 1: KİTAP EKLE ---
            if secim == "1":
                print("\n--- Yeni Kitap Ekleme ---")
                tur = input("Tür Seçiniz (1: Roman, 2: Dergi, 3: Çizgi Roman): ")

                # ERKEN ÇIKIŞ
                if tur not in ["1", "2", "3"]:
                    print("\n⛔ HATA: Geçersiz kitap türü! İşlem iptal edildi.")
                    continue 

                # SAYI KONTROLÜ
                try:
                    isbn_input = input("ISBN (Sadece Rakam): ")
                    int(isbn_input) 
                    
                    yil_input = input("Basım Yılı: ")
                    int(yil_input) 
                except ValueError:
                    print("\n⛔ HATA: ISBN veya Yıl alanına HARF girdiniz! İşlem iptal.")
                    continue

                baslik = input("Kitap Adı: ")
                yazar = input("Yazar: ")

                if tur == "1":
                    r_tur = input("Roman Türü: ")
                    yeni_kitap = Roman(isbn_input, baslik, yazar, yil_input, r_tur)
                elif tur == "2":
                    sayi = input("Dergi Sayısı: ")
                    yeni_kitap = Dergi(isbn_input, baslik, yazar, yil_input, sayi)
                elif tur == "3":
                    cizer = input("Çizer: ")
                    yeni_kitap = CizgiRoman(isbn_input, baslik, yazar, yil_input, cizer)
                
                kutuphane.kitap_ekle(yeni_kitap)

            # --- SEÇENEK 2: ÜYE EKLE ---
            elif secim == "2":
                print("\n--- Yeni Üye Kaydı ---")
                
                # 1. ÜYE NO KONTROLÜ
                u_no = input("Üye No (Sadece Rakam): ")
                if not u_no.isdigit():
                    raise ValueError("Üye numarası sadece rakamlardan oluşmalıdır!")

                # 2. İSİM KONTROLÜ
                ad = input("Ad: ")
                if not ad.replace(" ", "").isalpha():
                    raise ValueError("İsim alanına sayı veya sembol giremezsiniz!")

                # 3. SOYİSİM KONTROLÜ
                soyad = input("Soyad: ")
                if not soyad.isalpha():
                    raise ValueError("Soyad alanına sayı veya sembol giremezsiniz!")

                # 4. TELEFON KONTROLÜ (YENİ EKLENDİ)
                tel = input("Telefon (Örn: 0555 123 4567): ")
                # Tire ve boşlukları silip kalana bakıyoruz.
                temiz_tel = tel.replace(" ", "").replace("-", "")
                
                if not temiz_tel.isdigit():
                    raise ValueError("Telefon numarası HARF içeremez!")
                
                if len(temiz_tel) < 10:
                    raise ValueError("Telefon numarası çok kısa! (En az 10 hane olmalı)")

                kutuphane.uye_ekle(Uye(u_no, ad, soyad, tel))

            # --- DİĞER SEÇENEKLER ---
            elif secim == "3":
                bilgi = input("Hangi Kitap (ISBN veya Ad): ")
                u_no = input("Hangi Üye (No): ")
                kutuphane.odunc_ver_islemi(bilgi, u_no)

            elif secim == "4":
                bilgi = input("İade Edilecek Kitap (ISBN veya Ad): ")
                kutuphane.iade_al_islemi(bilgi)

            elif secim == "5":
                aranan = input("Aranacak kelime veya ISBN: ")
                kutuphane.kitap_ara(aranan)

            elif secim == "6":
                kutuphane.tumunu_listele()

            elif secim == "7":
                print("Sistemden çıkılıyor... İyi günler!")
                break
            
            else:
                print("Lütfen 1-7 arası geçerli bir seçim yapın.")

        # --- HATA YÖNETİMİ ---
        except ValueError as e:
            print(f"\n⛔ GİRİŞ HATASI: {e}")
            print("--- İşlem İptal Edildi, Ana Menüye Dönülüyor ---")
        except KitapZatenOduncVerildiError as e:
            print(f"\n🚫 İŞLEM BAŞARISIZ: {e}")
        except KitapBulunamadiError as e:
            print(f"\n🔍 BULUNAMADI: {e}")
        except UyeBulunamadiError as e:
            print(f"\n🔍 BULUNAMADI: {e}")
        except Exception as e:
            print(f"\n⚠️ BEKLENMEDİK HATA: {e}")

if __name__ == "__main__":
    main()