# 🖤 Siyah-Beyaz Resim Dönüştürücü

Bu proje, bir görüntüyü otomatik olarak **siyah-beyaz** hale getiren basit ama etkili bir Python betiğidir.  
Kod, gri tonlamaya çevrilmiş bir resmi 128 eşik değeri kullanarak tamamen siyah ve beyaz piksellere dönüştürür.

---

## 📷 Örnek:  
**Girdi:** `kou.png`  
**Çıktı:** `kou renksiz.png` _(sadece siyah ve beyaz piksellerle)_

---

## 🛠️ Kullanılan Teknolojiler

- **Python 3**
- **Pillow** (PIL - Python Imaging Library)

---

## 🚀 Nasıl Kullanılır?

### 1. Pillow Kütüphanesini Kur

Terminal veya komut satırından aşağıdaki komutu gir:

```bash
pip install Pillow
```
from PIL import Image
```python
def convert_to_bw(input_path, output_path):
    # Resmi gri tona çeviriyoruz
    img = Image.open(input_path).convert('L')

    # Gri değeri 128'den büyükse beyaz, değilse siyah yap
    bw = img.point(lambda x: 0 if x < 128 else 255, '1')

    # Yeni resmi kaydet
    bw.save(output_path)
    print(f"Siyah-beyaz resim başarıyla kaydedildi: {output_path}")


# 📌 Dosya yolları (mutlaka çift \\ veya / kullan!)
input_file = 'C:/phycherm/kou.png'
output_file = 'C:/phycherm/kou renksiz.png'

# Fonksiyonu çalıştır
convert_to_bw(input_file, output_file)
```
