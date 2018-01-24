from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
url = "https://www.amazon.com/gp/product/B0118QC1BA/ref=s9_acsd_cdeal_hd_bw_bFmNr_c_x_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=AZJF41VDFJMPA4XY6D95&pf_rd_t=101&pf_rd_p=32a36b64-58af-5269-b81a-c1030ee0250c&pf_rd_i=3760911"

driver = webdriver.Chrome(executable_path="C:\\Users\Andrei\Downloads\chromedriver_win32\chromedriver.exe")
driver.get(url)

sleep(3)

driver.find_element_by_xpath('//*[@id="submit.add-to-cart"]/span/input').click()

sleep(3)

# driver.find_element_by_xpath('//*[@id="smartShelfAddToCartContinue"]/span/input')
driver.execute_script("document.getElementById('smartShelfAddToCartNative').click()")

sleep(3)

# items_cart = driver.find_element_by_xpath('//div[@class="a-alert-content"]/span')

driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]/span[2]').click()
driver.find_element_by_xpath('//*[@id="dropdown1_9"]').click()
quantity_xpath = '//*[@id="activeCartViewForm"]/div[2]/div/div[4]/div/div[3]/div/div/input'
quantity_el = driver.find_element_by_xpath(quantity_xpath)
quantity_el.send_keys("999" + Keys.ENTER)

sleep(2)

items_cart = driver.find_elements_by_xpath('//div[@class="a-alert-content"]/span')
items=[x.text for x in items_cart]

print items[1]
