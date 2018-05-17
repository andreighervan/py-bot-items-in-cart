from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import csv
import pymysql
import time
import datetime
import io

# set the proxies to hide actual ID

now = datetime.datetime.now()
start_time = time.time()

print(now.strftime("%Y-%m-%d %H:%M:%S"))
conn = pymysql.connect(host='localhost', user='root', password='', db='amazon_sample')
a = conn.cursor()
sql = 'SELECT (Product_url) from `bedding` WHERE Id BETWEEN 1 AND 1000;'
a.execute(sql)
data = a.fetchall()


# set the proxies to hide actual IP

proxies = {
    'http': 'http://5.189.133.231:80',
    'https': 'https://27.111.43.178:8080'
}

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--proxy-server="%s"' % ';'.join(['%s=%s' % (k, v) for k, v in proxies.items()]))

driver = webdriver.Chrome(executable_path="C:\\Users\Andrei-PC\Downloads\webdriver\chromedriver.exe",
                          chrome_options=chrome_options)
header = ['Product title', 'Product price', 'Items in cart','Items in cart(number)','Link']

with open('csv/bot_1.csv', "w") as output:
    writer = csv.writer(output)
    writer.writerow(header)
links = []
for i in range(len(data)):
    links.extend(data[i])
for i in range(len(links)):
    driver.get(links[i])

    product_title = driver.find_elements_by_xpath('//*[@id="productTitle"][1]')
    prod_title = [x.text for x in product_title]

    try:
        prod_price = driver.find_element_by_xpath('//span[@id="priceblock_ourprice"]').text
    except:
        print('no price v1')

    try:
        prod_price = driver.find_element_by_xpath('(//span[@id="_price"]/span)[4]').text
    except:
        print('no price v2')

    try:
        prod_price = driver.find_element_by_xpath('//span[@id="priceblock_saleprice"]').text
    except:
        print('no price v3')

    try:
        prod_price = driver.find_element_by_xpath('(//span[contains(@class, "a-color-price")])[1]').text
    except:
        print('no price v4')

    try:
        driver.execute_script("window.scrollTo(0,200)")
        sizemenu = driver.find_element_by_id('dropdown_selected_size_name')
        sizemenu.click()
        select = driver.find_element_by_id('size_name_1')  # medium size
        select.click()
        driver.execute_script("window.scrollTo(0,50)")
        sleep(3)
    except:
        print('no select')

    try:
        driver.execute_script("window.scrollTo(0,150)")
        driver.find_element_by_xpath('//*[@id="add-to-cart-button"]').click()
        sleep(2)
    except:
        print('no add to cart button five')

    try:
        driver.execute_script("document.getElementById('add-to-cart-button-ubb').click()")
        sleep(2)
    except:
        print('no add to cart button six')

    try:
        driver.execute_script("document.getElementById('buybox-see-all-buying-choices-announce').click()")
        sleep(3)
    except:
        print('no add to cart button seven')

    try:
        driver.execute_script("document.getElementById('siNoCoverage-announce').click()")
    except:
        print('no add to cart button eight')

    try:
        driver.execute_script("window.scrollTo(0,150)")
        driver.find_element_by_xpath('(//input[@name="submit.addToCart"])[1]').click()
    except:
        print('no add to cart button ten')

    try:
        sleep(3)
        driver.execute_script("window.scrollTo(0,50)")
        driver.find_element_by_xpath('//form[@id="smartShelfFormContinue"]/span/span/input').click()
    except:
        print('no continue button')

    try:
        driver.find_element_by_xpath('//*[@id="hlb-view-cart"]/span/a').click()
        sleep(3)
    except:
        print('no cart button')

    try:
        driver.execute_script("window.scrollTo(0,470)")
        sleep(2)
        driver.find_element_by_xpath('(//input[contains(@name,"delete")])[2]').click()
        sleep(3)
    except:
        print('no delete one')

    try:
        driver.find_element_by_xpath('(//input[contains(@name,"delete")])[2]').click()
        sleep(3)
    except:
        print('no delete two')

    try:
        driver.find_element_by_xpath('(//input[contains(@name,"delete")])[2]').click()
        sleep(3)
    except:
        print('no delete three')

    try:
        driver.find_element_by_xpath('(//input[contains(@name,"delete")])[2]').click()
        sleep(3)
    except:
        print('no delete four')

    try:
        driver.find_element_by_xpath('(//input[contains(@name,"delete")])[2]').click()
        sleep(3)
    except:
        print('no delete five')

    try:
        driver.find_element_by_xpath('(//input[contains(@name,"delete")])[2]').click()
        sleep(3)
    except:
        print('no delete six')

    try:
        driver.execute_script("window.scrollTo(0,10)")
        sleep(3)
        driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]/span[2]').click()
        driver.find_element_by_xpath('//*[@id="dropdown1_9"]').click()
        quantity_xpath = '//*[@id="activeCartViewForm"]/div[2]/div/div[4]/div/div[3]/div/div/input'
        quantity_el = driver.find_element_by_xpath(quantity_xpath)
        quantity_el.send_keys("999" + Keys.ENTER)
        sleep(3)
    except:
        print('no itrack v1')

    try:
        driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]/span[2]').click()
        driver.find_element_by_xpath('//*[@id="dropdown1_9"]').click()
        quantity_xpath = '//*[@id="activeCartViewForm"]/div[2]/div/div[4]/div/div[3]/div/div/input'
        quantity_el = driver.find_element_by_xpath(quantity_xpath)
        quantity_el.send_keys("999" + Keys.ENTER)
        sleep(2)
    except:
        print('no itrack v2')

    items_cart = driver.find_elements_by_xpath('//div[@class="a-alert-content"]/span')
    items_in_cart = [x.text for x in items_cart]
    items_in_cart = ', '.join(items_in_cart)

    try:
        outofstock = driver.find_element_by_xpath('//*[@id="pantry-availability"]')
        data = [prod_title[0], 'No price', 'No items in cart','No items number','No link']
        with open('csv/bot_1.csv', "a", newline="") as output:
            writer = csv.writer(output)
            writer.writerow(data)
    except:
        print('no items')

    try:
        notfound = driver.find_element_by_xpath('//div[@id="g"]/div/a/img')
        data = ['Product not found', 'No price', 'No items in cart','No items number','No link']
        with open('csv/bot_1.csv', "a", newline="") as output:
            writer = csv.writer(output)
            writer.writerow(data)
    except:
        print('no items v2')

    try:
        data = [prod_title[0], prod_price, items_in_cart, '',links[i]]
    except:
        print('no items v3 ')

    with io.open('csv/bot_1.csv', "a", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(data)
    print('I solved this link %s' % (links[i]))
    print('Number of product %s' % (i + 1))

print("--- %s seconds ---" % (time.time() - start_time))
print(now.strftime("%Y-%m-%d %H:%M:%S"))
