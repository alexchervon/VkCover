from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import requests
import urllib.parse

# Ваш токен
token = ""


# Настройки текста
font = ImageFont.truetype('OpenSans-Regular.ttf',25)
text_color = (255,255,255)

# Выбор изображения на которое будем добавлять текст
img = Image.open('image.png')

# Настройка шапки
CONST_WIDTH = 1590 #Размер width
CONST_HEIGHT = 400 #Размер height
CONST_NAME = "header" #Название фото-шапки на выходе

# Ф-я создания объекта фото
def insertText(text,position):
    draw = ImageDraw.Draw(img)
    draw.text(position, text, text_color, font)


# Вписываем три текста
insertText("24",(1113, 90))
insertText("97",(1140, 157))
insertText("17",(1217, 234))


# Рендерим
img.save(CONST_NAME+'.png')


# Общая Ф-я для отпрвки запросов
def apiVKRequests(method,param):
    return requests.request('POST', 'https://api.vk.com/method/'+method+'?'+urllib.parse.urlencode(param)+'&access_token='+token).json()


# Замена шапки
def setPhoto(hash,photo):
    param = {
        'hash': hash,
        'photo':photo,
        'v': 5.80
    }

    if 'response' in apiVKRequests('photos.saveOwnerCoverPhoto',param):
        print('HEADER CHANGED')
    else: print('error setPhoto')


# Получение url для загрузки фото
def uploadServer():
    param = {
        'group_id':138003925,
        'v':5.80,
        'crop_x2':CONST_WIDTH,
        'crop_y2':CONST_HEIGHT
    }

    getUrl = apiVKRequests('photos.getOwnerCoverPhotoUploadServer',param)
    if 'response' in getUrl:
        file = {'file': open(CONST_NAME+'.png', 'rb')}
        sendPhoto = requests.post(getUrl['response']['upload_url'], files=file).json()
        hash = sendPhoto['hash']
        photo = sendPhoto['photo']
        setPhoto(hash, photo)
    else: print('error uploadServer',set)



uploadServer()
