from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


# Настройки текста
font = ImageFont.truetype('OpenSans-Regular.ttf',25)
text_color = (255,255,255)
img = Image.open('image.png')


# Ф-я создания объекта фото
def insertText(text,position):
    draw = ImageDraw.Draw(img)
    draw.text(position, text, text_color, font)


# Вписываем три текста
insertText("20",(1113, 90))
insertText("90",(1140, 157))
insertText("13",(1217, 234))



# Рендерим
img.save('header.png')