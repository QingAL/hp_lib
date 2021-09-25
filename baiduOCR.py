from aip import AipOcr
from PIL import ImageGrab
import numpy as np
import keyboard
from fuzzywuzzy import fuzz
import os


def fuzzyMatch(text):
    # 模糊匹配
    matchfac = -1
    matchkey = ""
    for key in hp_lib.keys():
        matchtemp = fuzz.ratio(text, key)
        if matchtemp > matchfac:
            matchkey = key
            matchfac = matchtemp
    print("OCR:", end="")
    print(text)
    print("match:", end="")
    print(matchkey)
    print("answer:", end="")
    print(hp_lib[matchkey])
    print("*********************************************")


def baiduOCR(picfile):
    # 百度提供ocr
    """ 你的 APPID AK SK """
    APP_ID = ""
    API_KEY = ""
    SECRET_KEY = ""
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    i = open(picfile, 'rb')
    img = i.read()
    message = client.form(img)
    i.close()
    # 输出文本内容
    text = ''
    for res_dict in message['forms_result']:
        for head_dict in res_dict['header']:
            text += head_dict['words']

    text = text.split('?')[0] + '?'
    fuzzyMatch(text)


if __name__ == '__main__':
    hp_lib = np.load('hp_lib.npy', allow_pickle=True).item()
    small_bbox = (299, 642, 1064, 759)
    big_bbox = (300, 1000, 1800, 1250)
    imgPath = "pics/"
    folder = os.path.exists(imgPath)
    if not folder:
        os.mkdir(imgPath)
    print('===AutoAnswer Loading===')
    while True:
        try:
            if keyboard.is_pressed('q'):
                bbox = small_bbox
                img = ImageGrab.grab(bbox)
                img_path = "pics/" + "temp.png"
                img.save(img_path)
                baiduOCR('pics/temp.png')
            elif keyboard.is_pressed('w'):
                bbox = big_bbox
                img = ImageGrab.grab(bbox)
                img_path = "pics/" + "temp.png"
                img.save(img_path)
                baiduOCR('pics/temp.png')
            else:
                pass
        except:
            break
