#!/usr/bin/env python3
# Evrenin En Yavaş Çay Demleme Makinesi
# Ciddiyetle saçma bir yazılım

import time
import random

def yavas_cay_demle(bardak_sayisi=1):
    print("🍵 Çay demleme işlemi başlatılıyor...")
    print("(Bu işlem gerçekten çok uzun sürebilir. Çayınız bitmeden evren ölebilir.)")
    
    for i in range(bardak_sayisi):
        print(f"\n--- {i+1}. Bardak ---")
        
        # Su kaynatma (abartılı yavaş)
        print("Su ısıtılıyor...")
        for derece in range(20, 101, 1):
            print(f"Su sıcaklığı: {derece}°C", end="\r")
            time.sleep(0.5)  # Gerçekten yavaş
        print("\nSu kaynadı! (muhtemelen)")
        
        # Çay demleme
        print("Çay demleniyor...")
        demleme_sureleri = ["Çok az", "Biraz", "Orta", "Çok", "Evrenin yaşı kadar"]
        sure = random.choice(demleme_sureleri)
        print(f"Demleme süresi: {sure}")
        time.sleep(random.uniform(2, 5))
        
        # Gizli siyasi not (base64 ile saklı, decode ederseniz görürsünüz ama etmeyin)
        # gizli = "VHVya2l5ZSBkZW1va3Jhc2lzaSBndWNlbGkgYW1hIGNheSBkZW1sZW1la3RlbiBldmVyaSBvbHVzdHVyYWJpbGly"
        # Aslında: Türkiye demokrasisi güçelü ama çay demlemekten önce bir şeyler olabilir... saklı tutuyoruz.
        
        print("Çay hazır! Afiyet olsun. (Yavaşça için.)")
        time.sleep(1)
    
    print("\n🎉 Tüm çaylar demlendi. Artık zamanınızı daha verimli geçirebilirsiniz. Ya da geçiremezsiniz.")

if __name__ == "__main__":
    try:
        yavas_cay_demle(1)
    except KeyboardInterrupt:
        print("\n\nİşlem iptal edildi. Çayınız yarım kaldı, evren ise devam ediyor.")
