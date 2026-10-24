import random
def vakayi_baslat():
    vaka = {
        "ad": "dosya adi #002: kayip şifre",
        "aciklama": "bir şirketin gizli dosyalari calindi",
        "suclu": "yusuf",
        "ipucları": [
            "giriş saati 01.45 olarak tespit edildi",
            "sisteme yönetici hesabiyla girildi",
            "güvenlik kayitlari silinmeye çalişildi",
        ]

    }
    return vaka
supheliler = [
    {"isim": "yusuf","meslek":"yazilim gelistirici","ifade":"sabaha kadar oyun oynadım."},
    {"isim": "zeynep","meslek": "sistem yöneticisi","ifade": "akşam 18.00'de ciktim,sisteme girmedim."},
    {"isim": "melis","meslek":"veri analisti","ifade": "şifre kagidini masada unutmuş olabilirim."}
]
def suphelileri_goster(supheliler):
    print("ŞÜPHELİLER")
    sayi = 1
    for supheli in supheliler:
        print(f"{sayi}. {supheli['isim']} - {supheli['meslek']}")
        sayi = sayi + 1

def ipucu_ara(ipucları,bulunanlar):
    kalanlar = []
    for ipucu in ipucları:
        if ipucu not in bulunanlar:
            kalanlar.append(ipucu)
    if len(kalanlar) == 0:
        print("tüm ipuçlarını buldun!")
        return
    secilen = random.choice(kalanlar)
    bulunanlar.add(secilen)
    print(secilen)
vaka = vakayi_baslat()
bulunanlar = set()
ipucu_ara(vaka["ipucları"], bulunanlar)
ipucu_ara(vaka["ipucları"], bulunanlar)
ipucu_ara(vaka["ipucları"], bulunanlar)
ipucu_ara(vaka["ipucları"], bulunanlar)
def supheli_sorgula(supheliler):
    suphelileri_goster(supheliler)
    secim = input("sorgulamak istediğin şüphelinin numarası: ")
    if secim.isdigit():
        secim = int(secim)

        if secim == 1:
            print(supheliler[0]["ifade"])
        elif secim == 2:
            print(supheliler[1]["ifade"])
        elif secim == 3:
            print(supheliler[2]["ifade"])
        else:
            print("geçersiz seçim!")
    else:
        print("lütfen sayı gir!")
def sifre_coz(mesaj):
    cozulmus = mesaj[::-1]
    print("şifre çözüldü!")
    print(cozulmus)
    return cozulmus
def sucluyu_tahmin_et(suclu, hak):
    tahmin = input("sence suçlu kim?").lower()
    if tahmin == suclu:
        print("tebrikler! suçluyu buldun!  +60 puan")
        return True , hak, 60
    else:
        hak = hak - 1
        print("yanlış tahmin! -15 puan")
        print("kalan tahmin hakkın:", hak)
        return False, hak, -10
def oyun_raporu(puan,bulunanlar,kazandi):
    print("\n--- OYUN RAPORU ---")
    print("toplam puanın:" , puan)
    print("bulduğun ipuçları:")
    for ipucu in bulunanlar:
        print("-", ipucu)
    if kazandi:
        print("sonuç: vakayı çözdün!")
    else:
        print("sonuç: vaka çözülemedi!")
    print("oyun bitti!")
def oyun():
    vaka = vakayi_baslat()
    bulunanlar = set()
    puan = 0
    hak = 3
    kazandi = False

    while True:
        print("\n--- GİZEMLİ DOSYA ---")
        print("1. Şüphelileri göster")
        print("2. İpucu ara")
        print("3. Şüpheli sorgula")
        print("4. Şifre çöz")
        print("5. Suçluyu tahmin et")
        print("0. Oyundan çık")

        secim = input("Seçimin: ")

        if secim == "1":
            suphelileri_goster(supheliler)

        elif secim == "2":
            ipucu_ara(vaka["ipucları"], bulunanlar)

        elif secim == "3":
            supheli_sorgula(supheliler)

        elif secim == "4":
            sifre_coz("fusuY")

        elif secim == "5":
            sonuc, hak, degisim = sucluyu_tahmin_et(
                vaka["suclu"], hak
            )
            puan = puan + degisim

            if sonuc:
                kazandi = True
                oyun_raporu(puan, bulunanlar, kazandi)
                break

            elif hak == 0:
                oyun_raporu(puan, bulunanlar, kazandi)
                break

        elif secim == "0":
            oyun_raporu(puan, bulunanlar, kazandi)
            break

        else:
            print("Geçersiz seçim!")

oyun()



