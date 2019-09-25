from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import csv
from PIL import Image
import os


#********** Имена файлов ***********


# ixyt.info/ru,  ixyt.info/en/  и  ixyt.info/de
def sel():

    browser = webdriver.Chrome()
    browser.set_window_size(1280, 1024)
    url = 'https://www.google.ru/search?newwindow=1&as_st=y&tbm=isch&sxsrf=ACYBGNRiRgKLtiqX67Phrfw9raaOoqQplA%3A1567842593121&sa=1&ei=IWFzXamRB4XjmwWWg42ABQ&q=site%3Aixyt.info&oq=site&tbs=iar:s'
    browser.get(url)
    time.sleep(3)
    # блок прокрутки

    op = 0


    for q in range(0, 25):
        k = str(q*800)
        time.sleep(0.5)
        browser.execute_script("window.scrollTo(0," + k + ")")


    button = browser.find_element_by_css_selector('#smb')
    button.click()

    for q in range(0, 30):
        g = str(int(k) + q * 800)
        time.sleep(1)
        browser.execute_script("window.scrollTo(0," + g + ")")

    browser.execute_script("window.scrollTo(0,0)")

    for q in range(0, 155):
        k = str(175 + 242 * q)
        time.sleep(0.5)
        browser.execute_script("window.scrollTo(0," + k + ")")
        op += 1
        browser.save_screenshot(str(op) + '.jpg')
        img = Image.open(str(op) + '.jpg')
        area = (0, 0, 1240, 885)
        cropped_img = img.crop(area)
        rgb_im = cropped_img.convert('RGB')
        rgb_im.save(str(op) + '.jpg')



    time.sleep(2)
    url2 = 'https://www.google.ru/search?as_st=y&tbm=isch&as_q=&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=ixyt.info/ru&safe=images&tbs=iar:s'
    browser.get(url2)
    browser.refresh()
    time.sleep(2)

    for q in range(0, 11):
        k =str(175 + 242 * q) #str(175 + (236+0.5*q)*q)
        time.sleep(1)
        browser.execute_script("window.scrollTo(0," + k + ")")
        op += 1
        browser.save_screenshot(str(op) + '.jpg')
        img = Image.open(str(op) + '.jpg')
        area = (0, 0, 1240, 885)
        cropped_img = img.crop(area)
        rgb_im = cropped_img.convert('RGB')
        rgb_im.save(str(op) + '.jpg')
    

    time.sleep(2)
    url3 = 'https://www.google.ru/search?as_st=y&tbm=isch&as_q=&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=ixyt.info/en/&safe=images&tbs=iar:s'
    browser.get(url3)
    browser.refresh()
    time.sleep(2)

    for q in range(0, 20):
        k = str(500 * q)
        time.sleep(0.5)
        browser.execute_script("window.scrollTo(0," + k + ")")
    browser.execute_script("window.scrollTo(0,0)")

    for q in range(0, 14):
        k =str(175 + 242 * q) #str(175 + (236+0.5*q)*q)
        time.sleep(1)
        browser.execute_script("window.scrollTo(0," + k + ")")
        op += 1
        browser.save_screenshot(str(op) + '.jpg')
        img = Image.open(str(op) + '.jpg')
        area = (0, 0, 1240, 885)
        cropped_img = img.crop(area)
        rgb_im = cropped_img.convert('RGB')
        rgb_im.save(str(op) + '.jpg')
    

    #https://www.google.ru/search?as_st=y&tbm=isch&as_q=&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=ixyt.info/de&safe=images&tbs=iar:s
    time.sleep(2)
    url4 = 'https://www.google.ru/search?as_st=y&tbm=isch&as_q=&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=ixyt.info/de&safe=images&tbs=iar:s'
    browser.get(url4)
    browser.refresh()
    time.sleep(2)
    for q in range(0, 14):
        k =str(175 + 242 * q) #str(175 + (236 + 0.5 * q) * q)
        time.sleep(1)
        browser.execute_script("window.scrollTo(0," + k + ")")
        op += 1
        browser.save_screenshot(str(op) + '.jpg')
        img = Image.open(str(op) + '.jpg')
        area = (0, 0, 1240, 885)
        cropped_img = img.crop(area)
        rgb_im = cropped_img.convert('RGB')
        rgb_im.save(str(op) + '.jpg')


    browser.quit()





name = requests.get('https://ixyt.info/sitemap.xml')
print(name.text)
soup = BeautifulSoup(name.text, 'html.parser')
poisk = soup.find_all('loc')
name_city_arr = []
name_country_arr = []
for q in range(0, len(poisk)):
    name_city = poisk[q].text.split('/')[-1]
    name_city_arr.append(name_city)
    name_country = poisk[q].text.split('/')[-2]
    name_country_arr.append(name_country)

name_country_arr = name_country_arr[6:]

name_city_arr = name_city_arr[6:]
print(len(name_country_arr))
print(len(name_city_arr))

data_read = [[]]
try:
    with open('base.csv', 'r') as fp:
        reader = csv.reader(fp, delimiter=',', quotechar='"')
        # next(reader, None)  # skip the headers
        data_read = [row for row in reader]

except Exception as e:

    with open('base.csv', 'w') as f:
        wr = csv.writer(f,delimiter=',',lineterminator='\r')
        wr.writerows([(name_country_arr[i], name_city_arr[i]) for i in range(len(name_country_arr))])

    with open('base.csv', 'r') as fp:
        reader = csv.reader(fp, delimiter=',', quotechar='"')
        # next(reader, None)  # skip the headers
        data_read = [row for row in reader]

peresech = []
peresech_country = []
poisk = []

for q in range(0, len(data_read)):
    try:
        poisk.append(data_read[q][1])
    except:
        ggg = 0


for x in name_city_arr:
    if x not in poisk:
        peresech.append(x)
        ind = name_city_arr.index(x)
        peresech_country.append(name_country_arr[ind])

print(peresech)

if peresech != []:

    with open('base.csv', 'a', encoding='utf-8') as f:
        wr = csv.writer(f, delimiter=',', lineterminator='\r')
        wr.writerows([(peresech_country[i], peresech[i]) for i in range(len(peresech))])

    sel()
    for q in range(0, len(peresech)):
        k = int(q+1) % 193 + 1

        mypath = './/' + 'image' + '//' + str(peresech_country[q])  #'.//' + str(peresech_country[q]) + '//' + str(peresech[q]) + '.jpg'
        try:
            os.makedirs(mypath)
        except:
            gggg = 0
        filepath = os.path.join(mypath, str(peresech[q]) + '-where-to-go' + '.jpg')

        fail = open(filepath, 'w')

        img = Image.open('./' + str(k) + '.jpg')

        img.save(filepath, quality=22, progressive=True)

        pass
    pass

# конец блока прокрутки


# скриншот


