from PIL import Image


def convert_to_bw(input_path, output_path):
    # Resmi önce  gri tona çeviriyoruz
    img = Image.open(input_path).convert('L')

    # Gri değeri 128'den büyükse beyaz, değilse siyah yap çünkü siyahın değeri 0 beyazın değeri 255 dir
    bw = img.point(lambda x: 0 if x < 128 else 255, '1')

    # Yeni resmi kaydet
    bw.save(output_path)
    print(f"Siyah-beyaz resim kaydedildi: {output_path}")


# 📌 Dosya yolları'nı yazarak input olarak kullanacağımız resmi buluyoruz
input_file = 'C:/phycherm/off.jpg'
output_file = 'C:/phycherm/off renksiz.png'
convert_to_bw(input_file, output_file)


