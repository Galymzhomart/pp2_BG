from PIL import Image

# Открываем изображение
image = Image.open("Lab_7\images\image3.jpg")

# Уменьшаем до 50% от оригинального размера
new_size = (image.width // 2, image.height // 2)
resized_image = image.resize(new_size, Image.LANCZOS)

# Сохраняем уменьшенное изображение
resized_image.save("Lab_7\images\image3.jpg")
