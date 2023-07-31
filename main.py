from PIL import Image as img

resimler_listesi = ['mouse-1.jpg','mouse-2.jpg','mouse-3.jpg']

#Resimlerin listesini oluşturma
resim_liste = [img.open(dosya) for dosya in resimler_listesi]

# İlk resmi bir GIF dosyası olarak kaydetme
resim_liste[0].save('mouse.gif',save_all=True,
            append_images=resim_liste[1:], # resimlerin geri kalanını ekle
            duration=1000,loop=0)
