import telebot
from google_images_download import google_images_download
import os

TOKEN = "1009225223:AAFQe7M7bKOec14E0NoMV7bpo_krB_jcb7U"
bot = telebot.TeleBot(TOKEN)

response =google_images_download.googleimagesdownload()


def download_images(query):
    # keywords is the search query
    # format is the image file format
    # limit is the number of images to be downloaded
    # print urs is to print the image file url
    # size is the image size which can
    # be specified manually ("large, medium, icon")
    # aspect ratio denotes the height width ratio
    # of images to download. ("tall, square, wide, panoramic")
    q = query
    arguments = {"keywords": q,
                 "format": "jpg",
                 "limit": 1,
                 "print_urls": True,
                 "size": "medium",
                 "aspect_ratio": "tall",
                 "output_directory": 'C:\\Users\\astro\\Downloads\\Images',
                 "no_directory": True}
    try:
        path = response.download(arguments)
        return path

    # Handling File NotFound Error
    except FileNotFoundError:
        arguments = {"keywords": query,
                     "format": "jpg",
                     "limit": 1,
                     "print_urls": True,
                     "size": "medium",
                     "output_directory": 'C:\\Users\\astro\\Downloads\\Images',
                     "no_directory": True}

        # Providing arguments for the searched query
        try:
            # Downloading the photos based
            # on the given arguments
            path = response.download(arguments)
            return path
        except:
            pass


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне. Ты можешь отправить мне сообщение (текст), а я в ответ отправлю тебе картинку, на которой изображено то, что ты написал. ')

@bot.message_handler(content_types=['text'])
def send_image(message):
    try:
        search_query = message.text
        tup = download_images(search_query)
        dict = tup[0]
        item = dict.popitem()
        path = item[1].pop()
        img = open(path, 'rb')
        bot.send_photo(message.chat.id, img)
        img.close()
        os.remove(path)
    except:
        pass


bot.polling(none_stop=True, interval=0)