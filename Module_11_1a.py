from PIL import Image, ImageOps

filename = "ford.jpg"
with Image.open(filename) as img:
    img.load()
img.show()
print(f'Параметры изображения: тип: {img.format}, размер: {img.size}, цвет: {img.mode}')

crop_img = img.crop((100, 150, 300, 300))
print(f'Изменённый размер: {crop_img.size}')
crop_img.show()
crop_img.save('ford_crop.jpeg')


rotated_img = img.rotate(45, expand=True)
rotated_img.show()
rotated_img.save('ford_rotated.jpeg')

gray_img = img.convert("L")
gray_img.show()
gray_img.save('ford_gray.pdf')

color_img = ImageOps.colorize(gray_img, black ="blue", white ="red")
color_img.show()
color_img.save('ford_color.pdf')

new_img = rotated_img.resize((1200, 800))
new_img.show()
new_img.save('ford_new.png')
