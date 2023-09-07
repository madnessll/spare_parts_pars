import csv
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# прокручиваю страницу полностью до конца со всеми товарами и сохраняю это все в index_selenium.html

# url = 'https://ag-jp.ru/vse-marki/'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     scroll_position = 0
#     while True:
#         browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(2)  # Может потребоваться регулировать это значение
#         new_scroll_position = browser.execute_script("return window.scrollY;")
#         if new_scroll_position == scroll_position:
#             break
#         scroll_position = new_scroll_position
#     with open('index_selenium.html', 'w', encoding='utf-8') as file:
#         file.write(browser.page_source)


# после прохожусь по html и собираю все ссылки на товары и сохраняю их в all_urls.txt

# count = 0
# with open('index_selenium.html', 'r', encoding='utf-8') as file:
#     content = file.read()
#     soup = BeautifulSoup(content, 'lxml')
#     al = soup.find_all(class_='c-good-container__image')
#     with open('all_urls.txt', 'w', encoding='utf-8') as file_txt:
#         for el in al:
#             file_txt.write(f"https://ag-jp.ru{el.find('a').get('href')}")
#             file_txt.write('\n')


# прохожу по всем ссылкам и записываю данные в таблцу

headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
with open('all_urls.txt', 'r', encoding='utf-8') as file_txt:
    with open('table.csv', 'w', encoding='utf-8', newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(
            (
                'Название', 'Цена', 'Ссылка', 'Фотографии'
            )
        )
        urls = file_txt.read().split()
        count = 0
        for url in urls:
            count += 1
            # print(url)
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            try:
                price = soup.find(class_="c-product-info__price-block__price").text.strip()
            except AttributeError:
                price = 'Нет цены'
            try:
                name = soup.find(class_="h2").text
            except AttributeError:
                name = 'Нет названия'
            images_all = soup.find_all(class_='c-img-slider-container')
            images_finish = ', '.join([img.find('img').get('src') for img in images_all])
            # print(images_finish)
            writer.writerow(
                (
                    name, price, url, images_finish
                )
            )
            print(count)








