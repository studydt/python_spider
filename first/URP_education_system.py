import os
import pytesseract
import pyautogui
from time import sleep
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#pytesseract.pytesseract.tesseract_cmd = 'c:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
option = webdriver.ChromeOptions()
#option.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=option)          #set chrome interface
download = "C:\\Users\\万水千山\\Downloads\\validateCodeAction.jpg"

def get_html(url):
    if(os.path.isfile(download)):
        os.remove(download)
    browser.get(url)
    img = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'vchart')))
    action = ActionChains(browser)
    action.context_click(img).perform()
    pyautogui.typewrite(['down', 'down', 'enter', 'enter'])
    sleep(0.5)
    pyautogui.typewrite(['enter'])

def funOCR():
    image = Image.open(download)
    image =image.convert('L')
    threshold = 90
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table, '1')
    text = pytesseract.image_to_string(image, config=' --psm 7')   #Treat the image as a single text line
    return text

def click(text,ID, passwords):
    input01 = browser.find_element_by_name('zjh')
    input01.send_keys(ID)
    input02 = browser.find_element_by_name('mm')
    input02.send_keys(passwords)
    input03 = browser.find_element_by_name('v_yzm')
    input03.send_keys(text)
    action = ActionChains(browser)
    click_ = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'btnSure')))
    action.click(click_).perform()

def main():
    url = "http://XXXXXXXXXX"
    ID = 'XXXXXX'
    passwords = 'XXXXXX'
    get_html(url)
    sleep(4)
    text = funOCR()
    click(text, ID, passwords)

if __name__ == '__main__':
    main()