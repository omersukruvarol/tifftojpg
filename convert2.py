
import os
import cv2

# Giriş ve çıktı klasörlerini tanımlayın
input_dir = "C:\\Users\\OmerVarul\\Desktop\\tifftojepg\\tiff"
output_dir = "C:\\Users\\OmerVarul\\Desktop\\tifftojepg\\jpeg"

# Giriş klasöründeki tüm dosyaları listeleyin
files = os.listdir(input_dir)

# Her dosyayı jpeg'e dönüştürün
for file in files:
    # Dosyanın tif olup olmadığını kontrol edin
    if file.endswith(".tif"):
        # Dosyayı okutur
        image = cv2.imread(os.path.join(input_dir, file))

        # Dosyanın ismini alın
        new_name = file.replace(".tif", ".jpg")

        # Dosyayı jpeg'e dönüştürün ve çıktı klasörüne kaydedin
        cv2.imwrite(os.path.join(output_dir, new_name), image)

print("Tüm dosyalar dönüştürüldü!")
